from __future__ import annotations

from typing import Optional, Type, Union

import pytest

from binarylane.config import Option
from binarylane.config import Repository as Config
from binarylane.config.sources import RuntimeSource


def test_named_options_have_default_values() -> None:
    config = Config()

    # Standard values provided by DefaultSource
    assert config.api_url == "https://api.binarylane.com.au"
    assert config.api_token == "unconfigured"
    assert config.api_development is False
    assert config.config_section == "bl"


def test_without_default_config() -> None:
    config = Config(default_source=False)

    with pytest.raises(RuntimeError):
        config.api_url

    with pytest.raises(RuntimeError):
        config.config_section

    assert config.api_token == "unconfigured"
    assert config.api_development is False


def test_named_options_can_be_configured() -> None:
    config = Config()

    config.add_option(Option.API_URL, "http://api.example")
    config.add_option(Option.API_TOKEN, "test_token")
    config.add_option(Option.API_DEVELOPMENT, "yes")
    config.add_option(Option.CONFIG_SECTION, "test_section")

    assert config.api_url == "http://api.example"
    assert config.api_token == "test_token"
    assert config.api_development is True
    assert config.config_section == "test_section"


def test_source_order_prefers_newest_str() -> None:
    config = Config(default_source=False)
    config.add_source(RuntimeSource({Option.API_URL: "first", Option.API_TOKEN: "first"}))
    config.add_source(RuntimeSource({Option.API_TOKEN: "second", Option.CONFIG_SECTION: "second"}))

    # Second config did not provide a value for api_url, so it is still "first"
    assert config.api_url == "first"

    # Second config has priority for these values
    assert config.api_token == "second"
    assert config.config_section == "second"


def test_source_order_prefers_newest_bool() -> None:
    # Default is false
    config = Config(default_source=False)
    assert config.api_development is False

    # Add a config source providing value of true
    config.add_source(RuntimeSource({Option.API_DEVELOPMENT: "true"}))
    assert config.api_development is True

    # Add a config source providing no value, so the previous value is still used
    config.add_source(RuntimeSource({Option.API_TOKEN: "token"}))
    assert config.api_development is True

    # Add a config source providing False value, which has priority over the earlier value
    config.add_source(RuntimeSource({Option.API_DEVELOPMENT: "off"}))
    assert config.api_development is False


@pytest.mark.parametrize(
    "value,expected",
    [
        ("", ValueError),
        (None, False),
        ("0", False),
        ("no", False),
        ("off", False),
        ("false", False),
        ("OFF", False),
        ("faLSE", False),
        ("1", True),
        ("yes", True),
        ("on", True),
        ("true", True),
        ("ON", True),
        ("tRUe", True),
        ("01", ValueError),
        ("enable", ValueError),
    ],
)
def test_value_conversion(value: Optional[str], expected: Union[bool, Type[Exception]]) -> None:
    config = Config()
    if value is not None:
        config.add_source(RuntimeSource({Option.API_DEVELOPMENT: value}))

    # In str context, value is unmodified:
    assert value == config.get(Option.API_DEVELOPMENT)

    # In boolean context, convert to expected (True/False) ...
    if expected is not ValueError:
        assert expected == config.api_development
        return

    # ... or raise ValueError for other strings
    with pytest.raises(ValueError) as exc:
        config.api_development
    assert exc.match(f"Not a boolean: {value}")
