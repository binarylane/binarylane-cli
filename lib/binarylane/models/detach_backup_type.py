from __future__ import annotations

from enum import Enum


class DetachBackupType(str, Enum):
    DETACH_BACKUP = "detach_backup"

    def __str__(self) -> str:
        return str(self.value)
