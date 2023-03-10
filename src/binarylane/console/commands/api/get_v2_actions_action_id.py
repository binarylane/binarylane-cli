from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.actions.get_v2_actions_action_id import sync_detailed
from binarylane.models.action_response import ActionResponse
from binarylane.models.problem_details import ProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    action_id: int

    def __init__(self, action_id: int) -> None:
        self.action_id = action_id


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch an Existing Action"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Actions/paths/~1v2~1actions~1%7Baction_id%7D/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "action_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the action to fetch.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[ActionResponse, None, ProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: ActionResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            action_id=request.action_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
