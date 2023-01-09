from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server_action.server_action_password_reset import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.password_reset import PasswordReset
from binarylane.models.password_reset_type import PasswordResetType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console import cli
from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "password-reset"

    @property
    def description(self):
        return """Reset the Password of a Server"""

    def configure(self, parser):
        """Add arguments for server-action_password-reset"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=PasswordResetType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--username",
            dest="username",
            type=Union[Unset, None, str],
            required=False,
            description="""The username of the user to change the password.
Only valid if the server supports password change actions (check server.password_change_supported via the servers endpoint).
If omitted and the server supports password change actions this will default to the username of the remote user that was configured when the server was created (normally 'root').""",
        )

        parser.cli_argument(
            "--send-password-via-email",
            dest="send_password_via_email",
            type=Union[Unset, None, bool],
            required=False,
            description="""Send the new password via email. If you do not include this the new password will only be available by querying the action result within five minutes of the action being completed.""",
            action=cli.BooleanOptionalAction,
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: PasswordResetType,
        username: Union[Unset, None, str] = UNSET,
        send_password_via_email: Union[Unset, None, bool] = UNSET,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

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
