from typing import Any, List, Union

from ...client.api.server.server_neighbors_get import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.server_neighbors_response import ServerNeighborsResponse
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "id",
            "name",
            "memory",
            "vcpus",
            "disk",
            "locked",
            "created_at",
            "status",
            "size_slug",
            "password_change_supported",
        ]

    @property
    def name(self):
        return "server_neighbors_get"

    @property
    def description(self):
        return """List All Servers That Share a Host with a Server"""

    def configure(self, parser):
        """Add arguments for server_neighbors_get"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Union[Any, ProblemDetails, ServerNeighborsResponse]:

        return sync_detailed(
            server_id=server_id,
            client=client,
        ).parsed
