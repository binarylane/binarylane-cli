from __future__ import annotations

import argparse
from typing import Optional

from binarylane.console import ConfigSource


class CommandLineConfig(ConfigSource):
    def __init__(self, config: argparse.Namespace) -> None:
        self._items = {key.replace("_", "-"): str(value) for key, value in vars(config).items() if value is not None}

    def get(self, name: str) -> Optional[str]:
        return self._items.get(name, None)
