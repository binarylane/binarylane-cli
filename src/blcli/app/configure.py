from getpass import getpass
from typing import TYPE_CHECKING, List

from ..cli import error, warn
from ..config import Config
from ..runners import Runner

if TYPE_CHECKING:
    from ..client import AuthenticatedClient
    from ..client.api.account.account_get import sync_detailed


class ConfigureRunner(Runner):
    """Interactive runner to request, verify, and store API token to configuration file"""

    @property
    def name(self) -> str:
        return "configure"

    @property
    def description(self) -> str:
        return "Configure access to BinaryLane API"

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
        config = Config.load()
        config.api_token = getpass("Enter your API access token: ")

        print(f"Trying to authenticate with {config.api_url} ...")
        if self._try_token(config):
            config.save()
            print("Success! API access token saved.")
        else:
            error("Invalid API token")

    def _try_token(self, config: Config) -> bool:
        """Return bool indicating if API is accessible with current configuration"""

        from ..client import AuthenticatedClient
        from ..client.api.account.account_get import sync_detailed

        client = AuthenticatedClient(token=config.api_token, base_url=config.api_url)
        response = sync_detailed(client=client)

        # Check for success
        if response.status_code == 200:
            return True

        # Request failed; it should be a 401 if token is invalid. If it isnt, show some extra info:
        if response.status_code != 401:
            warn(f"HTTP {response.status_code.value} - {response.status_code.name}")
        return False
