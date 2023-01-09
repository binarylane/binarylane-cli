from __future__ import annotations

from enum import Enum


class AttachBackupType(str, Enum):
    ATTACH_BACKUP = "attach_backup"

    def __str__(self) -> str:
        return str(self.value)
