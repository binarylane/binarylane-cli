from typing import Any, Union

from ...client.api.ssh_key.ssh_key_get import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.ssh_key_response import SshKeyResponse
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "ssh-key_get"

    @property
    def description(self):
        return """Fetch an Existing SSH Key"""

    def configure(self, parser):
        """Add arguments for ssh-key_get"""
        parser.cli_argument(
            "key_id",
        )

    def request(
        self,
        key_id: str,
        client: Client,
    ) -> Union[Any, ProblemDetails, SshKeyResponse]:

        return sync_detailed(
            key_id=key_id,
            client=client,
        ).parsed
