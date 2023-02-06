from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Dict, List, Optional, Tuple, Union

from binarylane.api.keys.get_v2_account_keys import sync_detailed
from binarylane.models.links import Links
from binarylane.models.ssh_keys_response import SshKeysResponse

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.list import ListRunner


class CommandRequest:
    pass


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "id",
            "name",
            "default",
            "fingerprint",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "id": """The ID of this SSH key.""",
            "fingerprint": """The fingerprint of this SSH key.""",
            "public_key": """The public key of this SSH key.""",
            "default": """If an SSH key is marked as default it will be deployed to all newly created servers that support SSH keys unless expressly overridden in the creation request.""",
            "name": """The name of this SSH key. This is used only to aid in identification.""",
        }

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """List All SSH Keys"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Keys/paths/~1v2~1account~1keys/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)
        return mapping

    @property
    def ok_response_type(self) -> type:
        return SshKeysResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, SshKeysResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: SshKeysResponse
        # HTTPStatus.UNAUTHORIZED: Any
        page = 0
        per_page = 25
        has_next = True
        response: Optional[SshKeysResponse] = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                return status_code, page_response.parsed

            assert isinstance(page_response.parsed, SshKeysResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.ssh_keys += page_response.parsed.ssh_keys

        return status_code, response
