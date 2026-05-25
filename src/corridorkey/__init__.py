"""CorridorKey - A key management and access control library.

This package provides tools for managing cryptographic keys,
access corridors, and permission-based authentication flows.

Note: Personal fork for learning purposes. Tracking upstream at
nikopueringer/CorridorKey.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("corridorkey")
except PackageNotFoundError:  # pragma: no cover
    # Fall back to a dev version string when package metadata is unavailable
    # (e.g. when running directly from source without installing)
    __version__ = "0.0.0.dev0"

__all__ = ["__version__"]
