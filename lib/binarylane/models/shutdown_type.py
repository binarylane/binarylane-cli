from __future__ import annotations

from enum import Enum


class ShutdownType(str, Enum):
    SHUTDOWN = "shutdown"

    def __str__(self) -> str:
        return str(self.value)
