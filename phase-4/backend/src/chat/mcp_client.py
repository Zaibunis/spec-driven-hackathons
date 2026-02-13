from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any, Optional

from src.config import settings

logger = logging.getLogger(__name__)

# --------------------------------------------------
# MCP RESULT MODEL
# --------------------------------------------------

@dataclass(frozen=True)
class MCPToolResult:
    success: bool
    data: Optional[dict[str, Any]] = None
    error: Optional[dict[str, Any]] = None

# --------------------------------------------------
# MCP CLIENT
# --------------------------------------------------

class MCPClient:
    """
    Client for calling MCP todo tools.
    This implementation directly calls MCP server handlers.
    """

    def __init__(self, server_url: Optional[str] = None):
        self._server_url = server_url or settings.MCP_SERVER_URL

    async def call_tool(self, name: str, arguments: dict[str, Any]) -> MCPToolResult:
        try:
            from src.mcp_server.tools import (
                add_task,
                list_tasks,
                update_task,
                complete_task,
                delete_task,
            )

            tool_map = {
                "add_task": add_task.handle,
                "list_tasks": list_tasks.handle,
                "update_task": update_task.handle,
                "complete_task": complete_task.handle,
                "delete_task": delete_task.handle,
            }

            if name not in tool_map:
                return MCPToolResult(
                    success=False,
                    error={"code": "TOOL_NOT_FOUND", "message": f"Unknown tool: {name}"},
                )

            result = await tool_map[name](arguments)

            if result.get("success"):
                return MCPToolResult(success=True, data=result)
            else:
                return MCPToolResult(
                    success=False,
                    error=result.get("error", {"message": "Tool execution failed"}),
                )

        except Exception as e:
            logger.exception("MCP tool execution failed")
            return MCPToolResult(
                success=False,
                error={"code": "INTERNAL_ERROR", "message": str(e)},
            )

    async def aclose(self):
        """No-op for now (reserved for future MCP transport)."""
        return
