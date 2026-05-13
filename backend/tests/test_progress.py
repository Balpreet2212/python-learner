"""Integration tests for learner progress / onboarding endpoint (M3)."""

import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Account, EmailToken


_counter = 0


async def _create_and_login(client: AsyncClient, db_session: AsyncSession) -> str:
    """Helper: signup + verify email + login. Returns CSRF token."""
    global _counter
    _counter += 1
    email = f"prog{_counter}@example.com"
    await client.post(
        "/v1/auth/signup",
        json={"email": email, "password": "securepass1", "role": "learner"},
    )
    token_row = await db_session.scalar(
        select(EmailToken).where(EmailToken.purpose == "email_verify")
    )
    assert token_row is not None
    await client.post("/v1/auth/verify-email", json={"token": token_row.token})
    login = await client.post(
        "/v1/auth/login", json={"email": email, "password": "securepass1"}
    )
    return str(login.json()["csrf_token"])


@pytest.mark.asyncio
async def test_onboarding_sets_track_and_world(
    client: AsyncClient, db_session: AsyncSession
) -> None:
    csrf = await _create_and_login(client, db_session)
    resp = await client.post(
        "/v1/learner/onboarding",
        json={"track": "junior", "world": "fantasy"},
        headers={"X-CSRF-Token": csrf},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["track"] == "junior"
    assert data["world"] == "fantasy"
    assert "current_unit" in data
    assert "badges" in data


@pytest.mark.asyncio
async def test_onboarding_is_idempotent(
    client: AsyncClient, db_session: AsyncSession
) -> None:
    csrf = await _create_and_login(client, db_session)
    headers = {"X-CSRF-Token": csrf}
    await client.post(
        "/v1/learner/onboarding",
        json={"track": "junior", "world": "fantasy"},
        headers=headers,
    )
    resp = await client.post(
        "/v1/learner/onboarding",
        json={"track": "core", "world": "scifi"},
        headers=headers,
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["track"] == "core"
    assert data["world"] == "scifi"


@pytest.mark.asyncio
async def test_onboarding_rejects_invalid_world(
    client: AsyncClient, db_session: AsyncSession
) -> None:
    csrf = await _create_and_login(client, db_session)
    resp = await client.post(
        "/v1/learner/onboarding",
        json={"track": "junior", "world": "underwater"},
        headers={"X-CSRF-Token": csrf},
    )
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_onboarding_rejects_missing_csrf(
    client: AsyncClient, db_session: AsyncSession
) -> None:
    csrf = await _create_and_login(client, db_session)
    _ = csrf  # obtained but intentionally not sent
    resp = await client.post(
        "/v1/learner/onboarding",
        json={"track": "junior", "world": "fantasy"},
    )
    assert resp.status_code == 403


@pytest.mark.asyncio
async def test_me_returns_profile_after_onboarding(
    client: AsyncClient, db_session: AsyncSession
) -> None:
    csrf = await _create_and_login(client, db_session)
    await client.post(
        "/v1/learner/onboarding",
        json={"track": "core", "world": "mystery"},
        headers={"X-CSRF-Token": csrf},
    )
    me = await client.get("/v1/me")
    assert me.status_code == 200
    profile = me.json().get("profile")
    assert profile is not None
    assert profile["track"] == "core"
    assert profile["world"] == "mystery"
