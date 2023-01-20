from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.server_action.server_action_password_reset import sync_detailed
from binarylane.models.action_response import ActionResponse
from binarylane.models.password_reset import PasswordReset
from binarylane.models.password_reset_type import PasswordResetType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners import ActionRunner


class CommandRequest:
    server_id: int
    json_body: PasswordReset

    def __init__(self, server_id: int, json_body: PasswordReset) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "password-reset"

    @property
    def description(self) -> str:
        return """Reset the Password of a Server"""

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server on which the action should be performed.""",
        )

        json_body = mapping.add_json_body(PasswordReset)

        json_body.add_primitive(
            "type",
            PasswordResetType,
            option_name="type",
            required=True,
        )

        json_body.add_primitive(
            "username",
            Union[Unset, None, str],
            option_name="username",
            required=False,
            description="""The username of the user to change the password.
Only valid if the server supports password change actions (check server.password_change_supported via the servers endpoint).
If omitted and the server supports password change actions this will default to the username of the remote user that was configured when the server was created (normally 'root').""",
        )

        json_body.add_primitive(
            "send_password_via_email",
            Union[Unset, None, bool],
            option_name="send-password-via-email",
            required=False,
            description="""Send the new password via email. If you do not include this the new password will only be available by querying the action result within five minutes of the action being completed.""",
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
