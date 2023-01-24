from __future__ import annotations

import sys

__all__ = [
    "get_origin",
    "get_args",
]

# TODO: use try/except ImportError when
# https://github.com/python/mypy/issues/1393 is fixed
if sys.version_info < (3, 8):
    from typing_extensions import get_args, get_origin
else:
    from typing import get_args, get_origin
