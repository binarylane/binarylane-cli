from __future__ import annotations

import logging
from typing import List

from binarylane.config import Config

from binarylane.console.runners import Runner

logger = logging.getLogger(__name__)


class ConfigureRunner(Runner):
    """Interactive runner to request, verify, and store API token to configuration file"""

    def run(self, args: List[str]) -> None:
        if args == [Runner.CHECK]:
            return

        self.parse(args)

        print(
            """
To get started with the BinaryLane CLI, you must obtain an API token for the CLI to authenticate with:

  1. Go to https://home.binarylane.com.au/api-info and login when prompted.
  2. Click the [+ Create Token] button, enter a token name such as "CLI" and click [Create].
  3. Copy the generated API token to the clipboard and paste below.
"""
        )
        # Add supplied token to config
        config = self._context
        config.api_token = input("Enter your API access token: ")

        # Test the supplied token:
        print(f"Trying to authenticate with {config.api_url} ...")
        if self._try_token(config):
            config.save()
            print("Success! API access token saved.")
        else:
            self.error("Invalid API token")

    def _try_token(self, config: Config) -> bool:
        """Return bool indicating if API is accessible with current configuration"""

        from binarylane.api.accounts.get_v2_account import sync_detailed
        from binarylane.client import AuthenticatedClient

        verify_ssl = not config.api_development
        client = AuthenticatedClient(base_url=config.api_url, token=config.api_token, verify_ssl=verify_ssl)
        response = sync_detailed(client=client)

        # Check for success
        if response.status_code == 200:
            return True

        # Request failed; it should be a 401 if token is invalid. If it isnt, show some extra info:
        if response.status_code != 401:
            logger.warning("HTTP %s - %s", response.status_code.value, response.status_code.name)
        return False


Command = ConfigureRunner
