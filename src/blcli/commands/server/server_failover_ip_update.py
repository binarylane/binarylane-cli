from typing import List

from ...client.api.server.server_failover_ip_update import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_failover-ip_update"

    @property
    def description(self):
        return """Sets the List of Failover IPs that are Assigned to a Server"""

    def configure(self, parser):
        """Add arguments for server_failover-ip_update"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "",
            nargs="*",
        )

    def request(self, server_id: int, client: Client, server: List[str]):
        return sync(
            server_id=server_id,
            client=client,
            json_body=server,
        )
