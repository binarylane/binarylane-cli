from __future__ import annotations

from enum import Enum


class ThresholdAlertType(str, Enum):
    CPU = "cpu"
    STORAGE_REQUESTS = "storage-requests"
    NETWORK_INCOMING = "network-incoming"
    NETWORK_OUTGOING = "network-outgoing"
    DATA_TRANSFER_USED = "data-transfer-used"
    STORAGE_USED = "storage-used"
    MEMORY_USED = "memory-used"

    def __str__(self) -> str:
        return str(self.value)
