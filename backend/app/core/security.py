"""Password hashing and token generation."""

import secrets

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

_ph = PasswordHasher()


def hash_password(plain: str) -> str:
    return _ph.hash(plain)


def verify_password(plain: str, hashed: str) -> bool:
    try:
        return _ph.verify(hashed, plain)
    except VerifyMismatchError:
        return False


def generate_token(nbytes: int = 32) -> str:
    """Return a URL-safe hex token."""
    return secrets.token_hex(nbytes)
