from __future__ import annotations

from enum import Enum


class AddDiskType(str, Enum):
    ADD_DISK = "add_disk"

    def __str__(self) -> str:
        return str(self.value)
