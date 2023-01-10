from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.ssh_key.ssh_key_get import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.ssh_key_response import SshKeyResponse

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "get"

    @property
    def description(self):
        return """Fetch an Existing SSH Key"""

    def configure(self, parser):
        """Add arguments for ssh-key_get"""
        parser.cli_argument(
            "key_id",
            str,
            description="""The ID or fingerprint of the SSH Key to fetch.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return SshKeyResponse

    def request(
        self,
        key_id: str,
        client: Client,
    ) -> Union[Any, ProblemDetails, SshKeyResponse]:

        page_response = sync_detailed(
            key_id=key_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
