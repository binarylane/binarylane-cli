from __future__ import annotations

from enum import Enum


class ActionStatus(str, Enum):
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"
    ERRORED = "errored"

    def __str__(self) -> str:
        return str(self.value)
