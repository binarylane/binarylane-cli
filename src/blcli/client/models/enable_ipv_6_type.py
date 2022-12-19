from enum import Enum


class EnableIpv6Type(str, Enum):
    ENABLE_IPV6 = "enable_ipv6"

    def __str__(self) -> str:
        return str(self.value)
