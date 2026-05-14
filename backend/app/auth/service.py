"""Auth business logic — signup, login, session management."""

import uuid
from datetime import UTC, datetime, timedelta

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.schemas import (
    AccountOut,
    LearnerProfileOut,
    LoginResponse,
    MeResponse,
    SignupRequest,
)
from app.core.errors import AppError, bad_request, conflict, unauthorized
from app.core.security import generate_token, hash_password, verify_password
from app.db.models import Account, EmailToken, LearnerProfile, Session, Subscription
from app.email.service import send_parent_invite_email, send_verification_email

SESSION_TTL_DAYS = 30
EMAIL_VERIFY_TTL_HOURS = 24
PARENT_INVITE_TTL_DAYS = 7


def _now() -> datetime:
    return datetime.now(UTC)


def _account_out(account: Account) -> AccountOut:
    return AccountOut(
        id=account.id,
        email=account.email,
        role=account.role,
        display_name=account.display_name,
        email_verified=account.email_verified,
        is_active=account.is_active,
        is_under_13=account.is_under_13,
    )


async def signup(db: AsyncSession, body: SignupRequest) -> None:
    """Create a new account. Returns nothing — learner must verify email before login."""
    existing = await db.scalar(select(Account).where(Account.email == body.email))
    if existing is not None:
        raise conflict("An account with that email already exists")

    now = _now()
    is_under_13 = body.is_under_13 and body.role == "learner"
    account = Account(
        id=uuid.uuid4(),
        email=body.email,
        password_hash=hash_password(body.password),
        role=body.role,
        display_name=body.display_name,
        # Skip email verification — accounts are active immediately
        email_verified=not is_under_13,
        is_active=not is_under_13,
        is_under_13=is_under_13,
        parent_invite_email=str(body.parent_email) if is_under_13 else None,
        created_at=now,
        updated_at=now,
    )
    db.add(account)
    await db.flush()  # get account.id

    if body.role == "learner":
        # Learner profile starts without track/world (set during onboarding §8.1)
        db.add(
            LearnerProfile(
                account_id=account.id,
                track="",
                world="",
            )
        )
        db.add(
            Subscription(
                account_id=account.id,
                status="trial",
                trial_ends_at=now + timedelta(days=14),
                updated_at=now,
            )
        )

    if is_under_13 and body.parent_email:
        # Under-13 still requires parent consent before account is active
        parent_token = EmailToken(
            token=generate_token(),
            account_id=account.id,
            purpose="parent_invite",
            expires_at=now + timedelta(days=PARENT_INVITE_TTL_DAYS),
        )
        db.add(parent_token)
        await db.commit()
        await send_parent_invite_email(
            str(body.parent_email),
            body.display_name or body.email,
            parent_token.token,
        )
    else:
        # No email verification — account is immediately active
        await db.commit()


async def verify_email(db: AsyncSession, token: str) -> None:
    now = _now()
    row = await db.scalar(
        select(EmailToken).where(
            EmailToken.token == token,
            EmailToken.purpose == "email_verify",
            EmailToken.used_at.is_(None),
            EmailToken.expires_at > now,
        )
    )
    if row is None:
        raise bad_request("Invalid or expired verification token")

    row.used_at = now
    account = await db.get(Account, row.account_id)
    if account is None:
        raise bad_request("Account not found")
    account.email_verified = True
    account.is_active = True
    account.updated_at = now
    await db.commit()


async def parent_verify(
    db: AsyncSession, token: str, parent_display_name: str | None, parent_password: str | None
) -> None:
    """Activate a learner account after parent verification (§12.4)."""
    now = _now()
    row = await db.scalar(
        select(EmailToken).where(
            EmailToken.token == token,
            EmailToken.purpose == "parent_invite",
            EmailToken.used_at.is_(None),
            EmailToken.expires_at > now,
        )
    )
    if row is None:
        raise bad_request("Invalid or expired parent invite token")

    row.used_at = now
    learner = await db.get(Account, row.account_id)
    if learner is None:
        raise bad_request("Learner account not found")

    learner.email_verified = True
    learner.is_active = True
    learner.updated_at = now
    await db.commit()


async def login(
    db: AsyncSession, email: str, password: str
) -> tuple[str, LoginResponse]:
    """Return (session_id, response). Caller sets the session cookie."""
    account = await db.scalar(select(Account).where(Account.email == email))

    if account is None or not verify_password(password, account.password_hash):
        raise unauthorized("Invalid email or password")

    if not account.email_verified:
        raise AppError(403, "email_not_verified", "Please verify your email before logging in")

    if not account.is_active:
        raise AppError(
            403,
            "account_inactive",
            "Your account is pending parent verification",
        )

    now = _now()
    session = Session(
        id=generate_token(32),
        account_id=account.id,
        csrf_token=generate_token(32),
        created_at=now,
        expires_at=now + timedelta(days=SESSION_TTL_DAYS),
    )
    db.add(session)
    await db.commit()
    await db.refresh(session)

    return session.id, LoginResponse(account=_account_out(account), csrf_token=session.csrf_token)


async def logout(db: AsyncSession, session_id: str) -> None:
    session = await db.get(Session, session_id)
    if session is not None:
        await db.delete(session)
        await db.commit()


async def get_session(db: AsyncSession, session_id: str) -> Session:
    now = _now()
    session = await db.scalar(
        select(Session).where(
            Session.id == session_id,
            Session.expires_at > now,
        )
    )
    if session is None:
        raise unauthorized()
    return session


def _profile_out(account: Account) -> LearnerProfileOut | None:
    p = account.profile
    if p is None:
        return None
    import json as _json
    try:
        badges: list[str] = _json.loads(p.badges_json)
    except Exception:
        badges = []
    return LearnerProfileOut(
        track=p.track,
        world=p.world,
        current_unit=p.current_unit,
        current_lesson=p.current_lesson,
        badges=badges,
        public_profile=p.public_profile,
    )


async def me(db: AsyncSession, session_id: str) -> MeResponse:
    session = await get_session(db, session_id)
    account = await db.get(Account, session.account_id)
    if account is None:
        raise unauthorized()
    # Eagerly load profile for learners
    if account.role == "learner" and account.profile is None:
        await db.refresh(account, ["profile"])
    return MeResponse(
        account=_account_out(account),
        csrf_token=session.csrf_token,
        profile=_profile_out(account),
    )
