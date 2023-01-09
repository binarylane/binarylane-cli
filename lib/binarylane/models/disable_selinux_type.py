from __future__ import annotations

from enum import Enum


class DisableSelinuxType(str, Enum):
    DISABLE_SELINUX = "disable_selinux"

    def __str__(self) -> str:
        return str(self.value)
