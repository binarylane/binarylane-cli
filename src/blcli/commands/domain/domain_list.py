from typing import Any, Union

from ...client.api.domain.domain_list import sync_detailed
from ...client.client import Client
from ...client.models.domains_response import DomainsResponse
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "domain_list"

    @property
    def description(self):
        return """List All Domains"""

    def configure(self, parser):
        """Add arguments for domain_list"""

    def request(
        self,
        client: Client,
    ) -> Union[Any, DomainsResponse, ProblemDetails, ValidationProblemDetails]:

        page = 0
        per_page = 25
        has_next = True
        response: DomainsResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
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
                response.domains += page_response.parsed.domains

        return response
