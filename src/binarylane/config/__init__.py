from __future__ import annotations

from typing import Dict, Optional

from binarylane.config import sources
from binarylane.config.options import OptionAttributes, OptionName
from binarylane.config.repository import Repository


class Config(Repository, OptionAttributes):
    def save(self) -> None:
        # We will determine what to save by comparing current state with default
        default = Config(default_source=True)

        # Create a dictionary of options with non-default values
        config_options: Dict[str, Optional[str]] = {}
        config_options[OptionName.API_URL] = self.api_url if self.api_url != default.api_url else None
        config_options[OptionName.API_TOKEN] = self.api_token if self.api_token != default.api_token else None
        config_options[OptionName.API_DEVELOPMENT] = (
            str(self.api_development).lower() if self.api_development != default.api_development else None
        )

        # Write configuration to disk
        file = self.get_source(sources.FileSource)
        file.save(config_options)
