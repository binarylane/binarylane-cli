from __future__ import annotations


class Context:
    _prog: str

    def __init__(self) -> None:
        self._prog = "bl"

    @property
    def prog(self) -> str:
        return self._prog

    @prog.setter
    def prog(self, name: str) -> None:
        self._prog = f"bl {name}"
