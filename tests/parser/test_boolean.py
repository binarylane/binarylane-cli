from __future__ import annotations

from typing import Union

import pytest

from binarylane.types import UNSET, Unset
from tests.parser import create_parser

from binarylane.console.parser import Mapping, Parser
from binarylane.console.parser import PrimitiveAttribute as Primitive

TEST = "test"


class PortBlockingRequest:
    port_blocking: Union[Unset, None, bool] = UNSET


@pytest.fixture
def parser() -> Parser:
    parser = create_parser()

    request = parser.set_mapping(Mapping(PortBlockingRequest))
    request.add(Primitive("port_blocking", bool, option_name="port-blocking", required=False, description=TEST))

    return parser


def test_create_server_boolean_unset(parser: Parser) -> None:
    parsed = parser.parse([])
    assert parsed.mapped_object.port_blocking is UNSET


def test_create_server_boolean_true(parser: Parser) -> None:
    parsed = parser.parse(["--port-blocking"])
    assert parsed.mapped_object.port_blocking is True


def test_create_server_boolean_false(parser: Parser) -> None:
    parsed = parser.parse(["--no-port-blocking"])
    assert parsed.mapped_object.port_blocking is False
