from __future__ import annotations

import json
import urllib.parse
from abc import ABC, abstractmethod
from types import TracebackType
from typing import TYPE_CHECKING, Any, Callable, Optional, TypeVar
from binarylane.pycompat import shlex

if TYPE_CHECKING:
    import httpx


WrapperT = TypeVar("WrapperT", bound="HttpxWrapper")


class HttpxWrapper(ABC):
    """Hook httpx.request to enable displaying additional information from API calls"""

    def __init__(self) -> None:
        # Lazy import of httpx, since this wrapper is rarely used
        import httpx

        globals()["httpx"] = httpx

    _httpx_request: Optional[Callable[..., httpx.Response]]

    def __enter__(self: WrapperT) -> WrapperT:

        self._httpx_request = httpx.request
        httpx.request = self.request
        return self

    @abstractmethod
    def request(self, *args: Any, **kwargs: Any) -> httpx.Response:
        """Perform HTTP request - child classes can override to modify and/or replace request"""
        if self._httpx_request:
            return self._httpx_request(*args, **kwargs)
        raise ValueError()

    def __exit__(
        self, exc_type: Optional[type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]
    ) -> None:
        httpx.request = self._httpx_request  # type: ignore


class CurlCommand(HttpxWrapper):  # pylint: disable=too-few-public-methods
    """Convert HTTP request to a curl command-line. The HTTP request is not performed."""

    shell: str

    def request(self, *args: Any, **kwargs: Any) -> httpx.Response:
        query_string = "" if not kwargs.get("params") else "?" + urllib.parse.urlencode(kwargs["params"])
        curl_cmdline = ["curl", "--request", kwargs["method"].upper(), kwargs["url"] + query_string]

        for header, value in kwargs.get("headers", {}).items():
            curl_cmdline += ["--header", f"{header}: {value}"]

        if kwargs.get("json"):
            curl_cmdline += ["--header", "Content-Type: application/json", "--data", json.dumps(kwargs["json"])]

        self.shell = shlex.join(curl_cmdline)

        # Intentionally not calling super().request, so that the request is not executed
        return httpx.Response(401)
