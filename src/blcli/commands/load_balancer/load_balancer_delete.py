from ...client.api.load_balancer.load_balancer_delete import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "load-balancer_delete"

    @property
    def description(self):
        return """Cancel an Existing Load Balancer"""

    def configure(self, parser):
        """Add arguments for load-balancer_delete"""
        parser.cli_argument(
            "load_balancer_id",
        )

    def request(
        self,
        load_balancer_id: int,
        client: Client,
    ):
        return sync(
            load_balancer_id=load_balancer_id,
            client=client,
        )
