from __future__ import annotations

from typing import Any, Dict, List, cast

from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.models.validation_problem_details_errors import ValidationProblemDetailsErrors

from binarylane.console.printers import formatter


def test_format_str() -> None:
    assert formatter.format_response("test", True) == {"table": [[formatter.DEFAULT_HEADING], ["test"]], "title": None}
    assert formatter.format_response("test", False) == {"table": [["test"]], "title": None}


def test_format_list() -> None:
    ns1 = "ns1.binarylane.com.au"
    ns2 = "ns2.binarylane.com.au"
    dns = [ns1, ns2]

    assert formatter.format_response(dns, True) == {"table": [[formatter.DEFAULT_HEADING], [ns1], [ns2]], "title": None}
    assert formatter.format_response(dns, False) == {"table": [[ns1], [ns2]], "title": None}


def test_format_primary_list() -> None:
    class DnsList:
        dns: List[str]
        meta: Dict[str, Any]
        links: List[str]

        def __init__(self) -> None:
            self.dns = ["ns1.binarylane.com.au", "ns2.binarylane.com.au"]

    response = DnsList()
    assert formatter.format_response(response, True) == {
        "table": [
            [formatter.DEFAULT_HEADING],
            [response.dns[0]],
            [response.dns[1]],
        ],
        "title": None,
    }


def test_format_primary_str() -> None:
    class DnsError:
        message: str
        meta: Dict[str, Any]
        links: List[str]

        def __init__(self) -> None:
            self.message = "DNS Error"

    response = DnsError()
    assert formatter.format_response(response, True) == {
        "table": [[formatter.DEFAULT_HEADING], [response.message]],
        "title": None,
    }


def test_format_problem_details() -> None:
    response = ProblemDetails(
        title="General Protection Fault",
        type="https://httpstatuses.com/500",
        status=500,
        detail="The server encountered an unexpected condition that prevented it from fulfilling the request.",
    )
    assert formatter.format_response(response, True) == {
        "table": cast(List[List[str]], []),
        "title": f"Error: {response.title}\n\n{response.detail}",
    }


def test_format_validation_problem_details() -> None:
    response = ValidationProblemDetails(
        title="There were validation errors",
        type="https://httpstatuses.com/400",
        status=400,
        detail="Please fix the errors and try again",
        errors=ValidationProblemDetailsErrors.from_dict(
            {"name": ["Name is required", "name must be unique"], "region": ["Region is required"]}
        ),
    )
    assert formatter.format_response(response, True) == {
        "table": [
            ["field", "errors"],
            ["name", "Name is required\nname must be unique"],
            ["region", "Region is required"],
        ],
        "title": f"Error: {response.title}",
    }


def test_format_validation_problem_details_no_errors() -> None:
    response = ValidationProblemDetails(
        title="Email already in use",
        type="https://httpstatuses.com/400",
        status=400,
        detail="Please fix the errors and try again",
        errors=None,
    )
    assert formatter.format_response(response, True) == {
        "table": cast(List[List[str]], []),
        "title": f"Error: {response.title}",
    }
