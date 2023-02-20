from typing import Any, Protocol


class Lookup(Protocol):
    def __call__(self, value: str) -> Any:
        ...
