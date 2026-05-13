"""Pydantic schemas for auth endpoints."""

import uuid
from typing import Literal, Self

from pydantic import BaseModel, EmailStr, Field, model_validator


class SignupRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    role: Literal["learner", "parent"]
    display_name: str | None = Field(default=None, max_length=100)
    is_under_13: bool = False
    # Required when is_under_13=True and role='learner'
    parent_email: EmailStr | None = None

    @model_validator(mode="after")
    def parent_email_required_for_under_13(self) -> Self:
        if self.is_under_13 and self.role == "learner" and self.parent_email is None:
            raise ValueError("parent_email is required for learners under 13")
        return self


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class VerifyEmailRequest(BaseModel):
    token: str


class ParentVerifyRequest(BaseModel):
    token: str
    # Parent can optionally set up their account at this step
    parent_display_name: str | None = Field(default=None, max_length=100)
    parent_password: str | None = Field(default=None, min_length=8, max_length=128)


class AccountOut(BaseModel):
    id: uuid.UUID
    email: str
    role: str
    display_name: str | None
    email_verified: bool
    is_active: bool
    is_under_13: bool


class LoginResponse(BaseModel):
    account: AccountOut
    csrf_token: str


class LearnerProfileOut(BaseModel):
    track: str
    world: str
    current_unit: int
    current_lesson: int
    badges: list[str]
    public_profile: bool


class MeResponse(BaseModel):
    account: AccountOut
    csrf_token: str
    profile: LearnerProfileOut | None = None  # None for parent accounts
