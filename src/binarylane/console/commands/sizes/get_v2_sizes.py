from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Dict, List, Optional, Tuple, Union

from binarylane.api.sizes.get_v2_sizes import sync_detailed
from binarylane.models.links import Links
from binarylane.models.sizes_response import SizesResponse
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.list import ListRunner


class CommandRequest:
    server_id: Union[Unset, None, int] = UNSET
    image: Union[Unset, None, str] = UNSET


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "slug",
            "size_type",
            "vcpus",
            "vcpu_units",
            "memory",
            "disk",
            "transfer",
            "price_monthly",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "slug": """The slug of this size.""",
            "size_type": """The type of this size, generally used to differentiate sizes optimized for different usages.""",
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
            "options": """Available add-ons (optional features not included in the base price) for the size. All costs are in AU$ per month (pro-rated).""",
            "description": """A description of this size.""",
            "cpu_description": """A description of the CPU provided in this size.""",
            "storage_description": """A description of the storage provided in this size.""",
            "regions_out_of_stock": """A list of region slugs where the size is normally available but is currently not available due to lack of stock.""",
        }

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """List All Available Sizes"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Sizes/paths/~1v2~1sizes/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            Union[Unset, None, int],
            required=False,
            option_name="server-id",
            description="""If supplied only sizes available for a resize the specified server will be returned. This parameter is only available when authenticated.""",
        )
        mapping.add_primitive(
            "image",
            Union[Unset, None, str],
            required=False,
            option_name="image",
            description="""If null or not provided regions that support the size are included in the returned objects regardless of operating system. If this is provided it must be the id or slug of an operating system image and will cause only valid regions for the size and operating system to be included in the returned objects.""",
        )
        return mapping

    @property
    def ok_response_type(self) -> type:
        return SizesResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, SizesResponse, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: SizesResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        page = 0
        per_page = 25
        has_next = True
        response: Optional[SizesResponse] = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                server_id=request.server_id,
                image=request.image,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                return status_code, page_response.parsed

            assert isinstance(page_response.parsed, SizesResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.sizes += page_response.parsed.sizes

        return status_code, response
