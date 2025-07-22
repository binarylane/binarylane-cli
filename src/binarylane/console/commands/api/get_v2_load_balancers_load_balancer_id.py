from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.load_balancers.get_v2_load_balancers_load_balancer_id import sync_detailed
from binarylane.models.load_balancer_response import LoadBalancerResponse
from binarylane.models.problem_details import ProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

import binarylane.console.commands.api.get_v2_load_balancers as api_get_v2_load_balancers
from binarylane.console.parser import Mapping, PrimitiveAttribute
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    load_balancer_id: int

    def __init__(self, load_balancer_id: int) -> None:
        self.load_balancer_id = load_balancer_id


class Command(CommandRunner):
    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/LoadBalancers/paths/~1v2~1load_balancers~1%7Bload_balancer_id%7D/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        def lookup_load_balancer_id(ref: str) -> Union[None, int]:
            return api_get_v2_load_balancers.Command(self._context).lookup(ref)

        mapping.add(
            PrimitiveAttribute(
                "load_balancer_id",
                int,
                required=True,
                option_name=None,
                metavar="load_balancer",
                description="""The ID or name of the load balancer to fetch.""",
                lookup=lookup_load_balancer_id,
            )
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return LoadBalancerResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, LoadBalancerResponse, ProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: LoadBalancerResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            load_balancer_id=request.load_balancer_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
