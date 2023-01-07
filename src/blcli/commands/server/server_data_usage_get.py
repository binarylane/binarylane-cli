from typing import Any, Union

from ...client.api.server.server_data_usage_get import sync_detailed
from ...client.client import Client
from ...client.models.data_usage_response import DataUsageResponse
from ...client.models.problem_details import ProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "get"

    @property
    def description(self):
        return """Fetch the Current Data Usage (Transfer) for a Server"""

    def configure(self, parser):
        """Add arguments for server_data-usage_get"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The target server id.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Union[Any, DataUsageResponse, ProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
