from __future__ import annotations

from typing import Any, Dict, List, Type, Union

from binarylane.api.server.server_software import sync_detailed
from binarylane.client import Client
from binarylane.models.licensed_softwares_response import LicensedSoftwaresResponse
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "licence_count",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "software": """""",
            "licence_count": """The current licence count for the software.""",
        }

    @property
    def name(self):
        return "software"

    @property
    def description(self):
        return """List all Enabled Software for a Server"""

    def configure(self, parser):
        """Add arguments for server_software"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server for which software should be fetched.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return LicensedSoftwaresResponse

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Union[Any, LicensedSoftwaresResponse, ProblemDetails]:

        page = 0
        per_page = 25
        has_next = True
        response: LicensedSoftwaresResponse = None

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
                response = page_response.parsed
                break

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.licensed_software += page_response.parsed.licensed_software

        return status_code, response
