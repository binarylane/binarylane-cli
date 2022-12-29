from typing import Any, Dict, List, Union

from ...client.api.server.server_ipv6_ptr_ns_list import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.reverse_name_servers_response import ReverseNameServersResponse
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return []

    @property
    def fields(self) -> Dict[str, str]:
        return {}

    @property
    def name(self):
        return "server_ipv6-ptr-ns_list"

    @property
    def description(self):
        return """Fetch all Existing IPv6 Name Server Records"""

    def configure(self, parser):
        """Add arguments for server_ipv6-ptr-ns_list"""

    def request(
        self,
        client: Client,
    ) -> Union[Any, ProblemDetails, ReverseNameServersResponse]:

        page = 0
        per_page = 25
        has_next = True
        response: ReverseNameServersResponse = None

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
                response.reverse_nameservers += page_response.parsed.reverse_nameservers

        return response
