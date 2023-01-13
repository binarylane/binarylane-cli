from __future__ import annotations

from http import HTTPStatus
from typing import Dict, List, Optional, Tuple, Union

from binarylane.api.ssh_key.ssh_key_list import sync_detailed
from binarylane.client import Client
from binarylane.models.links import Links
from binarylane.models.ssh_keys_response import SshKeysResponse

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "id",
            "fingerprint",
            "public_key",
            "default",
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

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for ssh-key_list"""

    @property
    def ok_response_type(self) -> type:
        return SshKeysResponse

    def request(
        self,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, SshKeysResponse]]:

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
