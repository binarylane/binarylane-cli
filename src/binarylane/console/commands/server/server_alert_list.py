from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server.server_alert_list import sync_detailed
from binarylane.client import Client
from binarylane.models.current_server_alerts_response import CurrentServerAlertsResponse
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "list"

    @property
    def description(self):
        return """List any Servers that have a Current Exceeded Threshold Alert"""

    def configure(self, parser):
        """Add arguments for server_alert_list"""

    @property
    def ok_response_type(self) -> Type:
        return CurrentServerAlertsResponse

    def request(
        self,
        client: Client,
    ) -> Union[Any, CurrentServerAlertsResponse, ProblemDetails]:

        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
