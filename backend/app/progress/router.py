"""Progress & onboarding routes (§11.2)."""

from typing import Literal

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_account, require_csrf
from app.auth.schemas import LearnerProfileOut
from app.auth.service import _profile_out
from app.core.errors import bad_request, forbidden
from app.db.models import Account
from app.db.session import get_db

router = APIRouter(prefix="/v1/learner", tags=["progress"])


class OnboardingRequest(BaseModel):
    track: Literal["junior", "core"]
    world: Literal["fantasy", "scifi", "mystery"]


@router.post("/onboarding")
async def set_onboarding(
    body: OnboardingRequest,
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
    _csrf: None = Depends(require_csrf),
) -> LearnerProfileOut:
    """Set track and world for a learner. Idempotent (§11.2)."""
    if account.role != "learner":
        raise forbidden("Only learner accounts can set onboarding preferences")
    if account.profile is None:
        await db.refresh(account, ["profile"])
    if account.profile is None:
        raise bad_request("Learner profile not found")

    account.profile.track = body.track
    account.profile.world = body.world
    await db.commit()

    result = _profile_out(account)
    if result is None:
        raise bad_request("Profile unavailable after save")
    return result
