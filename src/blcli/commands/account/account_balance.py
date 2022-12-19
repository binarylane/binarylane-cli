from ...client.api.account.account_balance import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "account_balance"

    @property
    def description(self):
        return """Fetch Current Balance Information"""

    def configure(self, parser):
        """Add arguments for account_balance"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
