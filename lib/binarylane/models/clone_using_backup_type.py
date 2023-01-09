from __future__ import annotations

from enum import Enum


class CloneUsingBackupType(str, Enum):
    CLONE_USING_BACKUP = "clone_using_backup"

    def __str__(self) -> str:
        return str(self.value)
