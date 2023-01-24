from __future__ import annotations

import sys

__all__ = [
    "cached_property",
]

# TODO: use try/except ImportError when
# https://github.com/python/mypy/issues/1393 is fixed
if sys.version_info < (3, 8):
    from backports.cached_property import cached_property
else:
    from functools import cached_property
