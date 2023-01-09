from __future__ import annotations

from enum import Enum


class ChangeIpv6Type(str, Enum):
    CHANGE_IPV6 = "change_ipv6"

    def __str__(self) -> str:
        return str(self.value)
