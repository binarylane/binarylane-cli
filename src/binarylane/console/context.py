from __future__ import annotations

from typing import Optional

from binarylane.console.config import Config, Option


class Context:
    config: Config

    def __init__(self) -> None:
        self.config = Config(default_config=False)
        self._prog = "bl"

    @property
    def prog(self) -> str:
        return self._prog

    @prog.setter
    def prog(self, name: str) -> None:
        self._prog = f"bl {name}"

    def __getitem__(self, item: Option) -> str:
        value: Optional[str] = self.config.get(item)
        if value is None:
            raise ValueError(item)
        return value

    def get(self, item: Option, default: str = "") -> str:
        value: Optional[str] = self.config.get(item)
        return value if value is not None else default
