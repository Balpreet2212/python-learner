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


class LinkLearnerRequest(BaseModel):
    email: EmailStr


class LinkOut(BaseModel):
    status: str  # "linked" | "already_linked"
