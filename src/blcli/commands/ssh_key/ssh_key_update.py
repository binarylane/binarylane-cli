from typing import Any, Union

from ... import cli
from ...client.api.ssh_key.ssh_key_update import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.ssh_key_response import SshKeyResponse
from ...client.models.update_ssh_key_request import UpdateSshKeyRequest
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runners import CommandRunner


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
            type=str,
            description="""The ID or fingerprint of the SSH Key to update.""",
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
            description="""Do not provide or leave null to leave the default status of the key unchanged.
Optional: If true this will be added to all new server installations (if we support SSH Key injection for the server's operating system).""",
            action=cli.BooleanOptionalAction,
        )

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
