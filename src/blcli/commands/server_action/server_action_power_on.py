from ...client.api.server_action.server_action_power_on import sync
from ...client.client import Client
from ...client.models.power_on import PowerOn
from ...client.models.power_on_type import PowerOnType
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_power-on"

    @property
    def description(self):
        return """Power a Server On"""

    def configure(self, parser):
        """Add arguments for server-action_power-on"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=PowerOnType,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: PowerOnType,
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=PowerOn(
                type=type,
            ),
        )
