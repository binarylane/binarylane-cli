from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.ssh_key.ssh_key_update import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.ssh_key_response import SshKeyResponse
from binarylane.models.update_ssh_key_request import UpdateSshKeyRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.actions import BooleanOptionalAction
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "update"

    @property
    def description(self):
        return """Update an Existing SSH Key"""

    def configure(self, parser):
        """Add arguments for ssh-key_update"""
        parser.cli_argument(
            "key_id",
            str,
            description="""The ID or fingerprint of the SSH Key to update.""",
        )

        parser.cli_argument(
            "--name",
            str,
            dest="name",
            required=True,
            description="""A name to help you identify the key.""",
        )

        parser.cli_argument(
            "--default",
            Union[Unset, None, bool],
            dest="default",
            required=False,
            description="""Do not provide or leave null to leave the default status of the key unchanged.
Optional: If true this will be added to all new server installations (if we support SSH Key injection for the server's operating system).""",
            action=BooleanOptionalAction,
        )

    @property
    def ok_response_type(self) -> Type:
        return SshKeyResponse

    def request(
        self,
        key_id: str,
        client: Client,
        name: str,
        default: Union[Unset, None, bool] = UNSET,
    ) -> Union[Any, ProblemDetails, SshKeyResponse, ValidationProblemDetails]:

        page_response = sync_detailed(
            key_id=key_id,
            client=client,
            json_body=UpdateSshKeyRequest(
                name=name,
                default=default,
            ),
        )
        return page_response.status_code, page_response.parsed
