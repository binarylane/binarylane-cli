from __future__ import annotations

from enum import Enum


class ChangeSeparatePrivateNetworkInterfaceType(str, Enum):
    CHANGE_SEPARATE_PRIVATE_NETWORK_INTERFACE = "change_separate_private_network_interface"

    def __str__(self) -> str:
        return str(self.value)
