from __future__ import annotations

import argparse

from binarylane.config import Option
from binarylane.config.sources import CommandlineSource


def test_get() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(f"--{Option.API_TOKEN}")
    parsed = parser.parse_args([f"--{Option.API_TOKEN}", "test_token"])

    source = CommandlineSource(parsed)

    assert source.get(Option.API_TOKEN) == "test_token"
    assert source.get(Option.API_URL) is None
