from __future__ import annotations

from typing import Any, Dict, List, Type, Union

from binarylane.api.load_balancer.load_balancer_availability import sync_detailed
from binarylane.client import Client
from binarylane.models.load_balancer_availability_response import LoadBalancerAvailabilityResponse

from binarylane.console.runners import ListRunner


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
        return "availability"

    @property
    def description(self):
        return """Fetch Load Balancer Availability and Pricing"""

    def configure(self, parser):
        """Add arguments for load-balancer_availability"""

    @property
    def ok_response_type(self) -> Type:
        return LoadBalancerAvailabilityResponse

    def request(
        self,
        client: Client,
    ) -> Union[Any, LoadBalancerAvailabilityResponse]:

        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
