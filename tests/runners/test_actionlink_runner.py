from __future__ import annotations

from typing import TYPE_CHECKING, Tuple

from tests.runner import TypeRunner

from binarylane.console.parser.object_attribute import Mapping
from binarylane.console.runners import actionlink

if TYPE_CHECKING:
    from http import HTTPStatus

    from pytest import CaptureFixture

    from binarylane.client import Client


class ActionLinkRunner(actionlink.ActionLinkRunner):
    def create_mapping(self) -> Mapping:
        return Mapping(ActionLinkRunner)

    def request(self, client: Client, request: object) -> Tuple[HTTPStatus, object]:
        raise NotImplementedError()

    @property
    def ok_response_type(self) -> type:
        raise NotImplementedError()

    @property
    def reference_url(self) -> str:
        return "https://github.com/binarylane/binarylane-cli"


def test_response_delayed_imports(capsys: CaptureFixture[str]) -> None:
    runner = TypeRunner(ActionLinkRunner)
    runner.test.response(204, None)
