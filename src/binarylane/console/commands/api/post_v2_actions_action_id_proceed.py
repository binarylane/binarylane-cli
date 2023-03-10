from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.actions.post_v2_actions_action_id_proceed import sync_detailed
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.proceed_request import ProceedRequest

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    action_id: int
    json_body: ProceedRequest

    def __init__(self, action_id: int, json_body: ProceedRequest) -> None:
        self.action_id = action_id
        self.json_body = json_body


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "proceed"

    @property
    def description(self) -> str:
        return """Respond to a UserInteractionRequired Action"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Actions/paths/~1v2~1actions~1%7Baction_id%7D~1proceed/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "action_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the action for which this is a response.""",
        )

        json_body = mapping.add_json_body(ProceedRequest)

        json_body.add_primitive(
            "proceed",
            bool,
            option_name="proceed",
            required=True,
            description="""Please see the documentation for each type of interaction for the effect of providing 'true' or 'false' here.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return type(None)

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            action_id=request.action_id,
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
