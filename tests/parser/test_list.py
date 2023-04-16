from __future__ import annotations

from argparse import ArgumentError
from typing import Any, Dict, List, Union

import pytest

from binarylane.types import UNSET, Unset
from tests.parser import TestRequest, create_parser

from binarylane.console.parser import ListAttribute, Mapping, Parser, PrimitiveAttribute

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


def add_route_entries(request: Mapping, *, required: bool) -> None:
    route_list = request.add(
        ListAttribute("route_entries", RouteEntryRequest, required=required, description="Route Entries")
    )
    route_list.add(PrimitiveAttribute("router", str, option_name="router", required=True, description=TEST))
    route_list.add(PrimitiveAttribute("destination", str, option_name="destination", required=True, description=TEST))
    route_list.add(PrimitiveAttribute("description", str, option_name="description", required=False, description=TEST))


@pytest.fixture
def parser() -> Parser:
    parser = create_parser()
    request = parser.set_mapping(Mapping(CreateVpcRequest))
    request.add(PrimitiveAttribute("name", str, option_name="name", required=True, description=TEST))
    request.add(PrimitiveAttribute("ip_range", str, option_name="ip-range", required=False, description=TEST))

    add_route_entries(request, required=False)

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


class RequiredListRequest(TestRequest):
    name: str
    route_entries: List[RouteEntryRequest]

    def __init__(self, name: str, route_entries: List[RouteEntryRequest]) -> None:
        self.name = name
        self.route_entries = route_entries


@pytest.fixture
def required_parser() -> Parser:
    parser = create_parser()
    request = parser.set_mapping(Mapping(RequiredListRequest))
    request.add(PrimitiveAttribute("name", str, option_name="name", required=True, description=TEST))

    add_route_entries(request, required=True)

    return parser


def test_empty_required_list(required_parser: Parser) -> None:
    parsed = required_parser.parse(REQUIRED_ARGUMENTS)

    assert parsed.mapped_object.to_dict() == {"name": "test", "route_entries": []}


def test_required_list_usage(required_parser: Parser) -> None:
    required_parser.parse(REQUIRED_ARGUMENTS)
    assert required_parser.format_usage() == "usage: bl test [OPTIONS] --name NAME [+route ... ]\n"


class ListRequest(TestRequest):
    sublist: List[Sublist]

    def __init__(self, sublist: List[Sublist]) -> None:
        self.sublist = sublist

    def to_dict(self) -> Dict[str, Any]:
        return {"sublist": [sublist.to_dict() if sublist else None for sublist in self.sublist]}


class Sublist:
    name: List[str]
    description: Union[str, None] = None

    def __init__(self, name: List[str]) -> None:
        self.name = name

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {"name": self.name}
        if self.description is not None:
            result["description"] = self.description
        return result


@pytest.fixture
def sublist_parser() -> Parser:
    parser = create_parser()
    mapping = parser.set_mapping(Mapping(ListRequest))
    attr = mapping.add(ListAttribute("sublist", Sublist, required=True))
    attr.add(PrimitiveAttribute("name", List[str], required=True, option_name="name"))
    attr.add(PrimitiveAttribute("description", str, required=False, option_name="description"))

    return parser


def test_list_of_list_of_str(sublist_parser: Parser) -> None:
    parsed = sublist_parser.parse(["+sublist", "--description", "test", "--name", "a", "b", "+sublist", "--name", "c"])
    assert parsed.mapped_object.to_dict() == {
        "sublist": [
            {"name": ["a", "b"], "description": "test"},
            {"name": ["c"]},
        ]
    }


def test_list_of_empty_list_of_str(sublist_parser: Parser) -> None:
    parsed = sublist_parser.parse(["+sublist", "--name"])
    assert parsed.mapped_object.to_dict() == {
        "sublist": [
            {"name": []},
        ]
    }


def test_list_of_missing_sublist_is_error(sublist_parser: Parser) -> None:
    with pytest.raises(ArgumentError) as exc:
        sublist_parser.parse(["+sublist"])

    assert "bl test: error: " in exc.value.message
