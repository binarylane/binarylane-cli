from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.links import Links
from binarylane.models.meta import Meta
from binarylane.models.software import Software
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="SoftwaresResponse")


@attr.s(auto_attribs=True)
class SoftwaresResponse:
    """
    Attributes:
        meta (Meta): Contains metadata about the response, currently this includes the total number of items.
        software (List[Software]):
        links (Union[Unset, None, Links]):
    """

    meta: Meta
    software: List[Software]
    links: Union[Unset, None, Links] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meta = self.meta.to_dict()

        software = []
        for software_item_data in self.software:
            software_item = software_item_data.to_dict()

            software.append(software_item)

        links: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict() if self.links else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
                "software": software,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        meta = Meta.from_dict(d.pop("meta"))

        software = []
        _software = d.pop("software")
        for software_item_data in _software:
            software_item = Software.from_dict(software_item_data)

            software.append(software_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, None, Links]
        if _links is None:
            links = None
        elif isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        softwares_response = cls(
            meta=meta,
            software=software,
            links=links,
        )

        softwares_response.additional_properties = d
        return softwares_response

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
