"""
Config package for DeepCode MCP tool definitions.

This package contains MCP (Model Context Protocol) tool definitions
used by various AI agents in the DeepCode system.
"""

from .mcp_tool_definitions import MCPToolDefinitions, get_mcp_tools
from .mcp_tool_definitions_index import (
    MCPToolDefinitions as MCPToolDefinitionsIndex,
    get_mcp_tools as get_mcp_tools_index,
)

__all__ = [
    "MCPToolDefinitions",
    "get_mcp_tools",
    "MCPToolDefinitionsIndex",
    "get_mcp_tools_index",
]
