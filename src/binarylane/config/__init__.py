from __future__ import annotations

from abc import ABC
from argparse import Namespace
from pathlib import Path
from typing import Dict, Optional

import binarylane.config.sources as src
from binarylane.config.options import OptionAttributes, OptionName
from binarylane.config.repository import Repository, Source


class Config(Repository, OptionAttributes, ABC):
    def __init__(
        self,
        *,
        default_source: bool = False,
        user_sources: bool = False,
        config_file: Optional[Path] = src.FileSource.DEFAULT_PATH,
    ) -> None:
        super().__init__(default_source=default_source)

        if not user_sources:
            return

        self.add_source(src.FileSource(config_file))
        self.add_source(src.EnvironmentSource())

    def add_commandline(self, commandline: Namespace) -> None:
        self.add_source(src.CommandlineSource(commandline))

    def add_source(self, source: Source) -> None:
        super().add_source(source)

        # If we have a file source, update its config section:
        try:
            self.get_source(src.FileSource).section_name = self.config_section
        except KeyError:
            pass

    def save(self) -> None:
        # We will determine what to save by comparing current state with default
        default = DefaultConfig()

        # Create a dictionary of options with non-default values
        config_options: Dict[str, Optional[str]] = {}
        config_options[OptionName.API_URL] = self.api_url if self.api_url != default.api_url else None
        config_options[OptionName.API_TOKEN] = self.api_token if self.api_token != default.api_token else None
        config_options[OptionName.API_DEVELOPMENT] = (
            str(self.api_development).lower() if self.api_development != default.api_development else None
        )

        # Write configuration to disk
        file = self.get_source(src.FileSource)
        file.save(config_options)


class DefaultConfig(Config):
    def __init__(self) -> None:
        super().__init__(default_source=True, user_sources=False)


class UserConfig(Config):
    def __init__(self, *, config_file: Optional[Path] = src.FileSource.DEFAULT_PATH) -> None:
        super().__init__(default_source=True, user_sources=True, config_file=config_file)
