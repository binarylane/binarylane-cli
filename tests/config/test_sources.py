from __future__ import annotations

import argparse
from pathlib import Path
from typing import MutableMapping

from binarylane.config import OptionName
from binarylane.config.sources import CommandlineSource, DefaultSource, EnvironmentSource, FileSource, RuntimeSource


def test_commandline_get() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(f"--{OptionName.API_TOKEN}")
    parsed = parser.parse_args([f"--{OptionName.API_TOKEN}", "test_token"])

    source = CommandlineSource(parsed)
    print(f"{OptionName.API_TOKEN}", parsed, source._config)

    assert source.get(OptionName.API_TOKEN) == "test_token"
    assert source.get(OptionName.API_URL) is None


def test_default_get() -> None:
    source = DefaultSource()

    assert source.get(OptionName.API_URL) == "https://api.binarylane.com.au"
    assert source.get(OptionName.API_TOKEN) is None
    assert source.get(OptionName.API_DEVELOPMENT) is None
    assert source.get(OptionName.CONFIG_SECTION) == "bl"


def test_environment_get(tmp_env: MutableMapping[str, str]) -> None:
    tmp_env["BL_API_TOKEN"] = "test_token"
    source = EnvironmentSource()
    assert source.get(OptionName.API_TOKEN) == "test_token"
    assert source.get(OptionName.API_URL) is None


def test_file_get(tmp_path: Path) -> None:
    config_file = tmp_path / "test.txt"

    with open(config_file, "w") as file:
        file.write(
            """\
[test]
api-token = other_token
api-url = api.example

[bl]
api-token = test_token
"""
        )

    source = FileSource(config_file)
    source.section_name = "bl"

    assert source.get(OptionName.API_TOKEN) == "test_token"
    assert source.get(OptionName.API_URL) is None


def test_runtime_get() -> None:
    source = RuntimeSource({OptionName.API_TOKEN: "test_token"})

    assert source.get(OptionName.API_TOKEN) == "test_token"
    assert source.get(OptionName.API_URL) is None
