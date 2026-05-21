"""Add progress_event table for parent dashboard activity tracking

Revision ID: 0002
Revises: 0001
Create Date: 2026-05-21
"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "0002"
down_revision: str | None = "0001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "progress_event",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("account_id", sa.Uuid(), nullable=False),
        sa.Column("event_type", sa.String(30), nullable=False),
        sa.Column("unit", sa.Integer(), nullable=True),
        sa.Column("lesson", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["account_id"], ["account.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_progress_event_account_id", "progress_event", ["account_id"])
    op.create_index("ix_progress_event_created_at", "progress_event", ["created_at"])


def downgrade() -> None:
    op.drop_index("ix_progress_event_created_at", "progress_event")
    op.drop_index("ix_progress_event_account_id", "progress_event")
    op.drop_table("progress_event")
