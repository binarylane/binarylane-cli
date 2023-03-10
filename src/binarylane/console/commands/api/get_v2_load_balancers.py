from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Dict, List, Optional, Tuple, Union

from binarylane.api.load_balancers.get_v2_load_balancers import sync_detailed
from binarylane.models.links import Links
from binarylane.models.load_balancers_response import LoadBalancersResponse

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
            "id",
            "name",
            "region",
            "ip",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "id": """The ID of the load balancer.""",
            "name": """The hostname of the load balancer.""",
            "ip": """The IPv4 address of the load balancer.""",
            "status": """
| Value | Description |
| ----- | ----------- |
| new | The load balancer is currently being built and is not ready to accept connections. |
| active | The load balancer is available. |
| errored | The load balancer is in an errored state. |

""",
            "created_at": """The date and time in ISO8601 format of the creation of the load balancer.""",
            "forwarding_rules": """The rules that control which traffic the load balancer will forward to servers in the pool.""",
            "health_check": """The rules that determine which servers are considered 'healthy' and in the server pool for the load balancer.""",
            "server_ids": """The server IDs of the servers that are currently in the load balancer pool (regardless of their current 'health').""",
            "region": """The region the load balancer is located in. If this value is null the load balancer is an 'AnyCast' load balancer.""",
        }

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """List all Load Balancers"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/LoadBalancers/paths/~1v2~1load_balancers/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)
        return mapping

    @property
    def ok_response_type(self) -> type:
        return LoadBalancersResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, LoadBalancersResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: LoadBalancersResponse
        # HTTPStatus.UNAUTHORIZED: Any
        page = 0
        per_page = 25
        has_next = True
        response: Optional[LoadBalancersResponse] = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                return status_code, page_response.parsed

            assert isinstance(page_response.parsed, LoadBalancersResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.load_balancers += page_response.parsed.load_balancers

        return status_code, response
