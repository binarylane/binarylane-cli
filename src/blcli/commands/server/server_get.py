from ...client.api.server.server_get import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_get"

    @property
    def description(self):
        return """Fetch an Existing Server"""

    def configure(self, parser):
        """Add arguments for server_get"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
    ):
        return sync(
            server_id=server_id,
            client=client,
        )
