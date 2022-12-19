from typing import List

from ...client.api.load_balancer.load_balancer_server_delete import sync
from ...client.client import Client
from ...client.models.server_ids_request import ServerIdsRequest
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "load-balancer_server_delete"

    @property
    def description(self):
        return """Remove Servers from an Existing Load Balancer"""

    def configure(self, parser):
        """Add arguments for load-balancer_server_delete"""
        parser.cli_argument(
            "load_balancer_id",
        )

        parser.cli_argument(
            "--server-ids",
            dest="server_ids",
            type=List[int],
            required=True,
            description="""None""",
        )

    def request(
        self,
        load_balancer_id: int,
        client: Client,
        server_ids: List[int],
    ):
        return sync(
            load_balancer_id=load_balancer_id,
            client=client,
            json_body=ServerIdsRequest(
                server_ids=server_ids,
            ),
        )
