from __future__ import annotations

from typing import Optional

from binarylane.console import ConfigSource, Setting


class RuntimeConfig(ConfigSource):
    name: Setting
    value: str

    def __init__(self, name: Setting, value: str) -> None:
        self.name = name
        self.value = value

    def get(self, name: Setting) -> Optional[str]:
        return self.value if self.name == name else None
