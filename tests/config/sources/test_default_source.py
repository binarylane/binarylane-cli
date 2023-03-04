from __future__ import annotations

from binarylane.config import Option
from binarylane.config.sources import DefaultSource


def test_get() -> None:
    source = DefaultSource()

    assert source.get(Option.API_URL) == "https://api.binarylane.com.au"
    assert source.get(Option.API_TOKEN) is None
    assert source.get(Option.API_DEVELOPMENT) is None
    assert source.get(Option.CONFIG_SECTION) == "bl"
