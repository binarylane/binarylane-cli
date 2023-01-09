from __future__ import annotations

from enum import Enum


class UncancelType(str, Enum):
    UNCANCEL = "uncancel"

    def __str__(self) -> str:
        return str(self.value)
