"""Account management — GET /v1/me, PATCH /v1/me, DELETE /v1/me (§11.2)."""

from datetime import UTC, datetime, timedelta

from fastapi import APIRouter, Depends, Response
from sqlalchemy import delete as sa_delete, exists, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.accounts.schemas import PatchMeRequest
from app.auth.dependencies import (
    SESSION_COOKIE,
    get_current_account,
    get_current_session,
    require_csrf,
)
from app.auth.schemas import AccountOut, MeResponse
from app.auth.service import _profile_out
from app.db.models import Account, ParentLink, ProgressEvent, Session
from app.db.session import get_db

router = APIRouter(prefix="/v1", tags=["accounts"])


@router.get("/me")
async def get_me(
    session: Session = Depends(get_current_session),
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
) -> MeResponse:
    if account.role == "learner" and account.profile is None:
        await db.refresh(account, ["profile"])

    # Log session_start once per UTC day for learners who have completed onboarding
    if account.role == "learner" and account.profile is not None and account.profile.track:
        try:
            now = datetime.now(UTC)
            day_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
            day_end = day_start + timedelta(days=1)
            already = await db.scalar(
                select(exists()).where(
                    ProgressEvent.account_id == account.id,
                    ProgressEvent.event_type == "session_start",
                    ProgressEvent.created_at >= day_start,
                    ProgressEvent.created_at < day_end,
                )
            )
            if not already:
                db.add(ProgressEvent(
                    account_id=account.id,
                    event_type="session_start",
                    created_at=now,
                ))
                await db.commit()
        except Exception:
            pass

    return MeResponse(
        account=AccountOut(
            id=account.id,
            email=account.email,
            role=account.role,
            display_name=account.display_name,
            email_verified=account.email_verified,
            is_active=account.is_active,
            is_under_13=account.is_under_13,
        ),
        csrf_token=session.csrf_token,
        profile=_profile_out(account),
    )


@router.patch("/me")
async def patch_me(
    body: PatchMeRequest,
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
    _csrf: None = Depends(require_csrf),
) -> AccountOut:
    if body.display_name is not None:
        account.display_name = body.display_name
    if body.public_profile is not None and account.role == "learner" and account.profile:
        account.profile.public_profile = body.public_profile
    account.updated_at = datetime.now(UTC)
    await db.commit()
    return AccountOut(
        id=account.id,
        email=account.email,
        role=account.role,
        display_name=account.display_name,
        email_verified=account.email_verified,
        is_active=account.is_active,
        is_under_13=account.is_under_13,
    )


@router.delete("/me", status_code=204)
async def delete_me(
    response: Response,
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
    _csrf: None = Depends(require_csrf),
) -> None:
    # Remove ParentLink rows on both sides (RESTRICT FK — must go before account)
    await db.execute(
        sa_delete(ParentLink).where(
            or_(
                ParentLink.parent_account_id == account.id,
                ParentLink.learner_account_id == account.id,
            )
        )
    )
    # Ensure subscription is loaded so ORM cascade can delete it (RESTRICT FK)
    await db.refresh(account, ["subscription"])
    # ORM cascade="all, delete-orphan" handles learner_profile and subscription;
    # DB cascade handles sessions, email_tokens, and progress_events.
    await db.delete(account)
    await db.commit()
    response.delete_cookie(SESSION_COOKIE, path="/")
