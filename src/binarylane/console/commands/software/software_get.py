from __future__ import annotations

from typing import Type, Union

from binarylane.api.software.software_get import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.software_response import SoftwareResponse

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "get"

    @property
    def description(self):
        return """Fetch Existing Software"""

    def configure(self, parser):
        """Add arguments for software_get"""
        parser.cli_argument(
            "software_id",
            type=str,
            description="""The ID of the software to fetch.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return SoftwareResponse

    def request(
        self,
        software_id: str,
        client: Client,
    ) -> Union[ProblemDetails, SoftwareResponse]:

        page_response = sync_detailed(
            software_id=software_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
