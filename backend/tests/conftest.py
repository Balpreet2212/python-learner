"""Shared test fixtures."""

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core import rate_limit as _rl_module
from app.db.base import Base
from app.db.session import get_db
from app.main import app

TEST_DB_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture(autouse=True)
def reset_rate_limiter() -> None:
    """Clear the in-memory rate limiter between tests so limits don't bleed across."""
    _rl_module._windows.clear()


@pytest_asyncio.fixture()
async def db_session() -> AsyncSession:  # type: ignore[misc]
    engine = create_async_engine(TEST_DB_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
        engine, expire_on_commit=False
    )
    async with factory() as session:
        yield session  # type: ignore[misc]

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest_asyncio.fixture()
async def client(db_session: AsyncSession) -> AsyncClient:  # type: ignore[misc]
    """HTTP client wired to the in-memory test DB."""

    async def override_get_db() -> AsyncSession:  # type: ignore[misc]
        yield db_session  # type: ignore[misc]

    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c  # type: ignore[misc]
    app.dependency_overrides.clear()
