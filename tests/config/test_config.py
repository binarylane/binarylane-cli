from __future__ import annotations

import argparse
from pathlib import Path
from typing import MutableMapping

import pytest

from binarylane.config import Config
from binarylane.config.options import OptionName


def test_default_values() -> None:
    config = Config()

    # Standard values provided by DefaultSource
    assert config.api_url == "https://api.binarylane.com.au"
    assert config.api_token == "unconfigured"
    assert config.api_development is False
    assert config.config_section == "bl"


def test_default_values_without_default_source() -> None:
    config = Config(default_source=False)

    # Intended behaviour with no sources:
    with pytest.raises(KeyError):
        config.api_url

    with pytest.raises(KeyError):
        config.config_section

    assert config.api_token == "unconfigured"
    assert config.api_development is False


def test_save_production(tmp_path: Path) -> None:
    config_file = Path(tmp_path) / "config.ini"
    config = Config()
    config.initialize(commandline=argparse.Namespace(), config_file=config_file)
    config.add_option(OptionName.API_TOKEN, "test_token")
    config.save()

    with open(config_file) as file:
        data = file.read()
    # API URL and Development flag not included as they have default value
    assert data.strip() == "[bl]\napi-token = test_token"


def test_save_development(tmp_path: Path, tmp_env: MutableMapping[str, str]) -> None:
    tmp_env["BL_API_URL"] = "http://api.example"
    tmp_env["BL_API_DEVELOPMENT"] = "on"

    config_file = Path(tmp_path) / "config.ini"
    config = Config()
    config.initialize(commandline=argparse.Namespace(), config_file=config_file)
    config.save()

    with open(config_file) as file:
        data = file.read()
    # API URL and Development flag not included as they have default value
    assert data.strip() == "[bl]\napi-url = http://api.example\napi-development = true"
