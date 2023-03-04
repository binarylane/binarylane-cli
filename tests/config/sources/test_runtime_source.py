from __future__ import annotations

from binarylane.config import Option
from binarylane.config.sources import RuntimeSource


def test_get() -> None:
    source = RuntimeSource({Option.API_TOKEN: "test_token"})

    assert source.get(Option.API_URL) is None
    assert source.get(Option.API_TOKEN) == "test_token"
