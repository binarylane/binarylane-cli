from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.keys.get_v2_account_keys_key_id import sync_detailed
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.ssh_key_response import SshKeyResponse

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    key_id: str

    def __init__(self, key_id: str) -> None:
        self.key_id = key_id


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch an Existing SSH Key"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Keys/paths/~1v2~1account~1keys~1%7Bkey_id%7D/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "key_id",
            str,
            required=True,
            option_name=None,
            description="""The ID or fingerprint of the SSH Key to fetch.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return SshKeyResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, SshKeyResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: SshKeyResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            key_id=request.key_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
