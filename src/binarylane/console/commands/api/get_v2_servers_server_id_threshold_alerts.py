from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Dict, List, Tuple, Union

from binarylane.api.servers.get_v2_servers_server_id_threshold_alerts import sync_detailed
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.threshold_alerts_response import ThresholdAlertsResponse

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.list import ListRunner


class CommandRequest:
    server_id: int

    def __init__(self, server_id: int) -> None:
        self.server_id = server_id


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "alert_type",
            "enabled",
            "value",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "alert_type": """
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
            "enabled": """If a threshold alert is not enabled it will not generate warnings for the user.""",
            "value": """The threshold value of the alert. Refer to the documentation for each threshold alert type for what this value measures in the context of the alert type.""",
            "current_value": """The last measured value for this alert type over the threshold alert period. Refer to the documentation for each threshold alert type for what this value measures in the context of the alert type. If there is no measured value in the threshold alert period this will be null.""",
            "last_raised": """The date and time (if any) in ISO8601 format of the last time this alert was raised. An alert may not be raised again until it has been cleared.""",
            "last_cleared": """The date and time (if any) in ISO8601 format of the last time this alert was cleared. An alert may not be raised again until a minimum duration has passed since it was last cleared.""",
        }

    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch the Currently Set Threshold Alerts for a Server"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Servers/paths/~1v2~1servers~1%7Bserver_id%7D~1threshold_alerts/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server for which threshold alerts should be fetched.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return ThresholdAlertsResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, ThresholdAlertsResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: ThresholdAlertsResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=request.server_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
