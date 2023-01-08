from typing import Any, Type, Union

from ...client.api.domain.domain_record_delete import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "delete"

    @property
    def description(self):
        return """Delete an Existing Domain Record"""

    def configure(self, parser):
        """Add arguments for domain_record_delete"""
        parser.cli_argument(
            "domain_name",
            type=str,
            description="""The domain name for which the record should be deleted.""",
        )
        parser.cli_argument(
            "record_id",
            type=int,
            description="""The ID of the record to delete.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return type(None)

    def request(
        self,
        domain_name: str,
        record_id: int,
        client: Client,
    ) -> Union[Any, ProblemDetails]:

        page_response = sync_detailed(
            domain_name=domain_name,
            record_id=record_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
