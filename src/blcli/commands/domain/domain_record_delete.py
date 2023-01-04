from typing import Any, Union

from ...client.api.domain.domain_record_delete import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "domain_record_delete"

    @property
    def description(self):
        return """Delete an Existing Domain Record"""

    def configure(self, parser):
        """Add arguments for domain_record_delete"""
        parser.cli_argument(
            "domain_name",
            type=str,
        )
        parser.cli_argument(
            "record_id",
            type=int,
        )

    def request(
        self,
        domain_name: str,
        record_id: int,
        client: Client,
    ) -> Union[Any, ProblemDetails]:

        return sync_detailed(
            domain_name=domain_name,
            record_id=record_id,
            client=client,
        ).parsed
