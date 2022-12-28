from typing import Any, Union

from ...client.api.vpc.vpc_get import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.vpc_response import VpcResponse
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "vpc_get"

    @property
    def description(self):
        return """Fetch an Existing VPC"""

    def configure(self, parser):
        """Add arguments for vpc_get"""
        parser.cli_argument(
            "vpc_id",
            description="""The target vpc id.""",
        )

    def request(
        self,
        vpc_id: int,
        client: Client,
    ) -> Union[Any, ProblemDetails, VpcResponse]:

        return sync_detailed(
            vpc_id=vpc_id,
            client=client,
        ).parsed
