from __future__ import annotations

from abc import ABC
from argparse import ArgumentError
from typing import Dict, NoReturn, Optional

from binarylane.console.parser.parser import Parser


class TestRequest(ABC):
    def to_dict(self) -> Dict[str, object]:
        result = vars(self)
        for name in result:
            if isinstance(result[name], TestRequest):
                result[name] = result[name].to_dict()
            if isinstance(result[name], list):
                for idx, value in enumerate(result[name]):
                    if isinstance(value, TestRequest):
                        result[name][idx] = value.to_dict()
        return result


class TestParser(Parser):
    def exit(self, status: int = 0, message: Optional[str] = None) -> NoReturn:
        raise ArgumentError(None, message or f"status={status}")


def create_parser() -> Parser:
    return TestParser(prog="bl test")
