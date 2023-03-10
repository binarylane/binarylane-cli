from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Dict, List, Tuple, Union

from binarylane.api.load_balancers.get_v2_load_balancers_availability import sync_detailed
from binarylane.models.load_balancer_availability_response import LoadBalancerAvailabilityResponse

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.list import ListRunner


class CommandRequest:
    pass


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
    def name(self) -> str:
        return "availability"

    @property
    def description(self) -> str:
        return """Fetch Load Balancer Availability and Pricing"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/LoadBalancers/paths/~1v2~1load_balancers~1availability/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)
        return mapping

    @property
    def ok_response_type(self) -> type:
        return LoadBalancerAvailabilityResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, LoadBalancerAvailabilityResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: LoadBalancerAvailabilityResponse
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
