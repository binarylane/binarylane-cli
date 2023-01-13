from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server.server_feature_list import sync_detailed
from binarylane.client import Client
from binarylane.models.available_advanced_server_features_response import AvailableAdvancedServerFeaturesResponse
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """Fetch the Currently Available Advanced Features for a Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server_feature_list"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server for which advanced features should be listed.""",
        )

    @property
    def ok_response_type(self) -> type:
        return AvailableAdvancedServerFeaturesResponse

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, AvailableAdvancedServerFeaturesResponse, ProblemDetails]]:

        # HTTPStatus.OK: AvailableAdvancedServerFeaturesResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=server_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
