from ...client.api.server_action.server_action_ping import sync
from ...client.client import Client
from ...client.models.ping import Ping
from ...client.models.ping_type import PingType
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_ping"

    @property
    def description(self):
        return """Attempt to Ping a Server"""

    def configure(self, parser):
        """Add arguments for server-action_ping"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=PingType,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: PingType,
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=Ping(
                type=type,
            ),
        )
