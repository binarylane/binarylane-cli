from __future__ import annotations

from argparse import Namespace
from typing import List, Optional, Type, TypeVar, Union, overload

from binarylane.types import UNSET, Unset

from binarylane.console.config._options import Options
from binarylane.console.config._value import Value
from binarylane.console.config.commandline_source import CommandlineSource
from binarylane.console.config.default_source import DefaultSource
from binarylane.console.config.environment_source import EnvironmentSource
from binarylane.console.config.file_source import FileSource
from binarylane.console.config.option import Option
from binarylane.console.config.runtime_source import RuntimeSource
from binarylane.console.config.source import Source

T = TypeVar("T", bound=Source)


class Config(Options):
    _config_sources: List[Source]

    @property
    def _option_source(self) -> Source:
        return self

    def __init__(self, *, init: Optional[Namespace] = None, default_config: bool = True) -> None:
        self._config_sources = []

        if default_config is True:
            self.add_config_source(DefaultSource())

        if init is not None:
            self.initialize(init)

    def initialize(self, init: Namespace) -> None:
        # Load configuration sources
        self.add_config_source(FileSource())
        self.add_config_source(EnvironmentSource())
        self.add_config_source(CommandlineSource(init))

        # After all config sources added, tell FileConfig which section to use:
        config_section = self[Option.CONFIG_SECTION]
        self.get_config_source(FileSource).section_name = config_section

    def get(self, name: Option, default: Optional[str] = None) -> Optional[str]:
        for source in self._config_sources[::-1]:
            value = source.get(name)
            # `value` is normally a str, but could also be our _Value subclass if one Config is added as a source
            # to a second  Config instance - `bl configure` does this for example.
            if isinstance(value, str):
                return Value(str(value))

        return default

    def __getitem__(self, name: Option) -> str:
        value = self.get(name)
        if value is None:
            raise KeyError(name)
        return value

    def set(self, name: Option, value: str) -> None:
        self.add_config_source(RuntimeSource(name, value))

    def add_config_source(self, config_source: Source) -> Config:
        self._config_sources.append(config_source)
        return self

    @overload
    def get_config_source(self, source_type: Type[T]) -> T:
        ...

    @overload
    def get_config_source(self, source_type: Type[T], default: Optional[T]) -> Optional[T]:
        ...

    def get_config_source(self, source_type: Type[T], default: Union[Unset, None, T] = UNSET) -> Optional[T]:
        for source in self._config_sources:
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
        file = self.get_config_source(FileSource)
        file.save(config_options)
