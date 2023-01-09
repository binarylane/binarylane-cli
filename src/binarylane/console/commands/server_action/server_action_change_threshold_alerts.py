from __future__ import annotations

from typing import Any, List, Type, Union

from binarylane.api.server_action.server_action_change_threshold_alerts import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_threshold_alerts import ChangeThresholdAlerts
from binarylane.models.change_threshold_alerts_type import ChangeThresholdAlertsType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.threshold_alert_request import ThresholdAlertRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "change-threshold-alerts"

    @property
    def description(self):
        return """Set or Update the Threshold Alerts for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-threshold-alerts"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
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
            type=List["ThresholdAlertRequest"],
            required=True,
            description="""Any alert type not listed will not be updated.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeThresholdAlertsType,
        threshold_alerts: List["ThresholdAlertRequest"],
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeThresholdAlerts(
                type=type,
                threshold_alerts=threshold_alerts,
            ),
        )
        return page_response.status_code, page_response.parsed
