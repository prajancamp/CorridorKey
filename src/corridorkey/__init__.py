"""CorridorKey - A key management and access control library.

This package provides tools for managing cryptographic keys,
access corridors, and permission-based authentication flows.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("corridorkey")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0.dev0"

__all__ = ["__version__"]
