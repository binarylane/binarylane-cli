from typing import Any, List, Union

from ...client.api.server.server_backup_list import sync_detailed
from ...client.client import Client
from ...client.models.backups_response import BackupsResponse
from ...client.models.problem_details import ProblemDetails
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "id",
            "name",
            "type",
            "public",
            "min_disk_size",
            "size_gigabytes",
            "status",
        ]

    @property
    def name(self):
        return "server_backup_list"

    @property
    def description(self):
        return """List All Backups for a Server"""

    def configure(self, parser):
        """Add arguments for server_backup_list"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Union[Any, BackupsResponse, ProblemDetails]:

        page = 0
        per_page = 25
        has_next = True
        response: BackupsResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                server_id=server_id,
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
                response.backups += page_response.parsed.backups

        return response
