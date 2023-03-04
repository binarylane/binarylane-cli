from __future__ import annotations

import argparse
from typing import Optional

from binarylane.config.types import Option, Source


class CommandlineSource(Source):
    def __init__(self, config: argparse.Namespace) -> None:
        self._config = {key.replace("_", "-"): str(value) for key, value in vars(config).items() if value is not None}

    def get(self, name: Option) -> Optional[str]:
        return self._config.get(name)
