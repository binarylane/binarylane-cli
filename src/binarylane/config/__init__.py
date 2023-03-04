from __future__ import annotations

from argparse import Namespace
from typing import Dict, List, Optional, Type, TypeVar

from binarylane.config import sources
from binarylane.config.options import ConfigBase, Option

T = TypeVar("T", bound=sources.Source)


class Config(ConfigBase):
    _sources: List[sources.Source]

    def __init__(self, *, default_source: bool = True) -> None:
        self._sources = []

        if default_source is True:
            self.add_source(sources.DefaultSource())

    def initialize(self, commandline: Namespace) -> None:
        # Add standard configuration sources
        self.add_source(sources.FileSource())
        self.add_source(sources.EnvironmentSource())
        self.add_source(sources.CommandlineSource(commandline))

        # After all sources added, tell FileSource which section to use:
        self.get_source(sources.FileSource).section_name = self.config_section

    def add_source(self, source: sources.Source) -> Config:
        self._sources.append(source)
        return self

    def get_source(self, source_type: Type[T]) -> T:
        for source in self._sources:
            if isinstance(source, source_type):
                return source

        raise KeyError(str(source_type))

    def add_option(self, name: Option, value: str) -> Config:
        self.add_source(sources.RuntimeSource({name: value}))
        return self

    def get_option(self, name: Option, default: Optional[str] = None) -> Optional[str]:
        for source in self._sources[::-1]:
            value = source.get(name)
            if value is not None:
                return value

        return default

    def save(self) -> None:
        # We will determine what to save by comparing current state with default
        default = sources.DefaultSource()
        config_options: Dict[str, Optional[str]] = {}

        # Save API URL if its non-default
        api_url = self.get_option(Option.API_URL)
        config_options[Option.API_URL] = api_url if api_url != default.get(Option.API_URL) else None

        # Save API Token
        config_options[Option.API_TOKEN] = self.get_option(Option.API_TOKEN)

        # Save boolean api_development if its non-default
        api_development = self.get_option(Option.API_DEVELOPMENT)
        config_options[Option.API_DEVELOPMENT] = (
            api_development if bool(api_development) != bool(default.get(Option.API_DEVELOPMENT)) else None
        )

        # Write configuration to disk
        file = self.get_source(sources.FileSource)
        file.save(config_options)
