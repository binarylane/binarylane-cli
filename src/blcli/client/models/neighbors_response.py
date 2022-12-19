from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="NeighborsResponse")


@attr.s(auto_attribs=True)
class NeighborsResponse:
    """
    Attributes:
        neighbor_ids (List[List[int]]):
    """

    neighbor_ids: List[List[int]]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        neighbor_ids = []
        for neighbor_ids_item_data in self.neighbor_ids:
            neighbor_ids_item = neighbor_ids_item_data

            neighbor_ids.append(neighbor_ids_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "neighbor_ids": neighbor_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        neighbor_ids = []
        _neighbor_ids = d.pop("neighbor_ids")
        for neighbor_ids_item_data in _neighbor_ids:
            neighbor_ids_item = cast(List[int], neighbor_ids_item_data)

            neighbor_ids.append(neighbor_ids_item)

        neighbors_response = cls(
            neighbor_ids=neighbor_ids,
        )

        neighbors_response.additional_properties = d
        return neighbors_response

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
