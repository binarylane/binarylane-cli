from __future__ import annotations

from typing import List

from binarylane.console.commands import api
from binarylane.console.runners import Descriptor

__all__ = ["descriptors"]
descriptors: List[Descriptor] = list(api.descriptors) + [
    Descriptor(".commands.configure", "configure", "Configure access to BinaryLane API"),
    Descriptor(".commands.version", "version", "Show the current version"),
]
