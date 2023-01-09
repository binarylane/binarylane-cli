from __future__ import annotations

from enum import Enum


class TakeBackupType(str, Enum):
    TAKE_BACKUP = "take_backup"

    def __str__(self) -> str:
        return str(self.value)
