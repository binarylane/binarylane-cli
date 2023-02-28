from __future__ import annotations

from typing import ClassVar, Dict, Optional

from binarylane.console import ConfigSource, Setting


class DefaultConfig(ConfigSource):
    _config: ClassVar[Dict[str, str]] = {
        Setting.ApiUrl: "https://api.binarylane.com.au",
        Setting.ConfigSection: "bl",
    }

    def get(self, name: str) -> Optional[str]:
        return self._config.get(name, None)
