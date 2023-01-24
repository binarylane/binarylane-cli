from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.keys.post_v2_account_keys import sync_detailed
from binarylane.models.ssh_key_request import SshKeyRequest
from binarylane.models.ssh_key_response import SshKeyResponse
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    json_body: SshKeyRequest

    def __init__(self, json_body: SshKeyRequest) -> None:
        self.json_body = json_body


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "create"

    @property
    def description(self) -> str:
        return """Add a New SSH Key"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Keys/paths/~1v2~1account~1keys/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        json_body = mapping.add_json_body(SshKeyRequest)

        json_body.add_primitive(
            "public_key",
            str,
            option_name="public-key",
            required=True,
            description="""The public key in OpenSSH "authorized_keys" format.""",
        )

        json_body.add_primitive(
            "name",
            str,
            option_name="name",
            required=True,
            description="""A name to help you identify the key.""",
        )

        json_body.add_primitive(
            "default",
            Union[Unset, None, bool],
            option_name="default",
            required=False,
            description="""Optional: If true this will be added to all new server installations (if we support SSH Key injection for the server's operating system).""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return SshKeyResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, SshKeyResponse, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: SshKeyResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
