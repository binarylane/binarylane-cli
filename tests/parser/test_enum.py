from __future__ import annotations

from argparse import ArgumentError
from enum import Enum
from typing import List, Union

import pytest

from binarylane.types import UNSET, Unset
from tests.parser import TestRequest, create_parser

from binarylane.console.parser import Mapping, ObjectAttribute, Parser, PrimitiveAttribute

TEST = "test"


class Ping(TestRequest):
    type: PingType

    def __init__(self, type: PingType) -> None:
        self.type = type


class PingType(str, Enum):
    PING = "ping"


class Parent(TestRequest):
    type: PingType
    child: Child

    def __init__(self, type: PingType) -> None:
        self.type = type


class Child(TestRequest):
    type: PingType
    name: str
    description: Union[None, Unset, str] = None

    def __init__(self, type: PingType, name: str) -> None:
        self.type = type
        self.name = name


def test_single_value_enum_does_not_require_configuration() -> None:
    parser = create_parser()
    request = parser.set_mapping(Mapping(Ping))
    request.add(PrimitiveAttribute("type", PingType, option_name="type", required=True, description=TEST))

    # "--type ping" is not required; single-value enum will default to its only value
    assert parser.parse([]).mapped_object.to_dict() == {"type": "ping"}

    # It is not a valid
    with pytest.raises(ArgumentError):
        parser.parse(["--type", "ping"])


class ChangeFeatures(TestRequest):
    features: Union[Unset, None, List[Feature]] = UNSET


class Feature(str, Enum):
    EMULATED_DEVICES = "emulated-devices"
    GUEST_AGENT = "guest-agent"
    UEFI = "uefi"

    def __str__(self) -> str:
        return str(self.value)


@pytest.fixture
def feature_parser() -> Parser:
    parser = create_parser()
    request = parser.set_mapping(Mapping(ChangeFeatures))
    type_ = Union[Unset, None, List[Feature]]
    request.add(PrimitiveAttribute("features", type_, option_name="features", required=False, description=TEST))
    return parser


def test_empty_list_of_enum(feature_parser: Parser) -> None:
    parsed = feature_parser.parse([])
    assert parsed.mapped_object.to_dict() == {}


def test_explicit_empty_list_of_enum(feature_parser: Parser) -> None:
    parsed = feature_parser.parse(["--features"])
    assert parsed.mapped_object.to_dict() == {
        "features": [],
    }


def test_single_item_list_of_enum(feature_parser: Parser) -> None:
    parsed = feature_parser.parse(["--features", "guest-agent"])
    assert parsed.mapped_object.to_dict() == {
        "features": ["guest-agent"],
    }


def test_multiple_item_list_of_enum(feature_parser: Parser) -> None:
    parsed = feature_parser.parse(["--features", "guest-agent", "uefi"])
    assert parsed.mapped_object.to_dict() == {
        "features": ["guest-agent", "uefi"],
    }


def test_repeated_item_list_of_enum(feature_parser: Parser) -> None:
    parsed = feature_parser.parse(["--features", "guest-agent", "--features", "uefi"])
    assert parsed.mapped_object.to_dict() == {
        "features": ["guest-agent", "uefi"],
    }


def test_mixed_item_list_of_enum(feature_parser: Parser) -> None:
    parsed = feature_parser.parse(["--features", "guest-agent", "emulated-devices", "--features", "uefi"])
    assert parsed.mapped_object.to_dict() == {
        "features": ["guest-agent", "emulated-devices", "uefi"],
    }


@pytest.fixture
def nested_parser() -> Parser:
    parser = create_parser()
    request = parser.set_mapping(Mapping(Parent))
    request.add(PrimitiveAttribute("type", PingType, option_name="type", required=True, description=TEST))

    parent = request.add(ObjectAttribute("child", Child, required=False, option_name="child", description=TEST))
    parent.add(PrimitiveAttribute("type", PingType, option_name="type", required=True, description=TEST))
    parent.add(PrimitiveAttribute("name", str, option_name="name", required=True, description=TEST))
    parent.add(PrimitiveAttribute("description", str, option_name="description", required=False, description=TEST))

    return parser


def test_empty_nested_enum(nested_parser: Parser) -> None:
    parsed = nested_parser.parse([])
    assert parsed.mapped_object.to_dict() == {
        "type": "ping",
    }


def test_valid_nested_enum(nested_parser: Parser) -> None:
    parsed = nested_parser.parse(["--name", "test"])
    assert parsed.mapped_object.to_dict() == {
        "type": "ping",
        "child": {
            "type": "ping",
            "name": "test",
        },
    }


def test_invalid_nested_enum(nested_parser: Parser) -> None:
    with pytest.raises(ArgumentError) as exc:
        nested_parser.parse(["--description", "test"])

    assert "following arguments are required: --name" in exc.value.message
