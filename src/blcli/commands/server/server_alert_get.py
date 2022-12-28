from typing import Any, List, Union

from ...client.api.server.server_alert_get import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.threshold_alerts_response import ThresholdAlertsResponse
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "alert_type",
            "enabled",
            "value",
        ]

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
