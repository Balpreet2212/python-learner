"""Initial schema — account, learner_profile, parent_link, subscription, session, email_token

Revision ID: 0001
Revises:
Create Date: 2026-05-13
"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "0001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "account",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("email", sa.String(320), nullable=False),
        sa.Column("password_hash", sa.Text(), nullable=False),
        sa.Column("role", sa.String(20), nullable=False),
        sa.Column("display_name", sa.String(100), nullable=True),
        sa.Column("email_verified", sa.Boolean(), nullable=False, server_default="0"),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default="1"),
        sa.Column("is_under_13", sa.Boolean(), nullable=False, server_default="0"),
        sa.Column("parent_invite_email", sa.String(320), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )

    op.create_table(
        "learner_profile",
        sa.Column("account_id", sa.Uuid(), nullable=False),
        sa.Column("track", sa.String(20), nullable=False),
        sa.Column("world", sa.String(20), nullable=False),
        sa.Column("current_unit", sa.Integer(), nullable=False, server_default="1"),
        sa.Column("current_lesson", sa.Integer(), nullable=False, server_default="1"),
        sa.Column("badges_json", sa.Text(), nullable=False, server_default="[]"),
        sa.Column("public_profile", sa.Boolean(), nullable=False, server_default="0"),
        sa.ForeignKeyConstraint(["account_id"], ["account.id"], ondelete="RESTRICT"),
        sa.PrimaryKeyConstraint("account_id"),
    )

    op.create_table(
        "parent_link",
        sa.Column("parent_account_id", sa.Uuid(), nullable=False),
        sa.Column("learner_account_id", sa.Uuid(), nullable=False),
        sa.Column("verified_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["parent_account_id"], ["account.id"], ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["learner_account_id"], ["account.id"], ondelete="RESTRICT"),
        sa.PrimaryKeyConstraint("parent_account_id", "learner_account_id"),
    )

    op.create_table(
        "subscription",
        sa.Column("account_id", sa.Uuid(), nullable=False),
        sa.Column("status", sa.String(20), nullable=False, server_default="trial"),
        sa.Column("trial_ends_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("current_period_end", sa.DateTime(timezone=True), nullable=True),
        sa.Column("provider_customer_id", sa.String(200), nullable=True),
        sa.Column("provider_subscription_id", sa.String(200), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["account_id"], ["account.id"], ondelete="RESTRICT"),
        sa.PrimaryKeyConstraint("account_id"),
    )

    op.create_table(
        "session",
        sa.Column("id", sa.String(64), nullable=False),
        sa.Column("account_id", sa.Uuid(), nullable=False),
        sa.Column("csrf_token", sa.String(64), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["account_id"], ["account.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_session_account_id", "session", ["account_id"])
    op.create_index("ix_session_expires_at", "session", ["expires_at"])

    op.create_table(
        "email_token",
        sa.Column("token", sa.String(64), nullable=False),
        sa.Column("account_id", sa.Uuid(), nullable=False),
        sa.Column("purpose", sa.String(30), nullable=False),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("used_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["account_id"], ["account.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("token"),
    )
    op.create_index("ix_email_token_account_id", "email_token", ["account_id"])


def downgrade() -> None:
    op.drop_table("email_token")
    op.drop_table("session")
    op.drop_table("subscription")
    op.drop_table("parent_link")
    op.drop_table("learner_profile")
    op.drop_table("account")
