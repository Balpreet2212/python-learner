"""Dev seed — run via `make seed` or `python -m app.db.seed`."""

import asyncio
import uuid
from datetime import UTC, datetime, timedelta

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import hash_password
from app.db.models import Account, LearnerProfile, Subscription
from app.db.session import async_session_factory


async def seed(session: AsyncSession) -> None:
    now = datetime.now(UTC)

    learner = Account(
        id=uuid.uuid4(),
        email="learner@pyquest.local",
        password_hash=hash_password("password123"),
        role="learner",
        display_name="Demo Learner",
        email_verified=True,
        is_active=True,
        created_at=now,
        updated_at=now,
    )
    session.add(learner)
    await session.flush()

    session.add(
        LearnerProfile(
            account_id=learner.id,
            track="core",
            world="scifi",
        )
    )
    session.add(
        Subscription(
            account_id=learner.id,
            status="trial",
            trial_ends_at=now + timedelta(days=14),
            updated_at=now,
        )
    )

    parent = Account(
        id=uuid.uuid4(),
        email="parent@pyquest.local",
        password_hash=hash_password("password123"),
        role="parent",
        display_name="Demo Parent",
        email_verified=True,
        is_active=True,
        created_at=now,
        updated_at=now,
    )
    session.add(parent)

    await session.commit()
    print("Seeded: learner@pyquest.local / parent@pyquest.local (password: password123)")


if __name__ == "__main__":
    async def main() -> None:
        async with async_session_factory() as session:
            await seed(session)

    asyncio.run(main())
