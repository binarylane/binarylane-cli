from __future__ import annotations

from typing import Any, Protocol


class Lookup(Protocol):
    def __call__(self, value: str) -> Any:
        ...
