from __future__ import annotations

from enum import Enum


class IsRunningType(str, Enum):
    IS_RUNNING = "is_running"

    def __str__(self) -> str:
        return str(self.value)
