from __future__ import annotations

from enum import Enum


class ResizeDiskType(str, Enum):
    RESIZE_DISK = "resize_disk"

    def __str__(self) -> str:
        return str(self.value)
