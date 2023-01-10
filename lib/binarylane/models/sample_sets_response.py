from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.links import Links
from binarylane.models.meta import Meta
from binarylane.models.sample_set import SampleSet
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="SampleSetsResponse")


@attr.s(auto_attribs=True)
class SampleSetsResponse:
    """
    Attributes:
        meta (Meta): Contains metadata about the response, currently this includes the total number of items.
        sample_sets (List[SampleSet]):
        links (Union[Unset, None, Links]):
    """

    meta: Meta
    sample_sets: List[SampleSet]
    links: Union[Unset, None, Links] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meta = self.meta.to_dict()

        sample_sets = []
        for sample_sets_item_data in self.sample_sets:
            sample_sets_item = sample_sets_item_data.to_dict()

            sample_sets.append(sample_sets_item)

        links: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict() if self.links else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
                "sample_sets": sample_sets,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        meta = Meta.from_dict(d.pop("meta"))

        sample_sets = []
        _sample_sets = d.pop("sample_sets")
        for sample_sets_item_data in _sample_sets:
            sample_sets_item = SampleSet.from_dict(sample_sets_item_data)

            sample_sets.append(sample_sets_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, None, Links]
        if _links is None:
            links = None
        elif isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        sample_sets_response = cls(
            meta=meta,
            sample_sets=sample_sets,
            links=links,
        )

        sample_sets_response.additional_properties = d
        return sample_sets_response

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
