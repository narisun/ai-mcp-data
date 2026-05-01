"""Backwards-compat entrypoint shim. Delegates to src.main."""
from .main import config, mcp, service

if __name__ == "__main__":
    service.run_with_registration(mcp, config.transport)
