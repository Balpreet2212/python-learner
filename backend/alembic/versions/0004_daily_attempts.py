"""Add daily_attempt table for daily challenge tracking

Revision ID: 0004
Revises: 0003
Create Date: 2026-05-28
"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "0004"
down_revision: str | None = "0003"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "daily_attempt",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("account_id", sa.Uuid(), nullable=False),
        sa.Column("challenge_index", sa.Integer(), nullable=False),
        sa.Column("date_key", sa.String(10), nullable=False),
        sa.Column("passed", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["account_id"], ["account.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_daily_attempt_account_id", "daily_attempt", ["account_id"])
    op.create_index(
        "ix_daily_attempt_account_date",
        "daily_attempt",
        ["account_id", "date_key"],
    )


def downgrade() -> None:
    op.drop_index("ix_daily_attempt_account_date", "daily_attempt")
    op.drop_index("ix_daily_attempt_account_id", "daily_attempt")
    op.drop_table("daily_attempt")
