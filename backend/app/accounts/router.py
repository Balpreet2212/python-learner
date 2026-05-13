"""Account management — GET /v1/me, PATCH /v1/me (§11.2)."""

from datetime import UTC, datetime

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.accounts.schemas import PatchMeRequest
from app.auth.dependencies import (
    get_current_account,
    get_current_session,
    require_csrf,
)
from app.auth.schemas import AccountOut, MeResponse
from app.db.models import Account, Session
from app.db.session import get_db

router = APIRouter(prefix="/v1", tags=["accounts"])


@router.get("/me")
async def get_me(
    session: Session = Depends(get_current_session),
    account: Account = Depends(get_current_account),
) -> MeResponse:
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
