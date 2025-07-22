from __future__ import annotations

import logging
from typing import TYPE_CHECKING, List, Optional, TypeVar

from binarylane.types import UNSET

from binarylane.console.parser.attribute import Attribute

if TYPE_CHECKING:
    import argparse

    from binarylane.console.parser.parser import Parser

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=Attribute)


class ObjectAttribute(Attribute):
    _attributes: List[Attribute]

    def __init__(
        self,
        attribute_name: str,
        attribute_type: type,
        *,
        required: bool,
        option_name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> None:
        super().__init__(
            attribute_name,
            attribute_type,
            required=required,
            option_name=option_name or attribute_name,
            description=description,
        )
        self._attributes = []

    @property
    def title(self) -> str:
        return self.attribute_name.replace("_", " ").title()

    @property
    def group_name(self) -> Optional[str]:
        group_name = None if self.required else self.attribute_name.title().replace("_", " ")

        # FIXME: Use OpenAPI exetension to do this
        if group_name == "Options":
            group_name = self.parent.group_name if self.parent else None

        return group_name

    @property
    def attributes(self) -> List[Attribute]:
        return list(self._attributes)  # return new list to prevent modifying our copy

    @property
    def init_attributes(self) -> List[Attribute]:
        return [attr for attr in self.attributes if attr.init]

    def add(self, obj: T) -> T:
        if not self.required:
            obj.required = False

        obj.parent = self
        self._attributes.append(obj)
        return obj

    def configure(self, parser: Parser) -> None:
        existing_arguments = parser.argument_names

        # If any argument names for this class conflict with existing names, prefix all the argument names
        if any(arg for arg in self.attributes if any(opt for opt in arg.name_or_flag if opt in existing_arguments)):
            self._unsupported("Prefixing option names", False)
            for arg in self.attributes:
                arg.option_names = [f"{self.attribute_name.replace('_', '-')}-{opt}" for opt in arg.option_names]

        group = self.group_name
        if group:
            parser.add_group(group, self.description)

        for attr in self.attributes:
            attr.configure(parser)

    def construct(self, parser: Parser, parsed: argparse.Namespace) -> object:
        init_kwargs = {attr.attribute_name: attr.construct(parser, parsed) for attr in self.init_attributes}
        all_options = {
            attr.attribute_name: attr.construct(parser, parsed)
            for attr in self.attributes
            if attr not in self.init_attributes
        }
        optionals = {varname: value for varname, value in all_options.items() if value is not UNSET}

        # If there are required attributes for the class constructor
        if init_kwargs:
            # See if any were not provided a value
            missing = [
                attr.name_or_flag[0] for attr in self.init_attributes if init_kwargs[attr.attribute_name] is UNSET
            ]

            # If one or more required attributes did not receive a value:
            if missing:
                # single-value enums are not required, as they default to the only possible value
                required = len([True for attr in self.init_attributes if not attr.has_default_value])

                # If some required values were provided, but not all, that is an error.
                # If no required values were provided, but an optional was, that is an error.
                if len(missing) < required or optionals:
                    parser.error(f"the following arguments are required: {', '.join(missing)}")

                # If all required arguments are missing, skip construction entirely
                return UNSET

        # If object has no required attributes and all optional attributes are unset, skip construction
        if not init_kwargs and not optionals and not self.required:
            return UNSET

        # All required constructor arguments present, proceed with object construction
        instance = self.attribute_type(**init_kwargs)
        vars(instance).update(optionals)
        return instance


class JsonBody(ObjectAttribute):
    def __init__(self, cls: type) -> None:
        super().__init__("json_body", cls, required=True)
        self.prefix = "json_body"
        self.required = True


class Mapping(ObjectAttribute):
    def __init__(self, cls: type) -> None:
        super().__init__("", cls, required=True)
        self.prefix = ""
        self.parent = None

    def add_json_body(self, cls: type) -> JsonBody:
        json_body = JsonBody(cls)
        self.add(json_body)
        return json_body
