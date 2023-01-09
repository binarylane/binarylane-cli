from __future__ import annotations

import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="DataUsage")


@attr.s(auto_attribs=True)
class DataUsage:
    """
    Attributes:
        server_id (int): The ID of the server that this data transfer usage refers to.
        expires (datetime.datetime): The date and time in ISO8601 format that the current billing period expires.
        transfer_gigabytes (int): The included data transfer for this server in this period in GB.
        current_transfer_usage_gigabytes (float): The used data transfer for this server in this period in GB.
            If you have more than one server, please see our data pooling policy: this value may include excess data
            transfer used by other servers or may have 'offloaded' excess data transfer to other servers with spare
            capacity.
        transfer_period_end (datetime.datetime): The date and time in ISO8601 format that the data transfer limit period
            ended (if it is completed) or when it will end (if this is the current period).
    """

    server_id: int
    expires: datetime.datetime
    transfer_gigabytes: int
    current_transfer_usage_gigabytes: float
    transfer_period_end: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server_id = self.server_id
        expires = self.expires.isoformat()

        transfer_gigabytes = self.transfer_gigabytes
        current_transfer_usage_gigabytes = self.current_transfer_usage_gigabytes
        transfer_period_end = self.transfer_period_end.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server_id": server_id,
                "expires": expires,
                "transfer_gigabytes": transfer_gigabytes,
                "current_transfer_usage_gigabytes": current_transfer_usage_gigabytes,
                "transfer_period_end": transfer_period_end,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server_id = d.pop("server_id")

        expires = isoparse(d.pop("expires"))

        transfer_gigabytes = d.pop("transfer_gigabytes")

        current_transfer_usage_gigabytes = d.pop("current_transfer_usage_gigabytes")

        transfer_period_end = isoparse(d.pop("transfer_period_end"))

        data_usage = cls(
            server_id=server_id,
            expires=expires,
            transfer_gigabytes=transfer_gigabytes,
            current_transfer_usage_gigabytes=current_transfer_usage_gigabytes,
            transfer_period_end=transfer_period_end,
        )

        data_usage.additional_properties = d
        return data_usage

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
