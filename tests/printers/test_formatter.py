from typing import Any, Dict, List

from blcli.printers import formatter


def test_format_str() -> None:
    assert formatter.format_response("test", True) == [[formatter.DEFAULT_HEADING], ["test"]]
    assert formatter.format_response("test", False) == [["test"]]


def test_format_list() -> None:
    ns1 = "ns1.binarylane.com.au"
    ns2 = "ns2.binarylane.com.au"
    dns = [ns1, ns2]

    assert formatter.format_response(dns, True) == [[formatter.DEFAULT_HEADING], [ns1], [ns2]]
    assert formatter.format_response(dns, False) == [[ns1], [ns2]]


def test_format_primary_list() -> None:
    class DnsList:
        dns: List[str]
        meta: Dict[str, Any]
        links: List[str]

        def __init__(self) -> None:
            self.dns = ["ns1.binarylane.com.au", "ns2.binarylane.com.au"]

    response = DnsList()
    assert formatter.format_response(response, True) == [
        [formatter.DEFAULT_HEADING],
        [response.dns[0]],
        [response.dns[1]],
    ]


def test_format_primary_str() -> None:
    class DnsError:
        message: str
        meta: Dict[str, Any]
        links: List[str]

        def __init__(self) -> None:
            self.message = "DNS Error"

    response = DnsError()
    assert formatter.format_response(response, True) == [[formatter.DEFAULT_HEADING], [response.message]]
