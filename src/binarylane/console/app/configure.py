from __future__ import annotations

import logging
from typing import TYPE_CHECKING, List

from binarylane.console import Setting
from binarylane.console.app.lazy_runner import LazyRunner
from binarylane.console.config import Config
from binarylane.console.runners import Runner

if TYPE_CHECKING:
    from binarylane.api.accounts.get_v2_account import sync_detailed
    from binarylane.client import AuthenticatedClient

logger = logging.getLogger(__name__)


class ConfigureRunner(LazyRunner):
    """Interactive runner to request, verify, and store API token to configuration file"""

    def run(self, args: List[str]) -> None:
        if args == [Runner.CHECK]:
            return

        print(
            """
To get started with the BinaryLane CLI, you must obtain an API token for the CLI to authenticate with:

  1. Go to https://home.binarylane.com.au/api-info and login when prompted.
  2. Click the [+ Create Token] button, enter a token name such as "CLI" and click [Create].
  3. Copy the generated API token to the clipboard and paste below.
"""
        )
        # Create new config based on context
        config = Config()
        config.add_config_source(self.context.config)
        # Add api-token to it
        config.set(Setting.ApiToken, input("Enter your API access token: "))

        print(f"Trying to authenticate with {config.get(Setting.ApiUrl)} ...")
        if self._try_token(config):
            config.save()
            print("Success! API access token saved.")
        else:
            self.error("Invalid API token")

    def _try_token(self, config: Config) -> bool:
        """Return bool indicating if API is accessible with current configuration"""

        from binarylane.api.accounts.get_v2_account import sync_detailed
        from binarylane.client import AuthenticatedClient

        api_url = Setting.ApiUrl
        if api_url is None:
            raise ValueError(Setting.ApiUrl)
        api_token = Setting.ApiToken or ""

        client = AuthenticatedClient(
            base_url=api_url, token=api_token, verify_ssl=not bool(config.get(Setting.ApiDevelopment))
        )
        response = sync_detailed(client=client)

        # Check for success
        if response.status_code == 200:
            return True

        # Request failed; it should be a 401 if token is invalid. If it isnt, show some extra info:
        if response.status_code != 401:
            logger.warning("HTTP %s - %s", response.status_code.value, response.status_code.name)
        return False


Command = ConfigureRunner
