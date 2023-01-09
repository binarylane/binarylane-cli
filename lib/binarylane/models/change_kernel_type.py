from __future__ import annotations

from enum import Enum


class ChangeKernelType(str, Enum):
    CHANGE_KERNEL = "change_kernel"

    def __str__(self) -> str:
        return str(self.value)
