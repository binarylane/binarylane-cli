from typing import Any, Union

from ...client.api.load_balancer.load_balancer_list import sync_detailed
from ...client.client import Client
from ...client.models.load_balancers_response import LoadBalancersResponse
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
