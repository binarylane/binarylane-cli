from typing import Any, Union

from ...client.api.load_balancer.load_balancer_availability import sync_detailed
from ...client.client import Client
from ...client.models.load_balancer_availability_response import LoadBalancerAvailabilityResponse
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
    ) -> Union[Any, LoadBalancerAvailabilityResponse]:

        return sync_detailed(
            client=client,
        ).parsed
