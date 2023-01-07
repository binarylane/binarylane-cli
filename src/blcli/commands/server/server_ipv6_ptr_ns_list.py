from typing import Any, Union

from ...client.api.server.server_ipv6_ptr_ns_list import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.reverse_name_servers_response import ReverseNameServersResponse
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "list"

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

            status_code = page_response.status_code
            if status_code != 200:
                response = page_response.parsed
                break

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.reverse_nameservers += page_response.parsed.reverse_nameservers

        return status_code, response
