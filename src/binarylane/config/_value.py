from __future__ import annotations

from configparser import ConfigParser


class Value(str):
    """
    Override standard bool behaviour for OptionValue strings so that rather than the usual behaviour, a value of
    - "true"/"yes"/"1"/"on" is True
    - "false"/"no"/"0"/"off" is False
    - all other values (including "") will raise ValueError

    Above comparisons are case-insensitive.
    """

    def __bool__(self) -> bool:
        value = ConfigParser.BOOLEAN_STATES.get(self.lower())
        if value is not None:
            return value
        raise ValueError(f"Not a boolean: {self}")
