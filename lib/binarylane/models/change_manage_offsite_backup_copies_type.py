from __future__ import annotations

from enum import Enum


class ChangeManageOffsiteBackupCopiesType(str, Enum):
    CHANGE_MANAGE_OFFSITE_BACKUP_COPIES = "change_manage_offsite_backup_copies"

    def __str__(self) -> str:
        return str(self.value)
