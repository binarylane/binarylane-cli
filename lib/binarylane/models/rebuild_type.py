from __future__ import annotations

from enum import Enum


class RebuildType(str, Enum):
    REBUILD = "rebuild"

    def __str__(self) -> str:
        return str(self.value)
