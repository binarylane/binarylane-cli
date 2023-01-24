from __future__ import annotations

import sys

__all__ = [
    "metadata",
]

# TODO: use try/except ImportError when
# https://github.com/python/mypy/issues/1393 is fixed
if sys.version_info < (3, 8):
    # additional changes to importlib.metadata were made in 3.10, but binarylane-cli does not utilise them.
    import importlib_metadata as metadata
else:
    from importlib import metadata
