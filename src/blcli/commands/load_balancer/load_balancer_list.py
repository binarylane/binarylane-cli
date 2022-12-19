from ...client.api.load_balancer.load_balancer_list import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "load-balancer_list"

    @property
    def description(self):
        return """List all Load Balancers"""

    def configure(self, parser):
        """Add arguments for load-balancer_list"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
