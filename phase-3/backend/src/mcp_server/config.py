"""
Configuration management for MCP Server & Todo Tooling.

Loads environment variables and provides database connection configuration.
"""

import os

from dotenv import load_dotenv

# Load backend/.env so MCP tools work regardless of how uvicorn was started
# (with or without --env-file). Real env vars still take precedence.
load_dotenv()


class Config:
    """Database and server configuration.

    Secrets are required from the environment - no hardcoded defaults.
    Values are resolved lazily (at property access) so importing this module
    does not fail when env vars are unset; accessing a missing required var
    raises immediately with a clear message.
    """

    @property
    def DATABASE_URL(self) -> str:
        """Database connection string. Required."""
        value = os.environ.get("DATABASE_URL")
        if not value:
            raise RuntimeError(
                "DATABASE_URL is not set. Configure it via environment (no defaults allowed)."
            )
        return value

    @property
    def JWT_SECRET(self) -> str:
        """JWT signing secret. Required."""
        value = os.environ.get("JWT_SECRET")
        if not value:
            raise RuntimeError(
                "JWT_SECRET is not set. Configure it via environment (no defaults allowed)."
            )
        return value

    JWT_ALGORITHM: str = "HS256"

    # MCP Server
    MCP_SERVER_NAME: str = os.getenv("MCP_SERVER_NAME", "todo-mcp-server")
    MCP_LOG_LEVEL: str = os.getenv("MCP_LOG_LEVEL", "INFO")

    @classmethod
    def validate(cls) -> None:
        """Validate required configuration."""
        if not cls.DATABASE_URL or cls.DATABASE_URL.startswith("postgresql://"):
            raise ValueError("DATABASE_URL must be set and use asyncpg driver")


# Module-level instance so `Config.DATABASE_URL` property access works everywhere
# (e.g. `from .config import Config; Config.JWT_SECRET`).
Config = Config()
