from __future__ import annotations

from http import HTTPStatus
from typing import Optional, Tuple, Union

from binarylane.api.server.server_failover_ip_get import sync_detailed
from binarylane.client import Client
from binarylane.models.failover_ips_response import FailoverIpsResponse
from binarylane.models.links import Links
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch the Failover IPs for a Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server_failover-ip_get"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The target server id.""",
        )

    @property
    def ok_response_type(self) -> type:
        return FailoverIpsResponse

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, FailoverIpsResponse, ProblemDetails]]:

        # HTTPStatus.OK: FailoverIpsResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page = 0
        per_page = 25
        has_next = True
        response: Optional[FailoverIpsResponse] = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                server_id=server_id,
                client=client,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                return status_code, page_response.parsed

            assert isinstance(page_response.parsed, FailoverIpsResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.failover_ips += page_response.parsed.failover_ips

        return status_code, response
