from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Tuple

import pytest

from binarylane.console.parser import Mapping
from binarylane.console.runners import Context
from binarylane.console.runners import list as list_runner

if TYPE_CHECKING:
    from http import HTTPStatus

    from binarylane.client import Client


class ListRunner(list_runner.ListRunner):
    default_format_property: List[str]
    fields_property: Dict[str, str]

    def __init__(self) -> None:
        self.default_format_property = ["id", "type", "resource_id"]
        self.fields_property = {key: "" for key in ["id", "status", "type", "started", "resource_type", "resource_id"]}
        super().__init__(Context())

    # START DO-NOTHING REQUIRED METHODS
    class CommandRequest:
        pass

    def create_mapping(self) -> Mapping:
        return Mapping(self.CommandRequest)

    def request(self, client: Client, request: object) -> Tuple[HTTPStatus, object]:
        raise NotImplementedError

    @property
    def ok_response_type(self) -> type:
        return NotImplementedError

    @property
    def reference_url(self) -> str:
        raise NotImplementedError

    # END DO-NOTHING REQUIRED METHODS

    @property
    def default_format(self) -> List[str]:
        return self.default_format_property

    @property
    def fields(self) -> Dict[str, str]:
        return self.fields_property

    @property
    def format(self) -> List[str]:
        return self._format


def parse(args: List[str]) -> ListRunner:
    runner = ListRunner()
    runner.process(runner.parse(args))
    return runner


def test_process_default_format() -> None:
    runner = parse([])
    assert runner.format == runner.default_format


def test_process_basic_format() -> None:
    runner = parse(["--format", "type,started,id"])
    assert runner.format == ["type", "started", "id"]


def test_process_glob_format() -> None:
    runner = parse(["--format", "*"])
    assert runner.format == list(runner.fields.keys())


def test_process_mixed_format() -> None:
    runner = parse(["--format", "*id,status,resource*,*"])
    assert runner.format == ["id", "resource_id", "status", "resource_type", "type", "started"]


def test_process_invalid_basic_format(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit):
        parse(["--format", "server_id"])

    assert "invalid --format value: 'server_id'" in capsys.readouterr().err


def test_process_invalid_glob_format(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit):
        parse(["--format", "server*"])

    assert "invalid --format value: 'server*'" in capsys.readouterr().err
