from __future__ import annotations

import json
import uuid
from datetime import UTC, datetime, timedelta

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.errors import conflict, not_found
from app.db.models import Account, ParentLink, ProgressEvent
from app.parent.schemas import LearnerDetailOut, LearnerSummaryOut

_TOTAL_UNITS = 7
_LESSONS_PER_UNIT = 5


def _now() -> datetime:
    return datetime.now(UTC)


async def get_linked_learners(
    db: AsyncSession, parent_id: uuid.UUID
) -> list[LearnerSummaryOut]:
    links = list(
        await db.scalars(
            select(ParentLink).where(ParentLink.parent_account_id == parent_id)
        )
    )
    summaries: list[LearnerSummaryOut] = []
    for link in links:
        learner = await db.get(Account, link.learner_account_id)
        if learner is None:
            continue
        if learner.profile is None:
            await db.refresh(learner, ["profile"])
        profile = learner.profile
        if profile is None:
            continue
        try:
            badges: list[str] = json.loads(profile.badges_json)
        except Exception:
            badges = []
        summaries.append(
            LearnerSummaryOut(
                id=learner.id,
                display_name=learner.display_name,
                email=learner.email,
                track=profile.track,
                world=profile.world,
                current_unit=profile.current_unit,
                current_lesson=profile.current_lesson,
                badges=badges,
                total_units=_TOTAL_UNITS,
                total_lessons_per_unit=_LESSONS_PER_UNIT,
            )
        )
    return summaries


async def get_learner_detail(
    db: AsyncSession, parent_id: uuid.UUID, learner_id: uuid.UUID
) -> LearnerDetailOut:
    link = await db.scalar(
        select(ParentLink).where(
            ParentLink.parent_account_id == parent_id,
            ParentLink.learner_account_id == learner_id,
        )
    )
    if link is None:
        raise not_found("Learner not linked to this account")

    learner = await db.get(Account, learner_id)
    if learner is None:
        raise not_found("Learner not found")

    now = _now()
    today = now.date()

    # Fetch all events for this learner (small table per user, manageable indefinitely)
    all_events = list(
        await db.scalars(
            select(ProgressEvent)
            .where(ProgressEvent.account_id == learner_id)
            .order_by(ProgressEvent.created_at.desc())
        )
    )

    # Last active: most recent event's UTC date
    last_active: str | None = all_events[0].created_at.date().isoformat() if all_events else None

    # Streak: consecutive days going backwards from today with a session_start event
    session_dates = {
        e.created_at.date() for e in all_events if e.event_type == "session_start"
    }
    streak = 0
    check = today
    while check in session_dates:
        streak += 1
        check -= timedelta(days=1)

    # Lessons this week (last 7 days)
    seven_days_ago = now - timedelta(days=7)
    lessons_this_week = sum(
        1 for e in all_events
        if e.event_type == "lesson_complete" and e.created_at >= seven_days_ago
    )

    # 30-day sparkline: lesson_complete counts per day, oldest→newest
    sparkline: list[int] = []
    for i in range(30):
        day = (now - timedelta(days=29 - i)).date()
        count = sum(
            1 for e in all_events
            if e.event_type == "lesson_complete" and e.created_at.date() == day
        )
        sparkline.append(count)

    return LearnerDetailOut(
        id=learner_id,
        display_name=learner.display_name,
        email=learner.email,
        streak_days=streak,
        last_active=last_active,
        lessons_this_week=lessons_this_week,
        sparkline_30d=sparkline,
    )


async def link_learner(
    db: AsyncSession, parent_id: uuid.UUID, learner_email: str
) -> str:
    learner = await db.scalar(
        select(Account).where(
            Account.email == learner_email,
            Account.role == "learner",
        )
    )
    if learner is None:
        raise not_found("No learner account found with that email")

    existing = await db.scalar(
        select(ParentLink).where(
            ParentLink.parent_account_id == parent_id,
            ParentLink.learner_account_id == learner.id,
        )
    )
    if existing is not None:
        raise conflict("Learner is already linked to this account")

    now = _now()
    db.add(
        ParentLink(
            parent_account_id=parent_id,
            learner_account_id=learner.id,
            verified_at=now,
            created_at=now,
        )
    )
    await db.commit()
    return "linked"
