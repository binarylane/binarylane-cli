from ...client.api.server_action.server_action_enable_ipv6 import sync
from ...client.client import Client
from ...client.models.enable_ipv_6 import EnableIpv6
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_enable-ipv6"

    @property
    def description(self):
        return """Enable IPv6 for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_enable-ipv6"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=EnableIpv6Type,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: EnableIpv6Type,
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=EnableIpv6(
                type=type,
            ),
        )
