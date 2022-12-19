from ...client.api.server.server_action_get import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_action_get"

    @property
    def description(self):
        return """Fetch an Action for a Server"""

    def configure(self, parser):
        """Add arguments for server_action_get"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )
        parser.cli_argument(
            "action_id",
        )

    def request(
        self,
        server_id: int,
        action_id: int,
        client: Client,
    ):
        return sync(
            server_id=server_id,
            action_id=action_id,
            client=client,
        )
