from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.license_ import License

T = TypeVar("T", bound="ChangeLicenses")


@attr.s(auto_attribs=True)
class ChangeLicenses:
    """
    Attributes:
        licenses (List[License]): The desired set of licenses.
    """

    licenses: List[License]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        licenses = []
        for licenses_item_data in self.licenses:
            licenses_item = licenses_item_data.to_dict()

            licenses.append(licenses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "licenses": licenses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        licenses = []
        _licenses = d.pop("licenses")
        for licenses_item_data in _licenses:
            licenses_item = License.from_dict(licenses_item_data)

            licenses.append(licenses_item)

        change_licenses = cls(
            licenses=licenses,
        )

        change_licenses.additional_properties = d
        return change_licenses

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
