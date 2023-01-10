from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.domain import Domain
from binarylane.models.links import Links
from binarylane.models.meta import Meta
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="DomainsResponse")


@attr.s(auto_attribs=True)
class DomainsResponse:
    """
    Attributes:
        meta (Meta): Contains metadata about the response, currently this includes the total number of items.
        domains (List[Domain]):
        links (Union[Unset, None, Links]):
    """

    meta: Meta
    domains: List[Domain]
    links: Union[Unset, None, Links] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meta = self.meta.to_dict()

        domains = []
        for domains_item_data in self.domains:
            domains_item = domains_item_data.to_dict()

            domains.append(domains_item)

        links: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict() if self.links else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
                "domains": domains,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        meta = Meta.from_dict(d.pop("meta"))

        domains = []
        _domains = d.pop("domains")
        for domains_item_data in _domains:
            domains_item = Domain.from_dict(domains_item_data)

            domains.append(domains_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, None, Links]
        if _links is None:
            links = None
        elif isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        domains_response = cls(
            meta=meta,
            domains=domains,
            links=links,
        )

        domains_response.additional_properties = d
        return domains_response

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
