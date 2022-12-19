from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReverseNameserversRequest")


@attr.s(auto_attribs=True)
class ReverseNameserversRequest:
    """
    Attributes:
        reverse_nameservers (Union[Unset, None, List[str]]): A list of all IPv6 reverse name servers for this server.
            Any existing reverse name servers that are omitted from the list will be removed from the server.
    """

    reverse_nameservers: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reverse_nameservers: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.reverse_nameservers, Unset):
            if self.reverse_nameservers is None:
                reverse_nameservers = None
            else:
                reverse_nameservers = self.reverse_nameservers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reverse_nameservers is not UNSET:
            field_dict["reverse_nameservers"] = reverse_nameservers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reverse_nameservers = cast(List[str], d.pop("reverse_nameservers", UNSET))

        reverse_nameservers_request = cls(
            reverse_nameservers=reverse_nameservers,
        )

        reverse_nameservers_request.additional_properties = d
        return reverse_nameservers_request

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
