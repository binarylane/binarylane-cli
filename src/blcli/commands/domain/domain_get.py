from typing import Any, Union

from ...client.api.domain.domain_get import sync_detailed
from ...client.client import Client
from ...client.models.domain_response import DomainResponse
from ...client.models.problem_details import ProblemDetails
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "domain_get"

    @property
    def description(self):
        return """Fetch an Existing Domain"""

    def configure(self, parser):
        """Add arguments for domain_get"""
        parser.cli_argument(
            "domain_name",
        )

    def request(
        self,
        domain_name: str,
        client: Client,
    ) -> Union[Any, DomainResponse, ProblemDetails]:

        return sync_detailed(
            domain_name=domain_name,
            client=client,
        ).parsed
