from ...client.api.load_balancer.load_balancer_availability import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "load-balancer_availability"

    @property
    def description(self):
        return """Fetch Load Balancer Availability and Pricing"""

    def configure(self, parser):
        """Add arguments for load-balancer_availability"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
