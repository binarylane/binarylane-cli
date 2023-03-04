from __future__ import annotations

from typing import Dict, Optional

from binarylane.config.types import Option, Source


class RuntimeSource(Source):
    def __init__(self, config: Dict[Option, str]) -> None:
        self._config = config

    def get(self, name: Option) -> Optional[str]:
        return self._config.get(name)
