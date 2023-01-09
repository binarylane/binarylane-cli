from __future__ import annotations

from enum import Enum


class DeleteDiskType(str, Enum):
    DELETE_DISK = "delete_disk"

    def __str__(self) -> str:
        return str(self.value)
