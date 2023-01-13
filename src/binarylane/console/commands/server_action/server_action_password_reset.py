from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server_action.server_action_password_reset import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.password_reset import PasswordReset
from binarylane.models.password_reset_type import PasswordResetType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.actions import BooleanOptionalAction
from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "password-reset"

    @property
    def description(self) -> str:
        return """Reset the Password of a Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server-action_password-reset"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            PasswordResetType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--username",
            Union[Unset, None, str],
            dest="username",
            required=False,
            description="""The username of the user to change the password.
Only valid if the server supports password change actions (check server.password_change_supported via the servers endpoint).
If omitted and the server supports password change actions this will default to the username of the remote user that was configured when the server was created (normally 'root').""",
        )

        parser.cli_argument(
            "--send-password-via-email",
            Union[Unset, None, bool],
            dest="send_password_via_email",
            required=False,
            description="""Send the new password via email. If you do not include this the new password will only be available by querying the action result within five minutes of the action being completed.""",
            action=BooleanOptionalAction,
        )

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: PasswordResetType,
        username: Union[Unset, None, str] = UNSET,
        send_password_via_email: Union[Unset, None, bool] = UNSET,
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
            json_body=PasswordReset(
                type=type,
                username=username,
                send_password_via_email=send_password_via_email,
            ),
        )
        return page_response.status_code, page_response.parsed
