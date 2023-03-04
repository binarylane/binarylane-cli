from __future__ import annotations

from binarylane.config import Config


class Context(Config):
    def __init__(self) -> None:
        super().__init__(default_source=True)
        self._prog = "bl"

    @property
    def prog(self) -> str:
        return self._prog

    @prog.setter
    def prog(self, name: str) -> None:
        self._prog = f"bl {name}"
