from __future__ import annotations

import logging
from typing import TYPE_CHECKING, List

from binarylane.console.runners import ExitCode, Runner
from binarylane.console.util import create_client

if TYPE_CHECKING:
    from binarylane.config import UserConfig

logger = logging.getLogger(__name__)


class Command(Runner):
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
            self.error(ExitCode.TOKEN, "Invalid API token")

    def _try_token(self, config: UserConfig) -> bool:
        """Return bool indicating if API is accessible with current configuration"""

        from binarylane.api.accounts.get_v2_account import sync_detailed

        response = sync_detailed(client=create_client(config))

        # Check for success
        if response.status_code == 200:
            return True

        # Request failed; it should be a 401 if token is invalid. If it isnt, show some extra info:
        if response.status_code != 401:
            logger.warning("HTTP %s - %s", response.status_code.value, response.status_code.name)
        return False
