from __future__ import annotations

import argparse
from typing import TYPE_CHECKING, MutableMapping

import pytest

from binarylane.config import DefaultConfig, OptionName, UserConfig
from binarylane.config.sources import CommandlineSource, DefaultSource, EnvironmentSource, FileSource

if TYPE_CHECKING:
    from pathlib import Path


def test_default_values() -> None:
    config = DefaultConfig()

    # Standard values provided by DefaultSource
    assert config.api_url == "https://api.binarylane.com.au"
    assert config.api_token == "unconfigured"
    assert config.api_development is False
    assert config.config_section == "bl"


def test_save_production(tmp_path: Path, tmp_env: MutableMapping[str, str]) -> None:
    config_file = tmp_path / "config.ini"
    config = UserConfig(config_file=config_file)
    config.add_commandline(argparse.Namespace())
    config.add_option(OptionName.API_TOKEN, "test_token")
    config.save()

    with open(config_file) as file:
        data = file.read()
    # API URL and Development flag not included as they have default value
    assert data.strip() == "[bl]\napi-token = test_token"


def test_save_development(tmp_path: Path, tmp_env: MutableMapping[str, str]) -> None:
    tmp_env["BL_API_URL"] = "http://api.example"
    tmp_env["BL_API_DEVELOPMENT"] = "on"

    config_file = tmp_path / "config.ini"
    config = UserConfig(config_file=config_file)
    config.add_commandline(argparse.Namespace())
    config.save()

    with open(config_file) as file:
        data = file.read()
    # API URL and Development flag not included as they have default value
    assert data.strip() == "[bl]\napi-url = http://api.example\napi-development = true"


def test_initialize_sources(tmp_path: Path) -> None:
    config_file = tmp_path / "config.ini"
    config = UserConfig(config_file=config_file)

    for source in (DefaultSource, EnvironmentSource, FileSource):
        assert isinstance(config.get_source(source), source)

    with pytest.raises(KeyError):
        config.get_source(CommandlineSource)


def test_config_section_read_from_repository(tmp_path: Path, tmp_env: MutableMapping[str, str]) -> None:
    config_file = tmp_path / "config.ini"
    with open(config_file, "w") as file:
        file.write(
            """\
[bl]
api-token = file

[env]
api-token = env

[commandline]
api-token = commandline
"""
        )

    config = UserConfig(config_file=config_file)
    assert config.api_token == "file"

    tmp_env["BL_CONTEXT"] = "env"
    config = UserConfig(config_file=config_file)
    assert config.api_token == "env"

    config = UserConfig(config_file=config_file)
    config.add_commandline(argparse.Namespace(context="commandline"))
    assert config.api_token == "commandline"
