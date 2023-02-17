from __future__ import annotations

from typing import Any, Dict, Union

import attr

from binarylane.types import UNSET, Unset


@attr.s(auto_attribs=True)
class Pages:
    last: Union[Unset, None, str] = UNSET
    next_: Union[Unset, None, str] = UNSET
    prev: Union[Unset, None, str] = UNSET
    first: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last = self.last
        next_ = self.next_
        prev = self.prev
        first = self.first

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if last is not UNSET:
            field_dict["last"] = last
        if next_ is not UNSET:
            field_dict["next"] = next_
        if prev is not UNSET:
            field_dict["prev"] = prev
        if first is not UNSET:
            field_dict["first"] = first

        return field_dict
