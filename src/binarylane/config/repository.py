from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Type, TypeVar
from binarylane.pycompat.typing import Protocol

import binarylane.config.sources as src

if TYPE_CHECKING:
    from binarylane.config.options import OptionName


class Source(Protocol):
    def get(self, name: str) -> Optional[str]:
        ...


T = TypeVar("T", bound=Source)


class Repository:
    _sources: List[Source]

    def __init__(self, default_source: bool = True) -> None:
        self._sources = []

        if default_source:
            self.add_source(src.DefaultSource())

    def add_source(self, source: Source) -> None:
        self._sources.append(source)

    def get_source(self, source_type: Type[T]) -> T:
        for source in self._sources[::-1]:
            if isinstance(source, source_type):
                return source
        raise KeyError(str(source_type))

    def add_option(self, name: OptionName, value: str) -> None:
        self.add_source(src.RuntimeSource({name: value}))

    def get_option(self, name: OptionName) -> Optional[str]:
        for source in self._sources[::-1]:
            value = source.get(name)
            if value is not None:
                return value
        return None

    def required_option(self, name: OptionName) -> str:
        value = self.get_option(name)
        if value is None:
            raise KeyError(name)
        return value

    def __repr__(self) -> str:
        return f"Repository([{', '.join([repr(source) for source in self._sources])}])"
