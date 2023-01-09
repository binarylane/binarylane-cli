from __future__ import annotations

from enum import Enum


class AccountStatus(str, Enum):
    INCOMPLETE = "incomplete"
    ACTIVE = "active"
    WARNING = "warning"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)
