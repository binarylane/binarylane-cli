from typing import Any, Union

from ...client.api.vpc.vpc_delete import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...runners import CommandRunner


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
            type=int,
            description="""The target vpc id.""",
        )

    def request(
        self,
        vpc_id: int,
        client: Client,
    ) -> Union[Any, ProblemDetails]:

        return sync_detailed(
            vpc_id=vpc_id,
            client=client,
        ).parsed
