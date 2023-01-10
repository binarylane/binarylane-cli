from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.links import Links
from binarylane.models.meta import Meta
from binarylane.models.vpc import Vpc
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="VpcsResponse")


@attr.s(auto_attribs=True)
class VpcsResponse:
    """
    Attributes:
        meta (Meta): Contains metadata about the response, currently this includes the total number of items.
        vpcs (List[Vpc]):
        links (Union[Unset, None, Links]):
    """

    meta: Meta
    vpcs: List[Vpc]
    links: Union[Unset, None, Links] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meta = self.meta.to_dict()

        vpcs = []
        for vpcs_item_data in self.vpcs:
            vpcs_item = vpcs_item_data.to_dict()

            vpcs.append(vpcs_item)

        links: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict() if self.links else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
                "vpcs": vpcs,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        meta = Meta.from_dict(d.pop("meta"))

        vpcs = []
        _vpcs = d.pop("vpcs")
        for vpcs_item_data in _vpcs:
            vpcs_item = Vpc.from_dict(vpcs_item_data)

            vpcs.append(vpcs_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, None, Links]
        if _links is None:
            links = None
        elif isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        vpcs_response = cls(
            meta=meta,
            vpcs=vpcs,
            links=links,
        )

        vpcs_response.additional_properties = d
        return vpcs_response

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
