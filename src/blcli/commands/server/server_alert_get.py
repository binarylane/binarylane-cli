from typing import Any, Union

from ...client.api.server.server_alert_get import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.threshold_alerts_response import ThresholdAlertsResponse
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_alert_get"

    @property
    def description(self):
        return """Fetch the Currently Set Threshold Alerts for a Server"""

    def configure(self, parser):
        """Add arguments for server_alert_get"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Union[Any, ProblemDetails, ThresholdAlertsResponse]:

        return sync_detailed(
            server_id=server_id,
            client=client,
        ).parsed
