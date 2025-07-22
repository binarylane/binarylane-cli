from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, ClassVar, List, Optional, Sequence, Union

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    import argparse

    from binarylane.console.parser.object_attribute import ObjectAttribute
    from binarylane.console.parser.parser import Parser


class Attribute(ABC):
    raise_on_unsupported: ClassVar[bool] = False

    parent: Optional[ObjectAttribute]
    attribute_name: str
    attribute_type: type
    # if init is True, this attribute is required by the parent's __init__ method
    init: bool
    # if required is True, this attribute is mandatory in the command-line parsing sense
    required: bool
    option_names: List[str]
    description: Optional[str]

    def __init__(
        self,
        attribute_name: str,
        attribute_type: type,
        *,
        required: bool,
        option_name: Union[str, Sequence[str], None],
        description: Optional[str],
    ) -> None:
        self.attribute_name = attribute_name
        self.attribute_type = attribute_type
        self.init = required
        self.required = required
        self.option_names = [option_name] if isinstance(option_name, str) else list(option_name) if option_name else []
        self.description = description

    @property
    def has_default_value(self) -> bool:
        return False

    @property
    def usage(self) -> Optional[str]:
        return None

    @property
    def option_name(self) -> Optional[str]:
        return self.option_names[0] if self.option_names else None

    @property
    def name_or_flag(self) -> Sequence[str]:
        if not self.option_names:
            return [self.attribute_name]
        return [f"--{opt}" for opt in self.option_names]

    @property
    def attributes(self) -> List[Attribute]:
        return []

    @property
    def group_name(self) -> Optional[str]:
        return self.parent.group_name if self.parent else None

    @abstractmethod
    def configure(self, parser: Parser) -> None: ...

    @abstractmethod
    def construct(self, parser: Parser, parsed: argparse.Namespace) -> object: ...

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
