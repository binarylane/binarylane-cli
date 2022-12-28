from typing import List

from ...client.api.server_action.server_action_change_threshold_alerts import sync
from ...client.client import Client
from ...client.models.change_threshold_alerts import ChangeThresholdAlerts
from ...client.models.change_threshold_alerts_type import ChangeThresholdAlertsType
from ...client.models.threshold_alert_request import ThresholdAlertRequest
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_change-threshold-alerts"

    @property
    def description(self):
        return """Set or Update the Threshold Alerts for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-threshold-alerts"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ChangeThresholdAlertsType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--threshold-alerts",
            dest="threshold_alerts",
            type=List[ThresholdAlertRequest],
            required=True,
            description="""Any alert type not listed will not be updated.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeThresholdAlertsType,
        threshold_alerts: List[ThresholdAlertRequest],
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=ChangeThresholdAlerts(
                type=type,
                threshold_alerts=threshold_alerts,
            ),
        )
