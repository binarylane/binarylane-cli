from typing import Any, Union

from ...client.api.domain.domain_delete import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "domain_delete"

    @property
    def description(self):
        return """Delete an Existing Domain"""

    def configure(self, parser):
        """Add arguments for domain_delete"""
        parser.cli_argument(
            "domain_name",
            type=str,
        )

    def request(
        self,
        domain_name: str,
        client: Client,
    ) -> Union[Any, ProblemDetails]:

        return sync_detailed(
            domain_name=domain_name,
            client=client,
        ).parsed
