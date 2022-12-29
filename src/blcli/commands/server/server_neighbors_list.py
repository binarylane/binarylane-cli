from typing import Any, Dict, List, Union

from ...client.api.server.server_neighbors_list import sync_detailed
from ...client.client import Client
from ...client.models.neighbors_response import NeighborsResponse
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return []

    @property
    def fields(self) -> Dict[str, str]:
        return {}

    @property
    def name(self):
        return "server_neighbors_list"

    @property
    def description(self):
        return """List All Servers That Share a Host"""

    def configure(self, parser):
        """Add arguments for server_neighbors_list"""

    def request(
        self,
        client: Client,
    ) -> Union[Any, NeighborsResponse]:

        return sync_detailed(
            client=client,
        ).parsed
