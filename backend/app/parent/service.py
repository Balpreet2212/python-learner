from __future__ import annotations

import json
import uuid
from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.errors import conflict, not_found
from app.db.models import Account, ParentLink
from app.parent.schemas import LearnerSummaryOut

_TOTAL_UNITS = 6
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
