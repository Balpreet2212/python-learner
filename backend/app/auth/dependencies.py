"""FastAPI dependencies for session and CSRF validation."""

from fastapi import Cookie, Depends, Header, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.service import get_session
from app.core.errors import forbidden, unauthorized
from app.db.models import Account, Session
from app.db.session import get_db

SESSION_COOKIE = "pyquest_session"


async def get_current_session(
    request: Request,
    db: AsyncSession = Depends(get_db),
    pyquest_session: str | None = Cookie(default=None),
) -> Session:
    if not pyquest_session:
        raise unauthorized()
    return await get_session(db, pyquest_session)


async def get_current_account(
    session: Session = Depends(get_current_session),
    db: AsyncSession = Depends(get_db),
) -> Account:
    account = await db.get(Account, session.account_id)
    if account is None:
        raise unauthorized()
    if not account.is_active:
        raise forbidden("Account is inactive")
    return account


async def require_csrf(
    request: Request,
    session: Session = Depends(get_current_session),
    x_csrf_token: str | None = Header(default=None, alias="X-CSRF-Token"),
) -> None:
    """Validate CSRF token on all state-mutating requests (§11.1)."""
    if x_csrf_token is None or x_csrf_token != session.csrf_token:
        raise forbidden("Invalid or missing CSRF token")
