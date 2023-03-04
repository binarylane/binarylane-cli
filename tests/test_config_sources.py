from __future__ import annotations

import argparse
import os
from pathlib import Path
from tempfile import NamedTemporaryFile, TemporaryDirectory

from binarylane.config.options import Option
from binarylane.config.sources import CommandlineSource, DefaultSource, EnvironmentSource, FileSource, RuntimeSource


def test_commandline_get() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(f"--{Option.API_TOKEN}")
    parsed = parser.parse_args([f"--{Option.API_TOKEN}", "test_token"])

    source = CommandlineSource(parsed)

    assert source.get(Option.API_TOKEN) == "test_token"
    assert source.get(Option.API_URL) is None


def test_default_get() -> None:
    source = DefaultSource()

    assert source.get(Option.API_URL) == "https://api.binarylane.com.au"
    assert source.get(Option.API_TOKEN) is None
    assert source.get(Option.API_DEVELOPMENT) is None
    assert source.get(Option.CONFIG_SECTION) == "bl"


def test_environment_get_str() -> None:
    os.environ["BL_API_TOKEN"] = "test_token"
    try:
        source = EnvironmentSource()
        assert source.get(Option.API_TOKEN) == "test_token"
    finally:
        del os.environ["BL_API_TOKEN"]


def test_environment_get_none() -> None:
    source = EnvironmentSource()
    assert source.get(Option.API_TOKEN) is None


def test_file_get_str() -> None:
    with NamedTemporaryFile() as file:
        file.write(
            """\
[bl]
api-token = test_token
""".encode()
        )
        file.flush()

        source = FileSource(Path(file.name))
        source.section_name = "bl"

        assert source.get(Option.API_TOKEN) == "test_token"


def test_file_get_none() -> None:
    with TemporaryDirectory() as directory:
        config_file = Path(directory) / "config.ini"  # Does not exist
        source = FileSource(config_file)
        source.section_name = "bl"

        assert source.get(Option.API_TOKEN) is None


def test_runtime_get() -> None:
    source = RuntimeSource({Option.API_TOKEN: "test_token"})

    assert source.get(Option.API_URL) is None
    assert source.get(Option.API_TOKEN) == "test_token"
