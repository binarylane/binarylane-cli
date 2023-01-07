from typing import Any, Union

from ...client.api.server.server_alert_list import sync_detailed
from ...client.client import Client
from ...client.models.current_server_alerts_response import CurrentServerAlertsResponse
from ...client.models.problem_details import ProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "list"

    @property
    def description(self):
        return """List any Servers that have a Current Exceeded Threshold Alert"""

    def configure(self, parser):
        """Add arguments for server_alert_list"""

    def request(
        self,
        client: Client,
    ) -> Union[Any, CurrentServerAlertsResponse, ProblemDetails]:

        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
