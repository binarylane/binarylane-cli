from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.server_actions.post_v_2_servers_server_id_actions_password_reset import sync_detailed
from binarylane.models.action_response import ActionResponse
from binarylane.models.password_reset import PasswordReset
from binarylane.models.password_reset_type import PasswordResetType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.action import ActionRunner


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

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/ServerActions/paths/~1v2~1servers~1%7Bserver_id%7D~1actions#PasswordReset/post"

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
            "password",
            Union[Unset, None, str],
            option_name="password",
            required=False,
            description="""If this is provided the specified or default remote user's account password will be set to this value.
Only valid if the server supports password change actions (check server.password_change_supported via the servers endpoint).
If omitted and the server supports password change actions a random password will be generated and emailed to the account email address.""",
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
