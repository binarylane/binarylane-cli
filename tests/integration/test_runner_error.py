from __future__ import annotations

import json

import pytest
from _pytest.capture import CaptureFixture

from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from tests.runner import TypeRunner

from binarylane.console.commands.servers import post_v2_servers as create_server
from binarylane.console.runners.command import CommandRunner


def test_runner_validation_error(capsys: CaptureFixture[str]) -> None:
    runner = TypeRunner[CommandRunner](create_server.Command)

    runner.setMockResponse(400, ValidationProblemDetails(title="Validation Error", status=400, errors=None))

    # should retun non zero exit code
    with pytest.raises(SystemExit):
        runner.run(["--image", "test", "--region", "test", "--size", "test"])

    # and print to std err
    captured = capsys.readouterr()
    assert "Error: Validation" in captured.err

    # leaving std out empty
    assert "" == captured.out


def test_runner_server_error(capsys: CaptureFixture[str]) -> None:
    runner = TypeRunner[CommandRunner](create_server.Command)

    runner.setMockResponse(500, ProblemDetails(title="Server Error", status=500))

    # should retun non zero exit code
    with pytest.raises(SystemExit):
        runner.run(["--image", "test", "--region", "test", "--size", "test"])

    # and print to std err
    captured = capsys.readouterr()
    assert "Error: Server Error" in captured.err

    # leaving std out empty
    assert "" == captured.out


def test_runner_server_error_json(capsys: CaptureFixture[str]) -> None:
    runner = TypeRunner[CommandRunner](create_server.Command)

    runner.setMockResponse(500, ProblemDetails(title="Server Error", status=500))

    # should retun non zero exit code
    with pytest.raises(SystemExit):
        runner.run(["--image", "test", "--region", "test", "--size", "test", "--output", "json"])

    # and print to std err as raw json
    captured = capsys.readouterr()
    std_err = captured.err
    res = json.loads(std_err)
    assert res["title"] == "Server Error"
    assert res["status"] == 500

    # leaving std out empty
    assert "" == captured.out
