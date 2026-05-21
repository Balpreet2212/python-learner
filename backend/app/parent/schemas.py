from __future__ import annotations

import uuid

from pydantic import BaseModel, EmailStr


class LearnerSummaryOut(BaseModel):
    id: uuid.UUID
    display_name: str | None
    email: str
    track: str
    world: str
    current_unit: int
    current_lesson: int
    badges: list[str]
    total_units: int
    total_lessons_per_unit: int


class LearnerDetailOut(BaseModel):
    id: uuid.UUID
    display_name: str | None
    email: str
    streak_days: int
    last_active: str | None  # ISO date, e.g. "2026-05-21"
    lessons_this_week: int
    sparkline_30d: list[int]  # 30 values oldest→newest, counting lesson_complete events


class LinkLearnerRequest(BaseModel):
    email: EmailStr


class LinkOut(BaseModel):
    status: str  # "linked" | "already_linked"
