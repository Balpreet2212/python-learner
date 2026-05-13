"""SQLAlchemy models implementing §10.2 schema + session/email_token helpers."""

import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Account(Base):
    __tablename__ = "account"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(320), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(Text, nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False)  # 'learner' | 'parent'
    display_name: Mapped[str | None] = mapped_column(String(100))
    email_verified: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    # Learner inactive until parent verifies (under-13 flow §12.4)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    # Only populated for under-13 learners awaiting parent verification
    is_under_13: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    parent_invite_email: Mapped[str | None] = mapped_column(String(320))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    # relationships
    profile: Mapped["LearnerProfile | None"] = relationship(
        back_populates="account", uselist=False, cascade="all, delete-orphan", lazy="selectin"
    )
    subscription: Mapped["Subscription | None"] = relationship(
        back_populates="account", uselist=False, cascade="all, delete-orphan"
    )
    sessions: Mapped[list["Session"]] = relationship(
        back_populates="account", cascade="all, delete-orphan"
    )
    email_tokens: Mapped[list["EmailToken"]] = relationship(
        back_populates="account", cascade="all, delete-orphan"
    )
    # parent_link rows where this account is the parent
    linked_learners: Mapped[list["ParentLink"]] = relationship(
        back_populates="parent_account",
        foreign_keys="ParentLink.parent_account_id",
        cascade="all, delete-orphan",
    )
    # parent_link rows where this account is the learner
    linked_parents: Mapped[list["ParentLink"]] = relationship(
        back_populates="learner_account",
        foreign_keys="ParentLink.learner_account_id",
        cascade="all, delete-orphan",
    )


class LearnerProfile(Base):
    """Learner-specific fields (§10.2). Only accounts with role='learner' have one."""

    __tablename__ = "learner_profile"

    account_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("account.id", ondelete="RESTRICT"), primary_key=True
    )
    track: Mapped[str] = mapped_column(String(20), nullable=False)  # 'junior' | 'core'
    world: Mapped[str] = mapped_column(String(20), nullable=False)  # 'fantasy'|'scifi'|'mystery'
    current_unit: Mapped[int] = mapped_column(nullable=False, default=1)
    current_lesson: Mapped[int] = mapped_column(nullable=False, default=1)
    # Stored as JSON string; deserialized in the service layer
    badges_json: Mapped[str] = mapped_column(Text, nullable=False, default="[]")
    public_profile: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    account: Mapped["Account"] = relationship(back_populates="profile")


class ParentLink(Base):
    """Links a parent account to a learner account (§10.2). RESTRICT on delete."""

    __tablename__ = "parent_link"

    parent_account_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("account.id", ondelete="RESTRICT"), primary_key=True
    )
    learner_account_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("account.id", ondelete="RESTRICT"), primary_key=True
    )
    verified_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    parent_account: Mapped["Account"] = relationship(
        back_populates="linked_learners", foreign_keys=[parent_account_id]
    )
    learner_account: Mapped["Account"] = relationship(
        back_populates="linked_parents", foreign_keys=[learner_account_id]
    )


class Subscription(Base):
    """Billing state (§10.2). Synced from Stripe webhooks."""

    __tablename__ = "subscription"

    account_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("account.id", ondelete="RESTRICT"), primary_key=True
    )
    status: Mapped[str] = mapped_column(
        String(20), nullable=False, default="trial"
    )  # 'trial' | 'active' | 'past_due' | 'cancelled'
    trial_ends_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    current_period_end: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    provider_customer_id: Mapped[str | None] = mapped_column(String(200))
    provider_subscription_id: Mapped[str | None] = mapped_column(String(200))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    account: Mapped["Account"] = relationship(back_populates="subscription")


class Session(Base):
    """Server-side session store. Cookie holds the signed session id."""

    __tablename__ = "session"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)  # random hex token
    account_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("account.id", ondelete="CASCADE"), nullable=False
    )
    csrf_token: Mapped[str] = mapped_column(String(64), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    account: Mapped["Account"] = relationship(back_populates="sessions")


class EmailToken(Base):
    """One-time tokens for email verification, parent invites, password resets."""

    __tablename__ = "email_token"

    token: Mapped[str] = mapped_column(String(64), primary_key=True)
    account_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("account.id", ondelete="CASCADE"), nullable=False
    )
    purpose: Mapped[str] = mapped_column(
        String(30), nullable=False
    )  # 'email_verify' | 'parent_invite' | 'password_reset'
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    used_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    account: Mapped["Account"] = relationship(back_populates="email_tokens")
