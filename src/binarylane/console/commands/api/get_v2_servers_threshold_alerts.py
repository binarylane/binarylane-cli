from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.servers.get_v2_servers_threshold_alerts import sync_detailed
from binarylane.models.current_server_alerts_response import CurrentServerAlertsResponse
from binarylane.models.problem_details import ProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    pass


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """List any Servers that have a Current Exceeded Threshold Alert"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Servers/paths/~1v2~1servers~1threshold_alerts/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)
        return mapping

    @property
    def ok_response_type(self) -> type:
        return CurrentServerAlertsResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, CurrentServerAlertsResponse, ProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: CurrentServerAlertsResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
