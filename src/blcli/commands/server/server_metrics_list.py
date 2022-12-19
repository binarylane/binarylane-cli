from ...client.api.server.server_metrics_list import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_metrics_list"

    @property
    def description(self):
        return """Fetch all of the Performance and Usage Data Sample Sets for a Server"""

    def configure(self, parser):
        """Add arguments for server_metrics_list"""
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
