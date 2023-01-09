from __future__ import annotations

from enum import Enum


class ChangeIpv6ReverseNameserversType(str, Enum):
    CHANGE_IPV6_REVERSE_NAMESERVERS = "change_ipv6_reverse_nameservers"

    def __str__(self) -> str:
        return str(self.value)
