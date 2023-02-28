from __future__ import annotations

from enum import Enum
from typing import Optional
from binarylane.pycompat.typing import Protocol


# pylint: disable=invalid-name
class Setting(str, Enum):
    ApiUrl = "api-url"
    ApiToken = "api-token"
    ApiDevelopment = "api-development"
    ConfigSection = "context"


class ConfigSource(Protocol):
    def get(self, name: Setting) -> Optional[str]:
        ...


class NullConfig(ConfigSource):
    def get(self, name: Setting) -> Optional[str]:
        return None


class Context:
    config: ConfigSource

    def __init__(self) -> None:
        self._prog = "bl"
        self.config = NullConfig()

    @property
    def prog(self) -> str:
        return self._prog

    @prog.setter
    def prog(self, name: str) -> None:
        self._prog = f"bl {name}"

    def __getitem__(self, item: Setting) -> str:
        value: Optional[str] = self.config.get(item)
        if value is None:
            raise ValueError(item)
        return value

    def get(self, item: Setting, default: str = "") -> str:
        value: Optional[str] = self.config.get(item)
        return value if value is not None else default
