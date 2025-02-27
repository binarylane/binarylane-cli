from __future__ import annotations

from enum import Enum


class ChangeRegionType(str, Enum):
    CHANGE_REGION = "change_region"

    def __str__(self) -> str:
        return str(self.value)
