from typing import Any, Union

from ... import cli
from ...client.api.ssh_key.ssh_key_create import sync_detailed
from ...client.client import Client
from ...client.models.ssh_key_request import SshKeyRequest
from ...client.models.ssh_key_response import SshKeyResponse
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runners import CommandRunner


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
