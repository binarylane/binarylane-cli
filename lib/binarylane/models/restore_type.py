from __future__ import annotations

from enum import Enum


class RestoreType(str, Enum):
    RESTORE = "restore"

    def __str__(self) -> str:
        return str(self.value)
