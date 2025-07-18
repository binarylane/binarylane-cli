from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Any, List, Tuple, Union

from binarylane.api.domains.post_v2_domains_refresh_nameserver_cache import sync_detailed
from binarylane.models.domain_refresh_request import DomainRefreshRequest

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping, PrimitiveAttribute
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    json_body: DomainRefreshRequest

    def __init__(self, json_body: DomainRefreshRequest) -> None:
        self.json_body = json_body


class Command(CommandRunner):
    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Domains/paths/~1v2~1domains~1refresh_nameserver_cache/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        json_body = mapping.add_json_body(DomainRefreshRequest)

        json_body.add(
            PrimitiveAttribute(
                "domain_names",
                List[str],
                required=True,
                option_name="domain-names",
                description="""The domain names to refresh.""",
            )
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return type(None)

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, Any]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
