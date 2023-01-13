from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server.server_alert_list import sync_detailed
from binarylane.client import Client
from binarylane.models.current_server_alerts_response import CurrentServerAlertsResponse
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """List any Servers that have a Current Exceeded Threshold Alert"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server_alert_list"""

    @property
    def ok_response_type(self) -> type:
        return CurrentServerAlertsResponse

    def request(
        self,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, CurrentServerAlertsResponse, ProblemDetails]]:

        # HTTPStatus.OK: CurrentServerAlertsResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
