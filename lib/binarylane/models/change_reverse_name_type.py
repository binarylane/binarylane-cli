from __future__ import annotations

from enum import Enum


class ChangeReverseNameType(str, Enum):
    CHANGE_REVERSE_NAME = "change_reverse_name"

    def __str__(self) -> str:
        return str(self.value)
