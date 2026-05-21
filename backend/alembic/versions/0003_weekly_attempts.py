"""Add weekly_attempt table for weekly challenge tracking

Revision ID: 0003
Revises: 0002
Create Date: 2026-05-21
"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "0003"
down_revision: str | None = "0002"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "weekly_attempt",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("account_id", sa.Uuid(), nullable=False),
        sa.Column("challenge_index", sa.Integer(), nullable=False),
        sa.Column("week_key", sa.String(10), nullable=False),
        sa.Column("passed", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["account_id"], ["account.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_weekly_attempt_account_id", "weekly_attempt", ["account_id"])
    op.create_index(
        "ix_weekly_attempt_account_week",
        "weekly_attempt",
        ["account_id", "week_key"],
    )


def downgrade() -> None:
    op.drop_index("ix_weekly_attempt_account_week", "weekly_attempt")
    op.drop_index("ix_weekly_attempt_account_id", "weekly_attempt")
    op.drop_table("weekly_attempt")
