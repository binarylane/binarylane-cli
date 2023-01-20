from __future__ import annotations

import argparse
import logging
from typing import TYPE_CHECKING, List, Optional, Type

from binarylane.types import UNSET

from binarylane.console.parser.attribute import Attribute
from binarylane.console.parser.primitive_attribute import PrimitiveAttribute

if TYPE_CHECKING:
    from binarylane.console.parser.parser import Parser

logger = logging.getLogger(__name__)


class ObjectAttribute(Attribute):
    _init_parameters: List[str]
    _attributes: List[Attribute]
    prefix: str = ""

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
        self.prefix = attribute_name

        self._init_parameters = []
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
        return [attr for attr in self.attributes if attr.attribute_name in self._init_parameters]

    def add_primitive(
        self,
        attribute_name: str,
        attribute_type_hint: object,
        *,
        option_name: Optional[str],
        required: bool,
        description: Optional[str] = None,
        warning: Optional[str] = None,
        action: Optional[Type[argparse.Action]] = None,
    ) -> None:

        if warning:
            self._unsupported(warning)

        if required:
            self._init_parameters.append(attribute_name)

        dest = attribute_name

        if self.prefix:
            dest = f"{self.prefix}_{dest}"

        self._attributes.append(
            PrimitiveAttribute(
                attribute_name=attribute_name,
                attribute_type_hint=attribute_type_hint,
                option_name=option_name,
                dest=dest,
                required=required and self.required,
                description=description,
                action=action,
                metavar=(option_name or attribute_name).replace("-", "_").upper(),
                parent=self,
            )
        )

    def add(self, obj: ObjectAttribute) -> ObjectAttribute:
        obj._set_parent(self)  # pylint: disable=protected-access
        self._attributes.append(obj)

        if obj.required:
            self._init_parameters.append(obj.attribute_name)

        return obj

    def _set_parent(self, obj: ObjectAttribute) -> None:
        self.parent = obj
        if obj.prefix:
            self.prefix = f"{obj.prefix}_{self.attribute_name}"

    def configure(self, parser: Parser) -> None:
        existing_arguments = parser.argument_names

        # If any argument names for this class conflict with existing names, prefix all the argument names
        if any(arg for arg in self.attributes if arg.name_or_flag in existing_arguments):
            self._unsupported("Prefixing option names", False)
            for arg in self.attributes:
                if arg.option_name:
                    arg.option_name = f"{self.attribute_name.replace('_', '-')}-{arg.option_name}"

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
            missing = [attr.name_or_flag for attr in self.init_attributes if init_kwargs[attr.attribute_name] is UNSET]

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
