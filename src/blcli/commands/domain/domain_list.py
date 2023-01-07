from typing import Any, Dict, List, Union

from ...client.api.domain.domain_list import sync_detailed
from ...client.client import Client
from ...client.models.domains_response import DomainsResponse
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "name",
            "zone_file",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "name": """The name of the domain.""",
            "current_nameservers": """The current authoritative name servers for this domain.""",
            "zone_file": """The zone file for the selected domain. If the DNS records for this domain are not managed locally this is what the zone file would be if the authority was delegated to us.""",
            "ttl": """The time to live for records in this domain in seconds. If the DNS records for this domain are not managed locally this will be what the TTL would be if the authority was delegated to us.""",
        }

    @property
    def name(self):
        return "list"

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

            status_code = page_response.status_code
            if status_code != 200:
                response = page_response.parsed
                break

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.domains += page_response.parsed.domains

        return status_code, response
