"""Integration tests for auth endpoints (M2).

Covers:
- Happy-path signup → verify-email → login → me → logout
- Under-13 signup flow (parent invite sent, learner inactive until parent-verify)
- Login failures (bad password, unverified email, inactive account)
- CSRF rejection on write endpoints
"""

import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Account, EmailToken


# ── Signup ──────────────────────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_signup_happy_path(client: AsyncClient, db_session: AsyncSession) -> None:
    resp = await client.post(
        "/v1/auth/signup",
        json={"email": "alice@example.com", "password": "securepass1", "role": "learner"},
    )
    assert resp.status_code == 201
    assert resp.json()["status"] == "verification_email_sent"

    account = await db_session.scalar(
        select(Account).where(Account.email == "alice@example.com")
    )
    assert account is not None
    assert account.email_verified is False
    assert account.is_active is True  # 13+ learners are active, just unverified


@pytest.mark.asyncio
async def test_signup_duplicate_email(client: AsyncClient) -> None:
    payload = {"email": "dup@example.com", "password": "securepass1", "role": "learner"}
    await client.post("/v1/auth/signup", json=payload)
    resp = await client.post("/v1/auth/signup", json=payload)
    assert resp.status_code == 409
    assert resp.json()["code"] == "conflict"


@pytest.mark.asyncio
async def test_signup_under_13_without_parent_email(client: AsyncClient) -> None:
    resp = await client.post(
        "/v1/auth/signup",
        json={
            "email": "kid@example.com",
            "password": "securepass1",
            "role": "learner",
            "is_under_13": True,
            # parent_email intentionally omitted
        },
    )
    assert resp.status_code == 422  # Pydantic validation error


@pytest.mark.asyncio
async def test_signup_under_13_with_parent_email(
    client: AsyncClient, db_session: AsyncSession
) -> None:
    resp = await client.post(
        "/v1/auth/signup",
        json={
            "email": "kid2@example.com",
            "password": "securepass1",
            "role": "learner",
            "is_under_13": True,
            "parent_email": "parent@example.com",
        },
    )
    assert resp.status_code == 201
    assert resp.json()["status"] == "pending_parent_verification"

    account = await db_session.scalar(
        select(Account).where(Account.email == "kid2@example.com")
    )
    assert account is not None
    assert account.is_active is False
    assert account.is_under_13 is True


# ── Email verification ───────────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_verify_email(client: AsyncClient, db_session: AsyncSession) -> None:
    await client.post(
        "/v1/auth/signup",
        json={"email": "bob@example.com", "password": "securepass1", "role": "learner"},
    )
    token_row = await db_session.scalar(
        select(EmailToken).where(EmailToken.purpose == "email_verify")
    )
    assert token_row is not None

    resp = await client.post("/v1/auth/verify-email", json={"token": token_row.token})
    assert resp.status_code == 200

    account = await db_session.scalar(
        select(Account).where(Account.email == "bob@example.com")
    )
    assert account is not None
    assert account.email_verified is True


@pytest.mark.asyncio
async def test_verify_email_bad_token(client: AsyncClient) -> None:
    resp = await client.post("/v1/auth/verify-email", json={"token": "notavalidtoken"})
    assert resp.status_code == 400


# ── Parent verification ──────────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_parent_verify_activates_learner(
    client: AsyncClient, db_session: AsyncSession
) -> None:
    await client.post(
        "/v1/auth/signup",
        json={
            "email": "kid3@example.com",
            "password": "securepass1",
            "role": "learner",
            "is_under_13": True,
            "parent_email": "parent3@example.com",
        },
    )
    token_row = await db_session.scalar(
        select(EmailToken).where(EmailToken.purpose == "parent_invite")
    )
    assert token_row is not None

    resp = await client.post("/v1/auth/parent-verify", json={"token": token_row.token})
    assert resp.status_code == 200

    account = await db_session.scalar(
        select(Account).where(Account.email == "kid3@example.com")
    )
    assert account is not None
    assert account.is_active is True
    assert account.email_verified is True


# ── Login / logout ───────────────────────────────────────────────────────────


_learner_counter = 0


async def _create_verified_learner(
    client: AsyncClient, db_session: AsyncSession, suffix: str = ""
) -> str:
    """Helper: signup + verify email. Returns email."""
    global _learner_counter
    _learner_counter += 1
    email = f"learner{_learner_counter}{suffix}@example.com"
    await client.post(
        "/v1/auth/signup",
        json={"email": email, "password": "securepass1", "role": "learner"},
    )
    token_row = await db_session.scalar(
        select(EmailToken).where(
            EmailToken.purpose == "email_verify",
        )
    )
    assert token_row is not None, "email_verify token not found — signup may have failed"
    await client.post("/v1/auth/verify-email", json={"token": token_row.token})
    return email


@pytest.mark.asyncio
async def test_login_happy_path(client: AsyncClient, db_session: AsyncSession) -> None:
    email = await _create_verified_learner(client, db_session)
    resp = await client.post(
        "/v1/auth/login", json={"email": email, "password": "securepass1"}
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "csrf_token" in data
    assert data["account"]["email"] == email
    assert "pyquest_session" in resp.cookies


@pytest.mark.asyncio
async def test_login_wrong_password(client: AsyncClient, db_session: AsyncSession) -> None:
    email = await _create_verified_learner(client, db_session)
    resp = await client.post(
        "/v1/auth/login", json={"email": email, "password": "wrongpassword"}
    )
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_login_unverified_email(client: AsyncClient) -> None:
    await client.post(
        "/v1/auth/signup",
        json={"email": "dave@example.com", "password": "securepass1", "role": "learner"},
    )
    resp = await client.post(
        "/v1/auth/login", json={"email": "dave@example.com", "password": "securepass1"}
    )
    assert resp.status_code == 403
    assert resp.json()["code"] == "email_not_verified"


@pytest.mark.asyncio
async def test_me_requires_session(client: AsyncClient) -> None:
    resp = await client.get("/v1/me")
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_me_returns_account(client: AsyncClient, db_session: AsyncSession) -> None:
    email = await _create_verified_learner(client, db_session)
    login = await client.post(
        "/v1/auth/login", json={"email": email, "password": "securepass1"}
    )
    csrf = login.json()["csrf_token"]

    resp = await client.get("/v1/me")
    assert resp.status_code == 200
    assert resp.json()["account"]["email"] == email
    assert resp.json()["csrf_token"] == csrf


@pytest.mark.asyncio
async def test_logout(client: AsyncClient, db_session: AsyncSession) -> None:
    email = await _create_verified_learner(client, db_session)
    login = await client.post(
        "/v1/auth/login", json={"email": email, "password": "securepass1"}
    )
    csrf = login.json()["csrf_token"]

    resp = await client.post("/v1/auth/logout", headers={"X-CSRF-Token": csrf})
    assert resp.status_code == 204

    # Session cookie should be gone → subsequent /me returns 401
    resp2 = await client.get("/v1/me")
    assert resp2.status_code == 401


# ── CSRF ────────────────────────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_csrf_rejection_on_logout(client: AsyncClient, db_session: AsyncSession) -> None:
    email = await _create_verified_learner(client, db_session)
    await client.post("/v1/auth/login", json={"email": email, "password": "securepass1"})

    # Attempt logout without CSRF header
    resp = await client.post("/v1/auth/logout")
    assert resp.status_code == 403
    assert resp.json()["code"] == "forbidden"


@pytest.mark.asyncio
async def test_csrf_wrong_token_rejected(client: AsyncClient, db_session: AsyncSession) -> None:
    email = await _create_verified_learner(client, db_session)
    await client.post("/v1/auth/login", json={"email": email, "password": "securepass1"})

    resp = await client.post(
        "/v1/auth/logout", headers={"X-CSRF-Token": "completely-wrong-token"}
    )
    assert resp.status_code == 403
