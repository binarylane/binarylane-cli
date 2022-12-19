from ...client.api.server.server_data_usage_list import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_data-usage_list"

    @property
    def description(self):
        return """Fetch all Current Data Usage (Transfer) for All Servers"""

    def configure(self, parser):
        """Add arguments for server_data-usage_list"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
