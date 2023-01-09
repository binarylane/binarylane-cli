from __future__ import annotations

from enum import Enum


class ChangePartnerType(str, Enum):
    CHANGE_PARTNER = "change_partner"

    def __str__(self) -> str:
        return str(self.value)
