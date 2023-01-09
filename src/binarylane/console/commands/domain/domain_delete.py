from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.domain.domain_delete import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "delete"

    @property
    def description(self):
        return """Delete an Existing Domain"""

    def configure(self, parser):
        """Add arguments for domain_delete"""
        parser.cli_argument(
            "domain_name",
            type=str,
            description="""The name of the domain to delete.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return type(None)

    def request(
        self,
        domain_name: str,
        client: Client,
    ) -> Union[Any, ProblemDetails]:

        page_response = sync_detailed(
            domain_name=domain_name,
            client=client,
        )
        return page_response.status_code, page_response.parsed
