from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import pytest

from tests.parser import ArgumentError, create_parser

from binarylane.console.parser import Mapping, Parser, PrimitiveAttribute


@dataclass
class ServerRequest:
    server_id: int


def lookup_server_id(ref: str) -> Optional[int]:
    return 1 if ref == "test" else None


@pytest.fixture
def parser() -> Parser:
    parser = create_parser()

    request = parser.set_mapping(Mapping(ServerRequest))
    request.add(
        PrimitiveAttribute(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The target server id.""",
            lookup=lookup_server_id,
        )
    )

    return parser


def test_successful_lookup(parser: Parser) -> None:
    parsed = parser.parse(["test"])
    assert parsed.mapped_object.server_id == 1


def test_failed_lookup(parser: Parser) -> None:
    with pytest.raises(ArgumentError) as exc:
        parser.parse(["wrong"])

    assert "error: SERVER_ID: could not find 'wrong'" in exc.value.message


def test_no_lookup(parser: Parser) -> None:
    parsed = parser.parse(["2"])
    assert parsed.mapped_object.server_id == 2
