from typing import Any, List, Union

from ...client.api.server.server_alert_list import sync_detailed
from ...client.client import Client
from ...client.models.current_server_alerts_response import CurrentServerAlertsResponse
from ...client.models.problem_details import ProblemDetails
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return []

    @property
    def name(self):
        return "server_alert_list"

    @property
    def description(self):
        return """List any Servers that have a Current Exceeded Threshold Alert"""

    def configure(self, parser):
        """Add arguments for server_alert_list"""

    def request(
        self,
        client: Client,
    ) -> Union[Any, CurrentServerAlertsResponse, ProblemDetails]:

        return sync_detailed(
            client=client,
        ).parsed
