from __future__ import annotations

from http import HTTPStatus
from typing import Tuple

import pytest
from _pytest.capture import CaptureFixture

from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails, ValidationProblemDetailsErrors
from tests.runner import TypeRunner

from binarylane.console.parser import Mapping
from binarylane.console.runners import command


class CommandRunner(command.CommandRunner):
    def create_mapping(self) -> Mapping:
        return Mapping(CommandRunner)

    def request(self, client: Client, request: object) -> Tuple[HTTPStatus, object]:
        raise NotImplementedError()

    @property
    def ok_response_type(self) -> type:
        raise NotImplementedError()

    @property
    def reference_url(self) -> str:
        return "https://github.com/binarylane/binarylane-cli"


def test_response_handles_validation_errors(capsys: CaptureFixture[str]) -> None:
    problem = ValidationProblemDetails.from_dict({"title": "Server not found", "errors": {"server_id": ["Server not found."]}})
    runner = TypeRunner(CommandRunner)

    with pytest.raises(SystemExit):
        runner.test.response(400, problem)

    captured = capsys.readouterr()
    assert "bl: error: argument SERVER_ID: server not found" in captured.err


def test_response_handles_problem_errors(capsys: CaptureFixture[str]) -> None:
    problem = ProblemDetails.from_dict({"title": "Server not found", "errors": {"server_id": ["Server not found."]}})
    runner = TypeRunner(CommandRunner)

    with pytest.raises(SystemExit):
        runner.test.response(400, problem)

    captured = capsys.readouterr()
    assert "bl: error: argument SERVER_ID: server not found" in captured.err


def test_response_handles_detail_error(capsys: CaptureFixture[str]) -> None:
    problem = ProblemDetails.from_dict({"title":"Server not found", "detail": "Unable to locate server with ID 1."})
    runner = TypeRunner(CommandRunner)

    with pytest.raises(SystemExit):
        runner.test.response(400, problem)

    captured = capsys.readouterr()
    assert "bl: error: Unable to locate server with ID 1." in captured.err


def test_response_handles_title_error(capsys: CaptureFixture[str]) -> None:
    problem = ProblemDetails.from_dict({"title":"Server not found."})
    runner = TypeRunner(CommandRunner)

    with pytest.raises(SystemExit):
        runner.test.response(400, problem)

    captured = capsys.readouterr()
    assert "bl: error: Server not found." in captured.err


def test_response_handles_none_error(capsys: CaptureFixture[str]) -> None:
    runner = TypeRunner(CommandRunner)

    with pytest.raises(SystemExit):
        runner.test.response(400, None)

    captured = capsys.readouterr()
    assert "ERROR: HTTP 400" in captured.err


def test_response_handles_nocontent(capsys: CaptureFixture[str]) -> None:
    runner = TypeRunner(CommandRunner)

    runner.test.response(204, None)

    captured = capsys.readouterr()
    assert captured.err == "" and captured.out == ""
