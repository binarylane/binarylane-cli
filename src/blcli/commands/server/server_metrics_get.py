from ...client.api.server.server_metrics_get import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_metrics_get"

    @property
    def description(self):
        return """Fetch the Latest Performance and Usage Data Sample Set for a Server"""

    def configure(self, parser):
        """Add arguments for server_metrics_get"""
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
