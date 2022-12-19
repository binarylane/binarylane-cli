from ...client.api.server_action.server_action_power_cycle import sync
from ...client.client import Client
from ...client.models.power_cycle import PowerCycle
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_power-cycle"

    @property
    def description(self):
        return """Power a Server Off and then On"""

    def configure(self, parser):
        """Add arguments for server-action_power-cycle"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=PowerCycleType,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: PowerCycleType,
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=PowerCycle(
                type=type,
            ),
        )
