from __future__ import annotations

import argparse
import configparser
import os
import sys
from abc import ABC
from pathlib import Path
from typing import ClassVar, Dict, Optional
from binarylane.pycompat.typing import Protocol


class _SourceBase(ABC):
    _config: Dict[str, str]

    def get(self, name: str) -> Optional[str]:
        return self._config.get(name, None)


class CommandlineSource(_SourceBase):
    def __init__(self, config: argparse.Namespace) -> None:
        self._config = {key.replace("_", "-"): str(value) for key, value in vars(config).items() if value is not None}


class DefaultSource(_SourceBase):
    def __init__(self) -> None:
        self._config = {
            "api-url": "https://api.binarylane.com.au",
            "context": "bl",
        }


class EnvironmentSource(_SourceBase):
    prefix: ClassVar[str] = "BL_"

    def __init__(self) -> None:
        self._config = {self._get_name(key): value for key, value in os.environ.items() if key.startswith(self.prefix)}

    def _get_name(self, key: str) -> str:
        return key[len(self.prefix) :].lower().replace("_", "-")


class RuntimeSource(_SourceBase):
    def __init__(self, config: Dict[str, str]) -> None:
        self._config = config


class FileSource:
    _DIRNAME = "binarylane"
    _FILENAME = "config.ini"
    _API_TOKEN = "api-token"
    section_name: str

    _parser: configparser.ConfigParser

    def __init__(self, config_file: Optional[Path] = None) -> None:
        self._parser = configparser.ConfigParser()
        self._read(config_file)
        self.section_name = configparser.DEFAULTSECT

    @staticmethod
    def _get_config_home() -> Path:
        """Return platform-specific path that programs should store configuration in"""
        # On windows, configuration is stored in APPDATA
        if sys.platform == "win32":
            appdata = os.getenv("APPDATA")
            if not appdata:
                raise EnvironmentError("%APPDATA% is not set?")
            return Path(appdata)

        # On other systems, use XDG_CONFIG_HOME if set
        xdg_config_home = os.getenv("XDG_CONFIG_HOME")
        if xdg_config_home:
            return Path(xdg_config_home)

        # Otherwise, use $HOME/.config
        home = os.getenv("HOME")
        if not home:
            raise EnvironmentError("$HOME is not set?")
        home_config = Path(home) / ".config"

        # Ensure $HOME/.config is a directory, creating it if necessary
        if home_config.exists() and not home_config.is_dir():
            raise EnvironmentError(f"{home_config} is not a directory?")
        home_config.mkdir(mode=0o700, exist_ok=True)
        return home_config

    def _get_config_dir(self) -> Path:
        return self._get_config_home() / self._DIRNAME

    def _read(self, config_file: Optional[Path] = None) -> None:
        if config_file is None:
            config_file = self._get_config_dir() / self._FILENAME
        if config_file.exists():
            self._parser.read(config_file)

    def save(self, config_options: Dict[str, Optional[str]]) -> None:
        # Update the section with provided options:
        for option, value in config_options.items():
            if value is not None:
                # ConfigParser needs actual str, not _Value
                self._section[option] = str(value)
            # A value of None means "use default", and so should be removed from the section
            else:
                self._section.pop(option, None)

        # Write the updated config to disk
        config_dir = self._get_config_dir()
        config_dir.mkdir(mode=0o700, exist_ok=True)
        with open(config_dir / self._FILENAME, "w", encoding="utf-8") as file:
            self._parser.write(file)

    @property
    def _section(self) -> configparser.SectionProxy:
        if self.section_name not in self._parser:
            self._parser[self.section_name] = {}
        return self._parser[self.section_name]

    def get(self, name: str) -> Optional[str]:
        return self._section.get(name, None)


class Source(Protocol):
    def get(self, name: str) -> Optional[str]:
        ...
