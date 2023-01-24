from __future__ import annotations

from argparse import ArgumentError
from typing import List, Union

import pytest

from binarylane.types import UNSET, Unset
from tests.parser import TestRequest, create_parser

from binarylane.console.parser import ListAttribute, Mapping
from binarylane.console.parser.parser import Parser

REQUIRED_ARGUMENTS = ["--name", "test"]
TEST = "test"


class CreateVpcRequest(TestRequest):
    name: str
    route_entries: Union[Unset, None, List[RouteEntryRequest]] = UNSET
    ip_range: Union[Unset, None, str] = UNSET

    def __init__(self, name: str) -> None:
        self.name = name


class RouteEntryRequest(TestRequest):
    router: str
    destination: str
    description: Union[Unset, None, str] = UNSET

    def __init__(self, router: str, destination: str) -> None:
        self.router = router
        self.destination = destination


@pytest.fixture
def parser() -> Parser:
    parser = create_parser()
    request = parser.set_mapping(Mapping(CreateVpcRequest))
    request.add_primitive("name", str, option_name="name", required=True, description=TEST)
    request.add_primitive("ip_range", str, option_name="ip-range", required=False, description=TEST)

    route_list = request.add(
        ListAttribute("route_entries", RouteEntryRequest, required=False, description="Route Entries")
    )
    route_list.add_primitive("router", str, option_name="router", required=True, description=TEST)
    route_list.add_primitive("destination", str, option_name="destination", required=True, description=TEST)
    route_list.add_primitive("description", str, option_name="description", required=False, description=TEST)

    return parser


def test_empty_list(parser: Parser) -> None:
    parsed = parser.parse(REQUIRED_ARGUMENTS)

    assert parsed.mapped_object.to_dict() == {
        "name": "test",
    }


def test_single_item_list(parser: Parser) -> None:
    parsed = parser.parse(REQUIRED_ARGUMENTS + ["+route", "--router", "1", "--destination", "2"])

    assert parsed.mapped_object.to_dict() == {"name": "test", "route_entries": [{"router": "1", "destination": "2"}]}


def test_multi_item_list(parser: Parser) -> None:
    parsed = parser.parse(
        REQUIRED_ARGUMENTS
        + [
            "+route",
            "--router",
            "1",
            "--destination",
            "2",
        ]
        + [
            "+route",
            "--router",
            "3",
            "--destination",
            "4",
            "--description",
            "middle",
        ]
        + [
            "+route",
            "--router",
            "5",
            "--destination",
            "6",
        ]
    )

    assert parsed.mapped_object.to_dict() == {
        "name": "test",
        "route_entries": [
            {"router": "1", "destination": "2"},
            {"router": "3", "destination": "4", "description": "middle"},
            {"router": "5", "destination": "6"},
        ],
    }


def test_invalid_keyword(parser: Parser) -> None:
    with pytest.raises(ArgumentError) as exc:
        parser.parse(REQUIRED_ARGUMENTS + ["+rule", "--source", "1", "--destination", "2"])

    assert "unrecognized arguments: +rule" in exc.value.message


def test_valid_and_invalid_keyword(parser: Parser) -> None:
    with pytest.raises(ArgumentError) as exc:
        parser.parse(REQUIRED_ARGUMENTS + ["+route", "--router", "1", "--destination", "2", "+rule", "--source", "3"])

    assert "unrecognized arguments: +rule" in exc.value.message


def test_invalid_list_item(parser: Parser) -> None:
    with pytest.raises(ArgumentError) as exc:
        parser.parse(REQUIRED_ARGUMENTS + ["+route", "--router", "1"])

    assert "the following arguments are required: --destination" in exc.value.message


def test_valid_and_invalid_list_item(parser: Parser) -> None:
    with pytest.raises(ArgumentError) as exc:
        parser.parse(
            REQUIRED_ARGUMENTS + ["+route", "--router", "1", "--destination", "2", "+route", "--description", "test"]
        )

    assert "the following arguments are required: --router, --destination" in exc.value.message


def test_list_item_must_be_last(parser: Parser) -> None:
    with pytest.raises(ArgumentError) as exc:
        parser.parse(REQUIRED_ARGUMENTS + ["+route", "--router", "1", "--ip-range", "10.240.0.0/16"])

    assert "unrecognized arguments: --ip-range" in exc.value.message


def test_invalid_list_item_has_correct_prog(parser: Parser) -> None:
    """list has its own subparser, so check its error output matches root parser"""
    with pytest.raises(ArgumentError) as exc:
        parser.parse(REQUIRED_ARGUMENTS + ["+route", "--router", "1"])

    assert "bl test: error: " in exc.value.message
