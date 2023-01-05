from typing import Union

from ...client.api.software.software_get import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.software_response import SoftwareResponse
from ...runners import CommandRunner


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

    def request(
        self,
        software_id: str,
        client: Client,
    ) -> Union[ProblemDetails, SoftwareResponse]:

        return sync_detailed(
            software_id=software_id,
            client=client,
        ).parsed
