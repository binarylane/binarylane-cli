from __future__ import annotations

import sys
from shlex import quote
from typing import Iterable

__all__ = ["join"]


def shlex_join(split_command: Iterable[str]) -> str:
    """Return a shell-escaped string from *split_command*."""
    return " ".join(quote(arg) for arg in split_command)


# TODO: use try/except ImportError when
# https://github.com/python/mypy/issues/1393 is fixed
if sys.version_info < (3, 8):
    join = shlex_join
else:
    from shlex import join
