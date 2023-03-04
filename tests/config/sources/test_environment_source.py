from __future__ import annotations

import os

from binarylane.config import Option
from binarylane.config.sources import EnvironmentSource


def test_get_os_environ() -> None:
    os.environ["BL_API_TOKEN"] = "test_token"
    try:
        source = EnvironmentSource()
        assert source.get(Option.API_TOKEN) == "test_token"
    finally:
        del os.environ["BL_API_TOKEN"]


def test_absent() -> None:
    source = EnvironmentSource()
    assert source.get(Option.API_TOKEN) is None
