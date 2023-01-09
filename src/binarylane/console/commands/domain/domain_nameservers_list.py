from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.domain.domain_nameservers_list import sync_detailed
from binarylane.client import Client
from binarylane.models.local_nameservers_response import LocalNameserversResponse

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "list"

    @property
    def description(self):
        return """List All Public Nameservers"""

    def configure(self, parser):
        """Add arguments for domain_nameservers_list"""

    @property
    def ok_response_type(self) -> Type:
        return LocalNameserversResponse

    def request(
        self,
        client: Client,
    ) -> Union[Any, LocalNameserversResponse]:

        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
