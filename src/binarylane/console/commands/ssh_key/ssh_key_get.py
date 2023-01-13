from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.ssh_key.ssh_key_get import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.ssh_key_response import SshKeyResponse

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch an Existing SSH Key"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for ssh-key_get"""
        parser.cli_argument(
            "key_id",
            str,
            description="""The ID or fingerprint of the SSH Key to fetch.""",
        )

    @property
    def ok_response_type(self) -> type:
        return SshKeyResponse

    def request(
        self,
        key_id: str,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, SshKeyResponse]]:

        # HTTPStatus.OK: SshKeyResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            key_id=key_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
