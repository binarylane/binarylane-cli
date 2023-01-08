from typing import Any, Dict, List, Type, Union

from ...client.api.ssh_key.ssh_key_list import sync_detailed
from ...client.client import Client
from ...client.models.ssh_keys_response import SshKeysResponse
from ...runners import ListRunner


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
    def name(self):
        return "list"

    @property
    def description(self):
        return """List All SSH Keys"""

    def configure(self, parser):
        """Add arguments for ssh-key_list"""

    @property
    def ok_response_type(self) -> Type:
        return SshKeysResponse

    def request(
        self,
        client: Client,
    ) -> Union[Any, SshKeysResponse]:

        page = 0
        per_page = 25
        has_next = True
        response: SshKeysResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                response = page_response.parsed
                break

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.ssh_keys += page_response.parsed.ssh_keys

        return status_code, response
