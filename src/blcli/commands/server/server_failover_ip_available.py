from typing import Any, Union

from ...client.api.server.server_failover_ip_available import sync_detailed
from ...client.client import Client
from ...client.models.failover_ips_response import FailoverIpsResponse
from ...client.models.problem_details import ProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_failover-ip_available"

    @property
    def description(self):
        return """Fetch a List of all Failover IPs that are Available to be Assigned to a Server"""

    def configure(self, parser):
        """Add arguments for server_failover-ip_available"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Union[Any, FailoverIpsResponse, ProblemDetails]:

        page = 0
        per_page = 25
        has_next = True
        response: FailoverIpsResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                server_id=server_id,
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
                response.failover_ips += page_response.parsed.failover_ips

        return response
