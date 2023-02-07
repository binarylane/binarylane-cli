from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Dict, List, Optional, Tuple, Union

from binarylane.api.server_actions.get_v2_servers_server_id_actions import sync_detailed
from binarylane.models.actions_response import ActionsResponse
from binarylane.models.links import Links
from binarylane.models.problem_details import ProblemDetails

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
            "id",
            "type",
            "started_at",
            "completed_at",
            "resource_id",
            "status",
            "result_data",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "id": """The ID of this action.""",
            "status": """
| Value | Description |
| ----- | ----------- |
| in-progress | This action is currently in progress. |
| completed | This action has successfully completed. |
| errored | An error was encountered while processing the action. |

""",
            "type": """The type of this action.""",
            "started_at": """The timestamp in ISO8601 format of when processing of this action started.""",
            "progress": """Information about the current progress of the action. Some actions are divided into 'steps' and this may also contain information about the current and completed steps.""",
            "completed_at": """The timestamp in ISO8601 format of when processing of this action completed. If this value is null the action is currently in progress.""",
            "resource_type": """The resource type (if any) associated with this action. The resource type also determines which (if any) of the resource_id or resource_uuid fields are populated.""",
            "resource_id": """The resource id of the resource (if any) associated with this action. This is only populated when the resource type has an integer identifier.""",
            "resource_uuid": """The resource id of the resource (if any) associated with this action. This is only populated when the resource type has a UUID identifier.""",
            "region": """The region (if any) of the resource associated with this action.""",
            "region_slug": """The region slug (if any) of the resource associated with this action.""",
            "result_data": """Returned information from a completed action. For example: a successful completed 'ping' action will have the ping value in ms in this field.""",
            "blocking_invoice_id": """If this Action is currently blocked by an invoice that requires payment this property will be set.""",
            "user_interaction_required": """If this is not null the action is waiting on a response from the user.""",
        }

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """List All Actions for a Server"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/ServerActions/paths/~1v2~1servers~1%7Bserver_id%7D~1actions/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server for which actions should be listed.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return ActionsResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[ActionsResponse, None, ProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: ActionsResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page = 0
        per_page = 25
        has_next = True
        response: Optional[ActionsResponse] = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                server_id=request.server_id,
                client=client,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                return status_code, page_response.parsed

            assert isinstance(page_response.parsed, ActionsResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.actions += page_response.parsed.actions

        return status_code, response
