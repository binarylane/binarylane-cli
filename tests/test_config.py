from __future__ import annotations

import os
from typing import Generator, Type, Union

import pytest

from binarylane.console import Setting
from binarylane.console.config import Config, EnvironmentConfig


@pytest.fixture()
def config() -> Generator[Config, None, None]:
    yield Config()

    # Remove any environment variables created by testcase
    for key in os.environ:
        if key.startswith("BL_"):
            del os.environ[key]


@pytest.mark.parametrize(
    "value,expected",
    [
        ("", False),
        ("0", False),
        ("no", False),
        ("off", False),
        ("false", False),
        ("1", True),
        ("yes", True),
        ("on", True),
        ("true", True),
        ("01", ValueError),
        ("enable", ValueError),
    ],
)
def test_development_environment_variable(config: Config, value: str, expected: Union[bool, Type[Exception]]) -> None:
    os.environ["BL_API_DEVELOPMENT"] = value
    config.add_config_source(EnvironmentConfig())

    if expected is not ValueError:
        assert expected == bool(config.get(Setting.ApiDevelopment))
        return

    with pytest.raises(ValueError) as exc:
        bool(config.get(Setting.ApiDevelopment))
    assert exc.match("Not a boolean: " + value)


def test_development_default(config: Config) -> None:
    assert bool(config.get(Setting.ApiDevelopment)) is False
