"""Main entry point for the data-mcp server."""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from platform_sdk import MCPConfig, configure_logging, get_logger

from .data_mcp_service import DataMcpService

configure_logging()
log = get_logger(__name__)

# Module-level: required for FastMCP construction before lifespan runs.
config = MCPConfig.load()

service = DataMcpService(config=config)

if config.transport == "sse":
    mcp = FastMCP(
        "Enterprise Data MCP",
        lifespan=service.lifespan,
        host="0.0.0.0",
        port=config.port,
    )
else:
    mcp = FastMCP("Enterprise Data MCP", lifespan=service.lifespan)

service.register_tools(mcp)


if __name__ == "__main__":
    log.info("mcp_server_starting", transport=config.transport)
    service.run_with_registration(mcp, config.transport)
