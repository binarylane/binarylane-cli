from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional

import binarylane.config.sources as src
from binarylane.config.options import OptionAttributes, OptionName
from binarylane.config.repository import Repository, Source

if TYPE_CHECKING:
    from argparse import Namespace
    from pathlib import Path


class _Config(Repository, OptionAttributes):
    def __init__(self) -> None:
        super().__init__(default_source=True)


class DefaultConfig(_Config):
    pass


class UserConfig(_Config):
    def __init__(self, *, config_file: Optional[Path] = src.FileSource.DEFAULT_PATH) -> None:
        super().__init__()

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

        # Output preferences - only save if explicitly set
        if self.output_format:
            config_options[OptionName.OUTPUT_FORMAT] = self.output_format
        if self.show_header is not None:
            config_options[OptionName.SHOW_HEADER] = str(self.show_header).lower()

        # Per-command format preferences
        for opt in [
            OptionName.FORMAT_IMAGES,
            OptionName.FORMAT_SERVERS,
            OptionName.FORMAT_DOMAINS,
            OptionName.FORMAT_VPCS,
            OptionName.FORMAT_LOAD_BALANCERS,
            OptionName.FORMAT_SSH_KEYS,
        ]:
            value = self.get_option(opt)
            if value:
                config_options[opt] = value

        # Server creation defaults
        for opt in [
            OptionName.DEFAULT_REGION,
            OptionName.DEFAULT_SIZE,
            OptionName.DEFAULT_IMAGE,
            OptionName.DEFAULT_SSH_KEYS,
            OptionName.DEFAULT_USER_DATA,
            OptionName.DEFAULT_PASSWORD,
            OptionName.DEFAULT_VPC,
        ]:
            value = self.get_option(opt)
            if value:
                config_options[opt] = value

        # Boolean defaults
        if self.default_backups is not None:
            config_options[OptionName.DEFAULT_BACKUPS] = str(self.default_backups).lower()
        if self.default_port_blocking is not None:
            config_options[OptionName.DEFAULT_PORT_BLOCKING] = str(self.default_port_blocking).lower()

        # Terminal settings
        if self.terminal_width:
            config_options[OptionName.TERMINAL_WIDTH] = str(self.terminal_width)

        # Write configuration to disk
        file = self.get_source(src.FileSource)
        file.save(config_options)
