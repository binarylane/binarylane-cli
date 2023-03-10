from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.keys.put_v2_account_keys_key_id import sync_detailed
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.ssh_key_response import SshKeyResponse
from binarylane.models.update_ssh_key_request import UpdateSshKeyRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    key_id: str
    json_body: UpdateSshKeyRequest

    def __init__(self, key_id: str, json_body: UpdateSshKeyRequest) -> None:
        self.key_id = key_id
        self.json_body = json_body


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "update"

    @property
    def description(self) -> str:
        return """Update an Existing SSH Key"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Keys/paths/~1v2~1account~1keys~1%7Bkey_id%7D/put"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "key_id",
            str,
            required=True,
            option_name=None,
            description="""The ID or fingerprint of the SSH Key to update.""",
        )

        json_body = mapping.add_json_body(UpdateSshKeyRequest)

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
            description="""Do not provide or leave null to leave the default status of the key unchanged.
Optional: If true this will be added to all new server installations (if we support SSH Key injection for the server's operating system).""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return SshKeyResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, SshKeyResponse, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: SshKeyResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            key_id=request.key_id,
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
