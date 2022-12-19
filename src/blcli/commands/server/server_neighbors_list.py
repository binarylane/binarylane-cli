from ...client.api.server.server_neighbors_list import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_neighbors_list"

    @property
    def description(self):
        return """List All Servers That Share a Host"""

    def configure(self, parser):
        """Add arguments for server_neighbors_list"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
