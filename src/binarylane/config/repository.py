from __future__ import annotations

from argparse import Namespace
from pathlib import Path
from typing import List, Optional, Type, TypeVar
from binarylane.pycompat.typing import Protocol

import binarylane.config.sources as src
from binarylane.config.options import OptionName


class Source(Protocol):
    def get(self, name: str) -> Optional[str]:
        ...


T = TypeVar("T", bound=Source)


class Repository:
    _sources: List[Source]

    def __init__(self, *, default_source: bool = True) -> None:
        self._sources = []

        if default_source is True:
            self.add_source(src.DefaultSource())

    def initialize(self, *, commandline: Namespace, config_file: Optional[Path] = src.FileSource.DEFAULT_PATH) -> None:
        try:
            # Check for existing commandline to see if we have initialized previously
            self.get_source(src.CommandlineSource)
            # If we have, add second command line source
            self.add_source(src.CommandlineSource(commandline))
        except KeyError:
            # Otherwise, perform initialization
            self.add_source(src.FileSource(config_file))
            self.add_source(src.EnvironmentSource())
            self.add_source(src.CommandlineSource(commandline))

        # After all sources added, tell FileSource which section to use:
        self.get_source(src.FileSource).section_name = self.required_option(OptionName.CONFIG_SECTION)

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
