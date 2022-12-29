from typing import Any, Dict, List, Union

from ...client.api.load_balancer.load_balancer_availability import sync_detailed
from ...client.client import Client
from ...client.models.load_balancer_availability_response import LoadBalancerAvailabilityResponse
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "anycast",
            "price_monthly",
            "price_hourly",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "anycast": """If true this is an Anycast load balancer option.""",
            "price_monthly": """Monthly Price in AU$.""",
            "price_hourly": """Hourly price in AU$.""",
            "regions": """The slugs of regions where this load balancer option is available. If this is an Anycast load balancer option this will be null.""",
        }

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
