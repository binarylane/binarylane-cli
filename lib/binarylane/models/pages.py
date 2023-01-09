from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="Pages")


@attr.s(auto_attribs=True)
class Pages:
    """Provides links to first, last, next and previous pages if more than a single page of results exists.

    Attributes:
        last (Union[Unset, None, str]): A link to the last page of items if this is not the last page.
        next_ (Union[Unset, None, str]): A link to the next page of items if this is not the last page.
        prev (Union[Unset, None, str]): A link to the previous page of items if this is not the first page.
        first (Union[Unset, None, str]): A link to the first page of items if this is not the first page.
    """

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
        field_dict.update(self.additional_properties)
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

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        last = d.pop("last", UNSET)

        next_ = d.pop("next", UNSET)

        prev = d.pop("prev", UNSET)

        first = d.pop("first", UNSET)

        pages = cls(
            last=last,
            next_=next_,
            prev=prev,
            first=first,
        )

        pages.additional_properties = d
        return pages

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
