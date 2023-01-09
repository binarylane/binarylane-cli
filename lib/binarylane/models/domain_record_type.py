from __future__ import annotations

from enum import Enum


class DomainRecordType(str, Enum):
    A = "A"
    AAAA = "AAAA"
    CAA = "CAA"
    CNAME = "CNAME"
    MX = "MX"
    NS = "NS"
    SOA = "SOA"
    SRV = "SRV"
    TXT = "TXT"

    def __str__(self) -> str:
        return str(self.value)
