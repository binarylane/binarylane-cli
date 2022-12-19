from ...client.api.server.server_user_data import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_user-data"

    @property
    def description(self):
        return """Fetch the Currently Set UserData for a Server"""

    def configure(self, parser):
        """Add arguments for server_user-data"""
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
