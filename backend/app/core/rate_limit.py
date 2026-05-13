"""Simple in-memory sliding-window rate limiter (per §11.4).

Single-process only. For multi-process deployments, replace storage with Redis.
This is documented in docs/decisions/0001-stack.md.
"""

import time
from collections import defaultdict, deque
from typing import Any

from fastapi import Request

from app.core.errors import rate_limited

# { key -> deque of timestamps (seconds) }
_windows: dict[str, deque[float]] = defaultdict(deque)


def _check(key: str, limit: int, window_seconds: int) -> None:
    """Raise 429 if `limit` requests have been made within `window_seconds`."""
    now = time.monotonic()
    cutoff = now - window_seconds
    dq = _windows[key]

    # Drop timestamps outside the window
    while dq and dq[0] < cutoff:
        dq.popleft()

    if len(dq) >= limit:
        raise rate_limited()

    dq.append(now)


def _client_ip(request: Request) -> str:
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


def limit_auth(request: Request) -> Any:
    """10 requests / minute / IP for auth endpoints."""
    key = f"auth:{_client_ip(request)}"
    _check(key, limit=10, window_seconds=60)


def limit_challenge_submit(request: Request) -> Any:
    """30 requests / hour / IP for challenge submission."""
    key = f"challenge:{_client_ip(request)}"
    _check(key, limit=30, window_seconds=3600)


def limit_default(request: Request) -> Any:
    """60 requests / minute / IP default."""
    key = f"default:{_client_ip(request)}"
    _check(key, limit=60, window_seconds=60)
