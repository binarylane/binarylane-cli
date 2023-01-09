from __future__ import annotations

from enum import Enum


class VideoDevice(str, Enum):
    CIRRUS_LOGIC = "cirrus-logic"
    STANDARD = "standard"
    VIRTIO = "virtio"
    VIRTIO_WIDE = "virtio-wide"

    def __str__(self) -> str:
        return str(self.value)
