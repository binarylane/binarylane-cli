from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.server_actions.post_v_2_servers_server_id_actions_change_threshold_alerts import sync_detailed
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_threshold_alerts import ChangeThresholdAlerts
from binarylane.models.change_threshold_alerts_type import ChangeThresholdAlertsType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.threshold_alert_request import ThresholdAlertRequest
from binarylane.models.threshold_alert_type import ThresholdAlertType
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import ListAttribute, Mapping
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    server_id: int
    json_body: ChangeThresholdAlerts

    def __init__(self, server_id: int, json_body: ChangeThresholdAlerts) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "change-threshold-alerts"

    @property
    def description(self) -> str:
        return """Set or Update the Threshold Alerts for a Server"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/ServerActions/paths/~1v2~1servers~1%7Bserver_id%7D~1actions#ChangeThresholdAlerts/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server on which the action should be performed.""",
        )

        json_body = mapping.add_json_body(ChangeThresholdAlerts)

        json_body.add_primitive(
            "type",
            ChangeThresholdAlertsType,
            option_name="type",
            required=True,
        )

        json_body_threshold_alert_request = json_body.add(
            ListAttribute(
                "threshold_alerts",
                ThresholdAlertRequest,
                option_name="threshold-alerts",
                description="""Any alert type not listed will not be updated.""",
                required=True,
            )
        )

        json_body_threshold_alert_request.add_primitive(
            "alert_type",
            ThresholdAlertType,
            option_name="alert-type",
            required=True,
            description="""
| Value | Description |
| ----- | ----------- |
| cpu | The alert is based off the average percentage of all CPU; 100% is the maximum possible even with multiple processors. A high average will prevent the server from responding quickly. |
| storage-requests | The alert is based off The average number of requests (combined read and write) received by the storage subsystem. A high number of requests often indicates swap usage (due to memory exhaustion) and is associated with poor performance. |
| network-incoming | The alert is based off the amount of data going into the server (from the internet and the LAN). A sudden increase may indicate the server is the victim of a DOS attack. |
| network-outgoing | The alert is based off the amount of data coming out of the server (to the internet and the LAN). A sudden increase may indicate the server has been hacked and is being used for spam delivery. |
| data-transfer-used | The alert is based off the percentage of your monthly data transfer limit. |
| storage-used | The alert is based off the disk space consumed as a percentage of your total disk space. If the server runs out of disk space programs may fail to execute or be unable to create new files, or the server may become unresponsive. |
| memory-used | The alert is based off the virtual memory consumed as a percentage of your physical memory. Virtual memory includes the swap file so the percentage may exceed 100% indicating that the server has run out of physical memory and is relying on swap space, which will generally cause poor performance. |

""",
        )

        json_body_threshold_alert_request.add_primitive(
            "enabled",
            Union[Unset, None, bool],
            option_name="enabled",
            required=False,
            description="""Do not provide or leave null to keep existing status.""",
        )

        json_body_threshold_alert_request.add_primitive(
            "value",
            Union[Unset, None, int],
            option_name="value",
            required=False,
            description="""Do not provide or leave null to keep existing value.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[ActionResponse, None, ProblemDetails, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: ActionResponse
        # HTTPStatus.ACCEPTED: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNPROCESSABLE_ENTITY: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=request.server_id,
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
