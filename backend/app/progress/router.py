"""Progress & onboarding routes (§11.2)."""

from datetime import UTC, datetime
from typing import Literal

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_account, require_csrf
from app.auth.schemas import LearnerProfileOut
from app.auth.service import _profile_out
from app.content.service import _date_key, _week_key
from app.core.errors import bad_request, forbidden
from app.db.models import Account, DailyAttempt, WeeklyAttempt
from app.db.session import get_db

router = APIRouter(prefix="/v1/learner", tags=["progress"])


class LearnerStatsOut(BaseModel):
    daily_done_today: bool
    weekly_done_this_week: bool
    daily_total: int
    weekly_total: int


@router.get("/stats")
async def get_learner_stats(
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
) -> LearnerStatsOut:
    if account.role != "learner":
        raise forbidden("Only learner accounts have stats")

    now = datetime.now(UTC)
    today = _date_key(now)
    this_week = _week_key(now)

    daily_today = (await db.execute(
        select(DailyAttempt).where(
            DailyAttempt.account_id == account.id,
            DailyAttempt.date_key == today,
            DailyAttempt.passed.is_(True),
        )
    )).scalar_one_or_none()

    weekly_this_week = (await db.execute(
        select(WeeklyAttempt).where(
            WeeklyAttempt.account_id == account.id,
            WeeklyAttempt.week_key == this_week,
            WeeklyAttempt.passed.is_(True),
        )
    )).scalar_one_or_none()

    daily_total = (await db.execute(
        select(func.count()).where(
            DailyAttempt.account_id == account.id,
            DailyAttempt.passed.is_(True),
        )
    )).scalar_one()

    weekly_total = (await db.execute(
        select(func.count()).where(
            WeeklyAttempt.account_id == account.id,
            WeeklyAttempt.passed.is_(True),
        )
    )).scalar_one()

    return LearnerStatsOut(
        daily_done_today=daily_today is not None,
        weekly_done_this_week=weekly_this_week is not None,
        daily_total=int(daily_total),
        weekly_total=int(weekly_total),
    )


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


@router.post("/reset-progress")
async def reset_progress(
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
    _csrf: None = Depends(require_csrf),
) -> LearnerProfileOut:
    """Reset the learner's progress to unit 1, lesson 1, no badges."""
    if account.role != "learner":
        raise forbidden("Only learner accounts can reset progress")
    if account.profile is None:
        await db.refresh(account, ["profile"])
    if account.profile is None:
        raise bad_request("Learner profile not found")

    account.profile.current_unit = 1
    account.profile.current_lesson = 1
    account.profile.badges_json = "[]"
    await db.commit()

    result = _profile_out(account)
    if result is None:
        raise bad_request("Profile unavailable after reset")
    return result
