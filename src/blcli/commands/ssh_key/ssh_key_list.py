from typing import Any, Union

from ...client.api.ssh_key.ssh_key_list import sync_detailed
from ...client.client import Client
from ...client.models.ssh_keys_response import SshKeysResponse
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "ssh-key_list"

    @property
    def description(self):
        return """List All SSH Keys"""

    def configure(self, parser):
        """Add arguments for ssh-key_list"""

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

            if page_response.status_code != 200:
                return page_response.parsed

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.ssh_keys += page_response.parsed.ssh_keys

        return response
