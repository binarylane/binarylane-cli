from ...client.api.server.server_tagged_delete import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_tagged_delete"

    @property
    def description(self):
        return """Cancel Existing Servers by Tag"""

    def configure(self, parser):
        """Add arguments for server_tagged_delete"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
