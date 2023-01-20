from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.domain.domain_nameservers_list import sync_detailed
from binarylane.models.local_nameservers_response import LocalNameserversResponse

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    pass


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """List All Public Nameservers"""

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)
        return mapping

    @property
    def ok_response_type(self) -> type:
        return LocalNameserversResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, LocalNameserversResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: LocalNameserversResponse
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
