"""Auth routes — §11.2 Auth & accounts endpoints."""

from fastapi import APIRouter, Depends, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import service
from app.auth.dependencies import (
    SESSION_COOKIE,
    get_current_session,
    require_csrf,
)
from app.auth.schemas import (
    LoginRequest,
    LoginResponse,
    ParentVerifyRequest,
    SignupRequest,
    VerifyEmailRequest,
)
from app.config import settings
from app.core.rate_limit import limit_auth
from app.db.models import Session
from app.db.session import get_db

router = APIRouter(prefix="/v1/auth", tags=["auth"])

_IS_PROD = settings.app_env == "production"


def _set_session_cookie(response: Response, session_id: str) -> None:
    response.set_cookie(
        key=SESSION_COOKIE,
        value=session_id,
        httponly=True,
        secure=_IS_PROD,
        samesite="lax",
        max_age=settings.session_max_age,
        path="/",
    )


@router.post("/signup", status_code=201)
async def signup(
    body: SignupRequest,
    request: Request,
    db: AsyncSession = Depends(get_db),
    _rl: None = Depends(limit_auth),
) -> dict[str, str]:
    await service.signup(db, body)
    if body.is_under_13:
        return {"status": "pending_parent_verification"}
    return {"status": "verification_email_sent"}


@router.post("/login")
async def login(
    body: LoginRequest,
    request: Request,
    response: Response,
    db: AsyncSession = Depends(get_db),
    _rl: None = Depends(limit_auth),
) -> LoginResponse:
    session_id, result = await service.login(db, body.email, body.password)
    _set_session_cookie(response, session_id)
    return result


@router.post("/logout", status_code=204)
async def logout(
    response: Response,
    db: AsyncSession = Depends(get_db),
    session: Session = Depends(get_current_session),
    _csrf: None = Depends(require_csrf),
) -> None:
    await service.logout(db, session.id)
    response.delete_cookie(SESSION_COOKIE, path="/")


@router.post("/verify-email", status_code=200)
async def verify_email(
    body: VerifyEmailRequest,
    db: AsyncSession = Depends(get_db),
) -> dict[str, str]:
    await service.verify_email(db, body.token)
    return {"status": "email_verified"}


@router.post("/parent-verify", status_code=200)
async def parent_verify(
    body: ParentVerifyRequest,
    db: AsyncSession = Depends(get_db),
) -> dict[str, str]:
    await service.parent_verify(
        db, body.token, body.parent_display_name, body.parent_password
    )
    return {"status": "learner_activated"}
