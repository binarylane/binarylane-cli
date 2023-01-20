from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.server.server_feature_list import sync_detailed
from binarylane.models.available_advanced_server_features_response import AvailableAdvancedServerFeaturesResponse
from binarylane.models.problem_details import ProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners import CommandRunner


class CommandRequest:
    server_id: int

    def __init__(self, server_id: int) -> None:
        self.server_id = server_id


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """Fetch the Currently Available Advanced Features for a Server"""

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server for which advanced features should be listed.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return AvailableAdvancedServerFeaturesResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, AvailableAdvancedServerFeaturesResponse, ProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: AvailableAdvancedServerFeaturesResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=request.server_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
