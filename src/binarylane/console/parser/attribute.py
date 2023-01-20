from __future__ import annotations

import argparse
import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, ClassVar, List, Optional

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from binarylane.console.parser.object_attribute import ObjectAttribute
    from binarylane.console.parser.parser import Parser


class Attribute(ABC):
    raise_on_unsupported: ClassVar[bool] = False

    parent: Optional[ObjectAttribute]
    attribute_name: str
    attribute_type: type
    required: bool
    option_name: Optional[str]
    description: Optional[str]

    def __init__(
        self,
        attribute_name: str,
        attribute_type: type,
        *,
        required: bool,
        option_name: Optional[str],
        description: Optional[str],
    ) -> None:
        self.attribute_name = attribute_name
        self.attribute_type = attribute_type
        self.required = required
        self.option_name = option_name
        self.description = description

    @property
    def has_default_value(self) -> bool:
        return False

    @property
    def usage(self) -> Optional[str]:
        return None

    @property
    def name_or_flag(self) -> str:
        return f"--{self.option_name}" if self.option_name else self.attribute_name

    @property
    def attributes(self) -> List[Attribute]:
        return []

    @property
    def group_name(self) -> Optional[str]:
        return self.parent.group_name if self.parent else None

    @abstractmethod
    def configure(self, parser: Parser) -> None:
        ...

    @abstractmethod
    def construct(self, parser: Parser, parsed: argparse.Namespace) -> object:
        ...

    def _unsupported(self, message: str, error: bool = True) -> None:
        """Report that command parsing is not likely to work correctly"""

        top = self
        while top.parent:
            top = top.parent
        if TYPE_CHECKING:
            assert isinstance(top, ObjectAttribute)
        message = f"{top.attribute_type.__module__}: {self.attribute_name} - {message}"

        if error and self.raise_on_unsupported:
            raise NotImplementedError(message)

        logger.log(logging.ERROR if error else logging.WARNING, message)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(varname={self.attribute_name!r}, required={self.required!r})"
