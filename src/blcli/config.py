"""Provided typed access to user configuration values"""

from __future__ import annotations

import os


class Config:
    """User configuration manager"""

    @property
    def api_token(self) -> str:
        """Obtain user's API token from environment variable or configuration file"""
        token = os.getenv("BL_CLI_TOKEN")
        if token:
            return token

        with open(os.path.expanduser("~/.config/python-blcli"), encoding="utf-8") as config_file:
            return config_file.read().strip()

    @classmethod
    def load(cls) -> "Config":
        """Create instance of Config() and load configuration file(s)"""
        return cls()
