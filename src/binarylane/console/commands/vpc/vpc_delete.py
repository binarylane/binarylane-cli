from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.vpc.vpc_delete import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "delete"

    @property
    def description(self):
        return """Delete an Existing VPC"""

    def configure(self, parser):
        """Add arguments for vpc_delete"""
        parser.cli_argument(
            "vpc_id",
            int,
            description="""The target vpc id.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return type(None)

    def request(
        self,
        vpc_id: int,
        client: Client,
    ) -> Union[Any, ProblemDetails]:

        page_response = sync_detailed(
            vpc_id=vpc_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
