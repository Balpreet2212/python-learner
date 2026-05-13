"""Integration tests for lesson content and challenge submission (M4)."""

import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import EmailToken


_counter = 0


async def _login(client: AsyncClient, db_session: AsyncSession) -> str:
    """Signup + verify + login. Returns CSRF token."""
    global _counter
    _counter += 1
    email = f"content{_counter}@example.com"
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
    csrf = str(login.json()["csrf_token"])
    # Complete onboarding so lesson endpoints work
    await client.post(
        "/v1/learner/onboarding",
        json={"track": "junior", "world": "fantasy"},
        headers={"X-CSRF-Token": csrf},
    )
    return csrf


@pytest.mark.asyncio
async def test_get_lesson_returns_content(client: AsyncClient, db_session: AsyncSession) -> None:
    await _login(client, db_session)
    resp = await client.get("/v1/learner/lesson")
    assert resp.status_code == 200
    data = resp.json()
    assert data["unit"] == 1
    assert data["lesson"] == 1
    assert data["title"] != ""
    assert data["narrative"] != ""
    assert "code_starter" in data
    assert isinstance(data["hints"], list)
    assert data["test_count"] > 0


@pytest.mark.asyncio
async def test_get_lesson_requires_auth(client: AsyncClient) -> None:
    resp = await client.get("/v1/learner/lesson")
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_submit_passing_code(client: AsyncClient, db_session: AsyncSession) -> None:
    csrf = await _login(client, db_session)
    # Lesson 1: assign a non-empty string to 'name'
    resp = await client.post(
        "/v1/learner/challenge/submit",
        json={"code": 'name = "Merlin"'},
        headers={"X-CSRF-Token": csrf},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["all_passed"] is True
    assert data["exec_error"] is None
    assert all(t["passed"] for t in data["tests"])


@pytest.mark.asyncio
async def test_submit_failing_code(client: AsyncClient, db_session: AsyncSession) -> None:
    csrf = await _login(client, db_session)
    # Wrong type: number instead of string
    resp = await client.post(
        "/v1/learner/challenge/submit",
        json={"code": "name = 42"},
        headers={"X-CSRF-Token": csrf},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["all_passed"] is False
    assert any(not t["passed"] for t in data["tests"])


@pytest.mark.asyncio
async def test_submit_syntax_error(client: AsyncClient, db_session: AsyncSession) -> None:
    csrf = await _login(client, db_session)
    resp = await client.post(
        "/v1/learner/challenge/submit",
        json={"code": "name = "},
        headers={"X-CSRF-Token": csrf},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["all_passed"] is False
    assert data["exec_error"] is not None


@pytest.mark.asyncio
async def test_submit_requires_csrf(client: AsyncClient, db_session: AsyncSession) -> None:
    await _login(client, db_session)
    resp = await client.post(
        "/v1/learner/challenge/submit",
        json={"code": 'name = "test"'},
    )
    assert resp.status_code == 403


@pytest.mark.asyncio
async def test_advance_lesson(client: AsyncClient, db_session: AsyncSession) -> None:
    csrf = await _login(client, db_session)
    # Submit passing code first
    await client.post(
        "/v1/learner/challenge/submit",
        json={"code": 'name = "Merlin"'},
        headers={"X-CSRF-Token": csrf},
    )
    # Advance
    resp = await client.post(
        "/v1/learner/lesson/advance",
        headers={"X-CSRF-Token": csrf},
    )
    assert resp.status_code == 200
    profile = resp.json()
    assert profile["current_lesson"] == 2


@pytest.mark.asyncio
async def test_advance_unit_awards_badge(client: AsyncClient, db_session: AsyncSession) -> None:
    csrf = await _login(client, db_session)
    headers = {"X-CSRF-Token": csrf}
    # Advance through all 5 lessons
    for _ in range(5):
        await client.post(
            "/v1/learner/challenge/submit",
            json={"code": 'name = "Ada"'},
            headers=headers,
        )
        await client.post("/v1/learner/lesson/advance", headers=headers)

    me = await client.get("/v1/me")
    profile = me.json()["profile"]
    assert profile["current_unit"] == 2
    assert profile["current_lesson"] == 1
    assert "unit_1_complete" in profile["badges"]
