from __future__ import annotations

from typing import Any, Dict, List

from binarylane.console.printers.json_printer import JsonPrinter

printer = JsonPrinter()


def test_format_str() -> None:
    assert printer.format_response("test") == '"test"'


def test_format_list() -> None:
    ns1 = "ns1.binarylane.com.au"
    ns2 = "ns2.binarylane.com.au"
    dns = [ns1, ns2]

    assert printer.format_response(dns) == '["ns1.binarylane.com.au", "ns2.binarylane.com.au"]'


def test_format_dict() -> None:
    class DnsList:
        dns: List[str]
        meta: Dict[str, Any]
        links: List[str]

        def __init__(self) -> None:
            self.dns = ["ns1.binarylane.com.au", "ns2.binarylane.com.au"]

        def to_dict(self) -> Dict[str, Any]:
            return {"dns": self.dns}

    response = DnsList()
    assert printer.format_response(response) == '{"dns": ["ns1.binarylane.com.au", "ns2.binarylane.com.au"]}'


# ActionLinkRunner when used with --async will print the action ID
def test_format_int() -> None:
    assert printer.format_response(12345) == "12345"
