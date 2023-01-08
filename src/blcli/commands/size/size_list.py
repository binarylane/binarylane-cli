from typing import Dict, List, Type, Union

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
    def fields(self) -> Dict[str, str]:
        return {
            "slug": """The slug of this size.""",
            "size_type": """""",
            "available": """If this is false the size is not available for new servers.""",
            "regions": """A list of region slugs where this size is available regardless of stock.
If this a response to a query that included a selected operating system this response will only include regions where that operating system is available on this size,
otherwise not all regions listed will support all operating systems on this size.""",
            "price_monthly": """Monthly Price in AU$.""",
            "price_hourly": """Hourly price in AU$.""",
            "disk": """The included storage for this size in GB.""",
            "memory": """The included memory for this size in MB.""",
            "transfer": """The included data transfer for this size in TB.""",
            "excess_transfer_cost_per_gigabyte": """The excess charged for any transfer above the included data transfer in AU$ per GB.""",
            "vcpus": """The count of virtual CPUs for this size. See vcpu_units for a description of how each virtual CPU maps to the underlying hardware.""",
            "vcpu_units": """This is the unit that the vcpus field counts, e.g. "core" or "thread".""",
            "options": """Available add-ons (optional features not included in the base price) for the size. All costs are per month (pro-rated).""",
            "description": """A description of this size.""",
            "cpu_description": """A description of the CPU provided in this size.""",
            "storage_description": """A description of the storage provided in this size.""",
            "regions_out_of_stock": """A list of region slugs where the size is normally available but is currently not available due to lack of stock.""",
        }

    @property
    def name(self):
        return "list"

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
            description="""If supplied only sizes available for a resize the specified server will be returned. This parameter is only available when authenticated.""",
        )
        parser.cli_argument(
            "--image",
            dest="image",
            type=Union[Unset, None, str],
            required=False,
            description="""If null or not provided regions that support the size are included in the returned objects regardless of operating system. If this is provided it must be the id or slug of an operating system image and will cause only valid regions for the size and operating system to be included in the returned objects.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return SizesResponse

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

            status_code = page_response.status_code
            if status_code != 200:
                response = page_response.parsed
                break

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.sizes += page_response.parsed.sizes

        return status_code, response
