from __future__ import annotations

from typing import ClassVar, Dict, Optional

from binarylane.config.option import Option
from binarylane.config.source import Source


class DefaultSource(Source):
    _config: ClassVar[Dict[str, str]] = {
        Option.API_URL: "https://api.binarylane.com.au",
        Option.CONFIG_SECTION: "bl",
    }

    def get(self, name: Option) -> Optional[str]:
        return self._config.get(name, None)
