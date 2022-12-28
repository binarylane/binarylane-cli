# pylint: disable=missing-module-docstring

from abc import abstractmethod
from typing import Any, List

from ..cli import display
from .command_runner import CommandRunner


class ListRunner(CommandRunner):
    """ListRunner displays a received list with user-customisable field list"""

    @property
    @abstractmethod
    def default_format(self) -> List[str]:
        """Default list of fields from response object to display"""

    def response(self, received: Any) -> None:
        display(received, self.default_format)
