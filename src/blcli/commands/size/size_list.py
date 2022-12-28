from typing import List, Union

from ...client.api.size.size_list import sync_detailed
from ...client.client import Client
from ...client.models.sizes_response import SizesResponse
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "slug",
            "available",
            "price_monthly",
            "price_hourly",
            "disk",
            "memory",
            "transfer",
            "excess_transfer_cost_per_gigabyte",
            "vcpus",
            "vcpu_units",
        ]

    @property
    def name(self):
        return "size_list"

    @property
    def description(self):
        return """List All Available Sizes"""

    def configure(self, parser):
        """Add arguments for size_list"""

        parser.cli_argument(
            "--server-id",
            dest="server_id",
            type=Union[Unset, None, int],
            required=False,
            description="""None""",
        )
        parser.cli_argument(
            "--image",
            dest="image",
            type=Union[Unset, None, str],
            required=False,
            description="""None""",
        )

    def request(
        self,
        client: Client,
        server_id: Union[Unset, None, int] = UNSET,
        image: Union[Unset, None, str] = UNSET,
    ) -> Union[SizesResponse, ValidationProblemDetails]:

        page = 0
        per_page = 25
        has_next = True
        response: SizesResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                server_id=server_id,
                image=image,
                page=page,
                per_page=per_page,
            )

            if page_response.status_code != 200:
                return page_response.parsed

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.sizes += page_response.parsed.sizes

        return response
