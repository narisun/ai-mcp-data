"""Backwards-compat entrypoint shim. Delegates to src.main.

Uses service.run_with_registration so the MCP registers with the platform
registry at process startup (FastMCP's SSE lifespan only runs per-connection,
which is too late). See SDK 0.5.1 for details.
"""
from .main import TRANSPORT, mcp, service

if __name__ == "__main__":
    service.run_with_registration(mcp, TRANSPORT)
