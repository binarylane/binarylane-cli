from typing import List, Union

from ...client.api.software.software_operating_system import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.softwares_response import SoftwaresResponse
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "id",
            "enabled",
            "name",
            "description",
            "cost_per_licence_per_month",
            "minimum_licence_count",
            "maximum_licence_count",
            "licence_step_count",
        ]

    @property
    def name(self):
        return "software_operating-system"

    @property
    def description(self):
        return """List All Available Software for an Existing Operating System"""

    def configure(self, parser):
        """Add arguments for software_operating-system"""
        parser.cli_argument(
            "operating_system_id_or_slug",
        )

    def request(
        self,
        operating_system_id_or_slug: str,
        client: Client,
    ) -> Union[ProblemDetails, SoftwaresResponse]:

        page = 0
        per_page = 25
        has_next = True
        response: SoftwaresResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                operating_system_id_or_slug=operating_system_id_or_slug,
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
                response.software += page_response.parsed.software

        return response
