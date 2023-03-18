from __future__ import annotations

from argparse import ArgumentError
from typing import Union

import pytest

from binarylane.types import UNSET, Unset
from tests.parser import TestRequest, create_parser

from binarylane.console.parser import Mapping, ObjectAttribute, Parser
from binarylane.console.parser import PrimitiveAttribute as Primitive

TEST = "test"
REQUIRED_ARGUMENTS = ["--size", "std-min", "--region", "syd", "--image", "ubuntu"]


class CreateServerRequest(TestRequest):
    size: str
    region: str
    image: str
    name: Union[None, Unset, str] = UNSET
    vpc_id: Union[None, Unset, int] = UNSET
    options: Union[None, Unset, SizeOptionsRequest] = UNSET
    old_ssh_key: Union[None, Unset, SshKeyRequest] = UNSET
    port_blocking: Union[Unset, None, bool] = UNSET

    def __init__(self, size: str, region: str, image: str) -> None:
        self.size = size
        self.region = region
        self.image = image


class SizeOptionsRequest(TestRequest):
    disk: Union[None, Unset, int]
    memory: Union[None, Unset, int]


class SshKeyRequest(TestRequest):
    public_key: str
    name: str
    default: Union[Unset, None, bool] = UNSET

    def __init__(self, public_key: str, name: str) -> None:
        self.public_key = public_key
        self.name = name


@pytest.fixture
def parser() -> Parser:
    parser = create_parser()
    json_body = parser.set_mapping(Mapping(CreateServerRequest))

    def opt(type_: type) -> object:
        return Union[None, Unset, type_]

    json_body.add(Primitive("size", str, option_name="size", required=True, description=TEST))
    json_body.add(Primitive("region", str, option_name="region", required=True, description=TEST))
    json_body.add(Primitive("image", str, option_name="image", required=True, description=TEST))
    json_body.add(Primitive("name", opt(str), option_name="name", required=False, description=TEST))
    json_body.add(Primitive("vpc_id", opt(int), option_name="vpc-id", required=False, description=TEST))
    json_body.add(Primitive("port_blocking", opt(bool), option_name="port-blocking", required=False, description=TEST))

    options = json_body.add(ObjectAttribute("options", SizeOptionsRequest, required=False, description=TEST))
    options.add(Primitive("disk", opt(int), option_name="disk", required=False, description=TEST))
    options.add(Primitive("memory", opt(int), option_name="memory", required=False, description=TEST))
    options.add(Primitive("transfer", opt(int), option_name="transfer", required=False, description=TEST))

    old_ssh_key = json_body.add(ObjectAttribute("old_ssh_key", SshKeyRequest, required=False, description=TEST))
    old_ssh_key.add(Primitive("public_key", str, option_name="public-key", required=True, description=TEST))
    old_ssh_key.add(Primitive("name", str, option_name="name", required=True, description=TEST))
    old_ssh_key.add(Primitive("default", bool, option_name="default", required=False, description=TEST))

    return parser


def test_create_server_with_required_arguments(parser: Parser) -> None:
    parsed = parser.parse(REQUIRED_ARGUMENTS)

    assert parsed.mapped_object.to_dict() == {
        "size": "std-min",
        "region": "syd",
        "image": "ubuntu",
    }


def test_create_server_with_no_arguments(parser: Parser) -> None:
    with pytest.raises(ArgumentError):
        parser.parse([])


def test_create_server_with_options(parser: Parser) -> None:
    parsed = parser.parse(REQUIRED_ARGUMENTS + ["--disk", "20", "--memory", "16"])

    assert parsed.mapped_object.to_dict() == {
        "size": "std-min",
        "region": "syd",
        "image": "ubuntu",
        "options": {
            "disk": 20,
            "memory": 16,
        },
    }


def test_create_server_with_invalid_type(parser: Parser) -> None:
    with pytest.raises(ArgumentError) as exc:
        parser.parse(REQUIRED_ARGUMENTS + ["--vpc-id", "should-be-int"])

    assert "invalid int value" in exc.value.message


def test_create_server_with_subobject_missing_required(parser: Parser) -> None:
    with pytest.raises(ArgumentError) as exc:
        parser.parse(REQUIRED_ARGUMENTS + ["--old-ssh-key-name", "key"])

    assert "the following arguments are required: --old-ssh-key-public-key" in exc.value.message


def test_create_server_with_subobject_optional_but_missing_required(parser: Parser) -> None:
    with pytest.raises(ArgumentError) as exc:
        parser.parse(REQUIRED_ARGUMENTS + ["--old-ssh-key-default"])

    assert "the following arguments are required: --old-ssh-key-public-key, --old-ssh-key-name" in exc.value.message


def test_create_server_with_valid_subobject(parser: Parser) -> None:
    parsed = parser.parse(
        REQUIRED_ARGUMENTS + ["--old-ssh-key-name", "named key", "--old-ssh-key-public-key", "key value"]
    )

    assert parsed.mapped_object.to_dict() == {
        "size": "std-min",
        "region": "syd",
        "image": "ubuntu",
        "old_ssh_key": {
            "public_key": "key value",
            "name": "named key",
        },
    }
