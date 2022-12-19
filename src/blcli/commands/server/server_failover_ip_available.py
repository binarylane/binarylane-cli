from ...client.api.server.server_failover_ip_available import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_failover-ip_available"

    @property
    def description(self):
        return """Fetch a List of all Failover IPs that are Available to be Assigned to a Server"""

    def configure(self, parser):
        """Add arguments for server_failover-ip_available"""
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
