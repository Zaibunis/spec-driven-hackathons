"""
Database connection and session management.

Provides async SQLModel engine and session factory for Neon PostgreSQL.
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlmodel import Session, select

from .config import Config


# Async engine for Neon Serverless PostgreSQL
# DATABASE_URL may be postgresql:// (sync psycopg2) or postgresql+asyncpg://.
# The async engine requires the asyncpg driver, so normalize the scheme here.
# asyncpg also rejects psycopg2-style query params (sslmode), so strip them and
# pass TLS via connect_args instead.
from urllib.parse import urlsplit, urlunsplit

_DB_URL = Config.DATABASE_URL
if _DB_URL.startswith("postgresql+asyncpg://"):
    _ASYNC_DB_URL = _DB_URL
elif _DB_URL.startswith("postgresql://") or _DB_URL.startswith("postgres://"):
    _ASYNC_DB_URL = _DB_URL.replace("postgresql://", "postgresql+asyncpg://", 1).replace(
        "postgres://", "postgresql+asyncpg://", 1
    )
else:
    _ASYNC_DB_URL = _DB_URL

# Strip query string (sslmode etc.) - TLS is enforced via connect_args below.
_parts = urlsplit(_ASYNC_DB_URL)
_ASYNC_DB_URL = urlunsplit((_parts.scheme, _parts.netloc, _parts.path, "", ""))

async_engine = create_async_engine(
    _ASYNC_DB_URL,
    echo=False,
    future=True,
    pool_size=5,
    max_overflow=10,
    # asyncpg does not accept sslmode in the URL; pass TLS via connect_args.
    connect_args={"ssl": True},
)


async def get_session() -> AsyncSession:
    """Get async database session."""
    async with AsyncSession(async_engine) as session:
        yield session


async def init_db() -> None:
    """Initialize database tables."""
    from .models import Task  # noqa: F401
    from sqlmodel import SQLModel

    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)