from ...client.api.account.account_get import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "account_get"

    @property
    def description(self):
        return """Fetch Information About the Current Account"""

    def configure(self, parser):
        """Add arguments for account_get"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
