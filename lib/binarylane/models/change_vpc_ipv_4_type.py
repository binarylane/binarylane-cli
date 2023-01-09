from __future__ import annotations

from enum import Enum


class ChangeVpcIpv4Type(str, Enum):
    CHANGE_VPC_IPV4 = "change_vpc_ipv4"

    def __str__(self) -> str:
        return str(self.value)
