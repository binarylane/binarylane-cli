from __future__ import annotations

from enum import Enum


class BackupSlot(str, Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    TEMPORARY = "temporary"

    def __str__(self) -> str:
        return str(self.value)
