from __future__ import annotations

from fastapi import Header, HTTPException, status

from src.core.config import better_auth_secret
from jose import jwt
from jose.exceptions import JWTError
from typing import Optional
from uuid import UUID


def unauthorized(detail: str = "Unauthorized"):
    """Raise an unauthorized HTTP exception."""
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail
    )


def extract_user_id(claims: dict) -> Optional[str]:
    """Extract user ID from JWT claims."""
    return claims.get("user_id")


def verify_jwt(token: str, secret: str) -> dict:
    """Verify JWT token and return claims."""
    try:
        claims = jwt.decode(token, secret, algorithms=["HS256"])
        return claims
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )


def get_current_user_id(authorization: str | None = Header(default=None)) -> str:
    if authorization is None or authorization.strip() == "":
        raise unauthorized()

    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or token.strip() == "":
        raise unauthorized()

    try:
        claims = verify_jwt(token=token, secret=better_auth_secret())
    except Exception:
        # Intentionally avoid leaking auth failure details.
        raise unauthorized()

    user_id = extract_user_id(claims)
    if user_id is None:
        raise unauthorized("Token missing user identity.")

    return user_id
