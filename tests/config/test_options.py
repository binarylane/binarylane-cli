from __future__ import annotations

from typing import Dict, Optional, Type, Union

import pytest

from binarylane.config.options import OptionAttributes, OptionName


class TestOptions(OptionAttributes):
    _config: Dict[OptionName, str]

    # Test infrastructure
    def setup_method(self) -> None:
        self._config = {}

    def add_option(self, name: OptionName, value: str) -> None:
        self._config[name] = value

    def get_option(self, name: OptionName) -> Optional[str]:
        return self._config.get(name, None)

    def required_option(self, name: OptionName) -> str:
        return self._config[name]

    # Test cases
    def test_options_can_be_added(self) -> None:
        self.add_option(OptionName.API_URL, "http://api.example")
        self.add_option(OptionName.API_TOKEN, "test_token")
        self.add_option(OptionName.API_DEVELOPMENT, "yes")
        self.add_option(OptionName.CONFIG_SECTION, "test_section")

        assert self.api_url == "http://api.example"
        assert self.api_token == "test_token"
        assert self.api_development is True
        assert self.config_section == "test_section"

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
    def test_value_conversion(self, value: Optional[str], expected: Union[bool, Type[Exception]]) -> None:
        if value is not None:
            self.add_option(OptionName.API_DEVELOPMENT, value)

        # If expected is True/False, check for correct value...
        if expected is not ValueError:
            assert expected == self.api_development
            return

        # ... or ensure ValueError is raised for other strings
        with pytest.raises(ValueError) as exc:
            self.api_development
        assert exc.match(f"Not a boolean: {value}")
