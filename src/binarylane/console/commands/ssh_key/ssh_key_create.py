from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.ssh_key.ssh_key_create import sync_detailed
from binarylane.client import Client
from binarylane.models.ssh_key_request import SshKeyRequest
from binarylane.models.ssh_key_response import SshKeyResponse
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console import cli
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "create"

    @property
    def description(self):
        return """Add a New SSH Key"""

    def configure(self, parser):
        """Add arguments for ssh-key_create"""

        parser.cli_argument(
            "--public-key",
            dest="public_key",
            type=str,
            required=True,
            description="""The public key in OpenSSH "authorized_keys" format.""",
        )

        parser.cli_argument(
            "--name",
            dest="name",
            type=str,
            required=True,
            description="""A name to help you identify the key.""",
        )

        parser.cli_argument(
            "--default",
            dest="default",
            type=Union[Unset, None, bool],
            required=False,
            description="""Optional: If true this will be added to all new server installations (if we support SSH Key injection for the server's operating system).""",
            action=cli.BooleanOptionalAction,
        )

    @property
    def ok_response_type(self) -> Type:
        return SshKeyResponse

    def request(
        self,
        client: Client,
        public_key: str,
        name: str,
        default: Union[Unset, None, bool] = UNSET,
    ) -> Union[Any, SshKeyResponse, ValidationProblemDetails]:

        page_response = sync_detailed(
            client=client,
            json_body=SshKeyRequest(
                public_key=public_key,
                name=name,
                default=default,
            ),
        )
        return page_response.status_code, page_response.parsed
