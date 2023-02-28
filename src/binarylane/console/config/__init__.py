from __future__ import annotations

from argparse import Namespace
from configparser import ConfigParser
from typing import List, Optional, Union

from binarylane.console import ConfigSource, Setting
from binarylane.console.config.commandline import CommandLineConfig
from binarylane.console.config.default import DefaultConfig
from binarylane.console.config.environment import EnvironmentConfig
from binarylane.console.config.file import FileConfig
from binarylane.console.config.runtime import RuntimeConfig


class _OptionValue(str):
    """
    Override standard bool behaviour for OptionValue strings so that rather than the usual behaviour, a value of
    - "true"/"yes"/"1"/"on" is True
    - "false"/"no"/"0"/"off" is False
    - all other values (including "") will raise ValueError

    Above comparisons are case-insensitive.
    """

    def __bool__(self) -> bool:
        value = ConfigParser.BOOLEAN_STATES.get(self.lower())
        if value is not None:
            return value
        raise ValueError(f"Not a boolean: {self}")


class Config(ConfigSource):
    _config_sources: List[ConfigSource]
    _file: Optional[FileConfig]

    def __init__(self, *, init: Optional[Namespace] = None, default_config: bool = True) -> None:
        self._config_sources = []

        if default_config is True:
            self.add_config_source(DefaultConfig())

        if init is None:
            return

        self._file = FileConfig()
        self.add_config_source(self._file)
        self.add_config_source(EnvironmentConfig())
        self.add_config_source(CommandLineConfig(init))

        # After all config sources added, tell FileConfig which section to use:
        config_section = self.get(Setting.ConfigSection)
        # ConfigSection cannot be null as DefaultConfig provides a value
        assert config_section is not None
        self._file.section_name = config_section

    def get(self, name: Setting) -> Optional[str]:
        for source in self._config_sources[::-1]:
            value = source.get(name)
            if value:
                return _OptionValue(value)

        return None

    def set(self, name: Setting, value: str) -> None:
        self.add_config_source(RuntimeConfig(name, value))

    def add_config_source(self, config_source: ConfigSource) -> Config:
        self._config_sources.append(config_source)
        return self

    def save(self) -> None:
        if not self._file:
            raise RuntimeError("Configuration file has not been loaded")
        self._file.save()
