from __future__ import annotations

from enum import Enum


class ChangeNetworkType(str, Enum):
    CHANGE_NETWORK = "change_network"

    def __str__(self) -> str:
        return str(self.value)
