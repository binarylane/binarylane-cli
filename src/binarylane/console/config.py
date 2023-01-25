"""Provided typed access to user configuration values"""

from __future__ import annotations

import os
import sys
from configparser import ConfigParser, SectionProxy
from pathlib import Path


class Config:
    """User configuration manager"""

    _DIRNAME = "binarylane"
    _FILENAME = "config.ini"
    _SECTION = "bl"
    _API_TOKEN = "api-token"

    _parser: ConfigParser

    def __init__(self) -> None:
        self._parser = ConfigParser()
        self._migrate()
        self._read()

    @staticmethod
    def _get_config_home() -> Path:
        """Return platform-specific path that programs should store configuration in"""
        if sys.platform == "win32":
            appdata = os.getenv("APPDATA")
            if not appdata:
                raise EnvironmentError("%APPDATA% is not set?")
            return Path(appdata)

        xdg_config_home = os.getenv("XDG_CONFIG_HOME")
        if xdg_config_home:
            return Path(xdg_config_home)

        home = os.getenv("HOME")
        if not home:
            raise EnvironmentError("$HOME is not set?")
        return Path(home) / ".config"

    def _get_config_dir(self) -> Path:
        return self._get_config_home() / self._DIRNAME

    def _migrate(self) -> None:
        # NOTE: legacy config was always in ~/.config, even on Windows
        migrate_filename = Path(os.path.expanduser("~/.config/python-blcli"))
        if not migrate_filename.is_file():
            return

        # Read legacy config
        with open(migrate_filename, encoding="utf-8") as file:
            self._context[self._API_TOKEN] = file.read().strip()

        # Write current config format
        self.save()

        # Remove legacy config
        migrate_filename.unlink()

    def _read(self) -> None:
        config_file = self._get_config_dir() / self._FILENAME
        if config_file.exists():
            self._parser.read(config_file)

    def save(self) -> None:
        """Write contents of _parser to disk"""
        config_dir = self._get_config_dir()
        config_dir.mkdir(mode=0o700, exist_ok=True)
        with open(config_dir / self._FILENAME, "w", encoding="utf-8") as file:
            self._parser.write(file)

    @property
    def _context(self) -> SectionProxy:
        if self._SECTION not in self._parser:
            self._parser[self._SECTION] = {}
        return self._parser[self._SECTION]

    @property
    def api_url(self) -> str:
        """URL of BinaryLane API"""
        env_override = os.getenv("BL_API_URL")
        if env_override:
            return env_override

        return "https://api.binarylane.com.au"

    @property
    def api_token(self) -> str:
        """Obtain user's API token from environment variable or configuration file"""
        token = os.getenv("BL_API_TOKEN")
        if token:
            return token

        return self._context.get(self._API_TOKEN)

    @api_token.setter
    def api_token(self, value: str) -> None:
        self._context[self._API_TOKEN] = value

    @property
    def verify_ssl(self) -> bool:
        """Verify SSL certificates when making API requests"""
        env_override = os.getenv("BL_API_SKIP_VERIFY_SSL")
        if env_override:
            return not env_override.lower() in ("1", "true", "yes")
        return True

    @classmethod
    def load(cls) -> "Config":
        """Create instance of Config() and load configuration file(s)"""
        return cls()
