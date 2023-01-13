from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server.server_data_usage_get import sync_detailed
from binarylane.client import Client
from binarylane.models.data_usage_response import DataUsageResponse
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch the Current Data Usage (Transfer) for a Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server_data-usage_get"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The target server id.""",
        )

    @property
    def ok_response_type(self) -> type:
        return DataUsageResponse

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, DataUsageResponse, ProblemDetails]]:

        # HTTPStatus.OK: DataUsageResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=server_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
