from typing import Any, Dict, List, Union

from ...client.api.load_balancer.load_balancer_list import sync_detailed
from ...client.client import Client
from ...client.models.load_balancers_response import LoadBalancersResponse
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "id",
            "name",
            "ip",
            "status",
            "created_at",
            "algorithm",
            "redirect_http_to_https",
            "enable_proxy_protocol",
            "enable_backend_keepalive",
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
            "health_check": """""",
            "sticky_sessions": """""",
            "server_ids": """The server IDs of the servers that are currently in the load balancer pool (regardless of their current 'health').""",
            "algorithm": """
| Value | Description |
| ----- | ----------- |
| round_robin | Each request will be sent to one of the nominated servers in turn. |
| least_connections | Each request will be sent to the server with the least existing connections. This option is not currently supported. |

""",
            "redirect_http_to_https": """Whether to redirect HTTP traffic received by the load balancer to HTTPS. This is not currently supported.""",
            "enable_proxy_protocol": """Whether the PROXY protocol is enabled on the load balancer. This is not currently supported.""",
            "enable_backend_keepalive": """Whether to use HTTP keepalive connections to servers in the load balancer pool. This is not currently supported.""",
            "region": """""",
            "tag": """Adding servers by tag is currently not supported and this value will always be null.""",
            "vpc_id": """The VPC ID of the VPC the load balancer is assigned to. This is not currently supported: all load balancers are either in the default (public) network for the region or are 'AnyCast' load balancers.""",
        }

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
    ) -> Union[Any, LoadBalancersResponse]:

        page = 0
        per_page = 25
        has_next = True
        response: LoadBalancersResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                page=page,
                per_page=per_page,
            )

            if page_response.status_code != 200:
                return page_response.parsed

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.load_balancers += page_response.parsed.load_balancers

        return response
