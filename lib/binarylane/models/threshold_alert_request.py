from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.threshold_alert_type import ThresholdAlertType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="ThresholdAlertRequest")


@attr.s(auto_attribs=True)
class ThresholdAlertRequest:
    """
    Attributes:
        alert_type (ThresholdAlertType):
            | Value | Description |
            | ----- | ----------- |
            | cpu | The alert is based off the average percentage of all CPU; 100% is the maximum possible even with
            multiple processors. A high average will prevent the server from responding quickly. |
            | storage-requests | The alert is based off The average number of requests (combined read and write) received by
            the storage subsystem. A high number of requests often indicates swap usage (due to memory exhaustion) and is
            associated with poor performance. |
            | network-incoming | The alert is based off the amount of data going into the server (from the internet and the
            LAN). A sudden increase may indicate the server is the victim of a DOS attack. |
            | network-outgoing | The alert is based off the amount of data coming out of the server (to the internet and the
            LAN). A sudden increase may indicate the server has been hacked and is being used for spam delivery. |
            | data-transfer-used | The alert is based off the percentage of your monthly data transfer limit. |
            | storage-used | The alert is based off the disk space consumed as a percentage of your total disk space. If the
            server runs out of disk space programs may fail to execute or be unable to create new files, or the server may
            become unresponsive. |
            | memory-used | The alert is based off the virtual memory consumed as a percentage of your physical memory.
            Virtual memory includes the swap file so the percentage may exceed 100% indicating that the server has run out
            of physical memory and is relying on swap space, which will generally cause poor performance. |

        enabled (Union[Unset, None, bool]): Do not provide or leave null to keep existing status.
        value (Union[Unset, None, int]): Do not provide or leave null to keep existing value.
    """

    alert_type: ThresholdAlertType
    enabled: Union[Unset, None, bool] = UNSET
    value: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alert_type = self.alert_type.value

        enabled = self.enabled
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_type": alert_type,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alert_type = ThresholdAlertType(d.pop("alert_type"))

        enabled = d.pop("enabled", UNSET)

        value = d.pop("value", UNSET)

        threshold_alert_request = cls(
            alert_type=alert_type,
            enabled=enabled,
            value=value,
        )

        threshold_alert_request.additional_properties = d
        return threshold_alert_request

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
