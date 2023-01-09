from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.sample_set import SampleSet
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="SampleSetResponse")


@attr.s(auto_attribs=True)
class SampleSetResponse:
    """
    Attributes:
        sample_set (Union[Unset, None, SampleSet]):
    """

    sample_set: Union[Unset, None, SampleSet] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sample_set: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.sample_set, Unset):
            sample_set = self.sample_set.to_dict() if self.sample_set else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sample_set is not UNSET:
            field_dict["sample_set"] = sample_set

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _sample_set = d.pop("sample_set", UNSET)
        sample_set: Union[Unset, None, SampleSet]
        if _sample_set is None:
            sample_set = None
        elif isinstance(_sample_set, Unset):
            sample_set = UNSET
        else:
            sample_set = SampleSet.from_dict(_sample_set)

        sample_set_response = cls(
            sample_set=sample_set,
        )

        sample_set_response.additional_properties = d
        return sample_set_response

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
