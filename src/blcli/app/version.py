import importlib
import importlib.metadata
from typing import List, Optional

from ..runners import Runner


class VersionRunner(Runner):
    """Display blcli package version"""

    @property
    def name(self) -> str:
        return "version"

    @property
    def description(self) -> str:
        return "Show the current version"

    def run(self, args: List[str]) -> None:
        package = __package__
        version = self._distribution_version("binarylane-cli") or self._module_version(package) or "dev"

        print(self.prog, version)

    def _distribution_version(self, package: str) -> Optional[str]:
        try:
            return importlib.metadata.distribution(package).version
        except importlib.metadata.PackageNotFoundError:
            return None

    def _module_version(self, package: str) -> Optional[str]:
        try:
            return importlib.import_module(".._version", package).__version__
        except ModuleNotFoundError:
            return None
