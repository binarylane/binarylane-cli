from typing import Any, List, Union

from ...client.api.domain.domain_nameservers_list import sync_detailed
from ...client.client import Client
from ...client.models.local_nameservers_response import LocalNameserversResponse
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return []

    @property
    def name(self):
        return "domain_nameservers_list"

    @property
    def description(self):
        return """List All Public Nameservers"""

    def configure(self, parser):
        """Add arguments for domain_nameservers_list"""

    def request(
        self,
        client: Client,
    ) -> Union[Any, LocalNameserversResponse]:

        return sync_detailed(
            client=client,
        ).parsed
