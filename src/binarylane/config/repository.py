from __future__ import annotations

from argparse import Namespace
from typing import List, Optional, Type, TypeVar, Union, overload

from binarylane.config.options import Options
from binarylane.config.sources import CommandlineSource, DefaultSource, EnvironmentSource, FileSource, RuntimeSource
from binarylane.config.types import Option, Source
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound=Source)


class Repository(Options):
    _sources: List[Source]

    @property
    def _option_source(self) -> Source:
        return self

    def __init__(self, *, default_source: bool = True) -> None:
        self._sources = []

        if default_source is True:
            self.add_source(DefaultSource())

    def initialize(self, init: Namespace) -> None:
        """Add standard configuration sources"""
        self.add_source(FileSource())
        self.add_source(EnvironmentSource())
        self.add_source(CommandlineSource(init))

        # After all config sources added, tell FileConfig which section to use:
        config_section = self[Option.CONFIG_SECTION]
        self.get_source(FileSource).section_name = config_section

    def get(self, name: Option, default: Optional[str] = None) -> Optional[str]:
        for source in self._sources[::-1]:
            value = source.get(name)
            if value is not None:
                return value

        return default

    def __getitem__(self, name: Option) -> str:
        value = self.get(name)
        if value is None:
            raise KeyError(name)
        return value

    def add_option(self, name: Option, value: str) -> None:
        self.add_source(RuntimeSource({name: value}))

    def add_source(self, config_source: Source) -> Repository:
        self._sources.append(config_source)
        return self

    @overload
    def get_source(self, source_type: Type[T]) -> T:
        ...

    @overload
    def get_source(self, source_type: Type[T], default: Optional[T]) -> Optional[T]:
        ...

    def get_source(self, source_type: Type[T], default: Union[Unset, None, T] = UNSET) -> Optional[T]:
        for source in self._sources:
            if isinstance(source, source_type):
                return source

        if isinstance(default, Unset):
            raise KeyError(str(source_type))
        return default

    def save(self) -> None:
        # We will determine what to save by comparing current state with default
        default = DefaultSource()
        config_options = {}

        # Save API URL if its non-default
        api_url = self.get(Option.API_URL)
        config_options[Option.API_URL] = api_url if api_url != default.get(Option.API_URL) else None

        # Save API Token
        config_options[Option.API_TOKEN] = self.get(Option.API_TOKEN)

        # Save boolean api_development if its non-default
        api_development = self.get(Option.API_DEVELOPMENT)
        config_options[Option.API_DEVELOPMENT] = (
            api_development if bool(api_development) != bool(default.get(Option.API_DEVELOPMENT)) else None
        )

        # Write configuration to disk
        file = self.get_source(FileSource)
        file.save(config_options)
