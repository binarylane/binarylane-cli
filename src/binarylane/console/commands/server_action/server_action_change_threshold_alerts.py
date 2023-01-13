from __future__ import annotations

from http import HTTPStatus
from typing import List, Tuple, Union

from binarylane.api.server_action.server_action_change_threshold_alerts import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_threshold_alerts import ChangeThresholdAlerts
from binarylane.models.change_threshold_alerts_type import ChangeThresholdAlertsType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.threshold_alert_request import ThresholdAlertRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "change-threshold-alerts"

    @property
    def description(self) -> str:
        return """Set or Update the Threshold Alerts for a Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server-action_change-threshold-alerts"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            ChangeThresholdAlertsType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--threshold-alerts",
            List[ThresholdAlertRequest],
            dest="threshold_alerts",
            required=True,
            description="""Any alert type not listed will not be updated.""",
        )

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeThresholdAlertsType,
        threshold_alerts: List[ThresholdAlertRequest],
    ) -> Tuple[HTTPStatus, Union[ActionResponse, None, ProblemDetails, ValidationProblemDetails]]:

        # HTTPStatus.OK: ActionResponse
        # HTTPStatus.ACCEPTED: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNPROCESSABLE_ENTITY: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeThresholdAlerts(
                type=type,
                threshold_alerts=threshold_alerts,
            ),
        )
        return page_response.status_code, page_response.parsed
