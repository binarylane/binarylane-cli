from __future__ import annotations

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from binarylane.models.threshold_alert_type import ThresholdAlertType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="ThresholdAlert")


@attr.s(auto_attribs=True)
class ThresholdAlert:
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

        enabled (bool): If a threshold alert is not enabled it will not generate warnings for the user.
        value (int): The threshold value of the alert. Refer to the documentation for each threshold alert type for what
            this value measures in the context of the alert type.
        current_value (Union[Unset, None, int]): The last measured value for this alert type over the threshold alert
            period. Refer to the documentation for each threshold alert type for what this value measures in the context of
            the alert type. If there is no measured value in the threshold alert period this will be null.
        last_raised (Union[Unset, None, datetime.datetime]): The date and time (if any) in ISO8601 format of the last
            time this alert was raised. An alert may not be raised again until it has been cleared.
        last_cleared (Union[Unset, None, datetime.datetime]): The date and time (if any) in ISO8601 format of the last
            time this alert was cleared. An alert may not be raised again until a minimum duration has passed since it was
            last cleared.
    """

    alert_type: ThresholdAlertType
    enabled: bool
    value: int
    current_value: Union[Unset, None, int] = UNSET
    last_raised: Union[Unset, None, datetime.datetime] = UNSET
    last_cleared: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alert_type = self.alert_type.value

        enabled = self.enabled
        value = self.value
        current_value = self.current_value
        last_raised: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_raised, Unset):
            last_raised = self.last_raised.isoformat() if self.last_raised else None

        last_cleared: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_cleared, Unset):
            last_cleared = self.last_cleared.isoformat() if self.last_cleared else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_type": alert_type,
                "enabled": enabled,
                "value": value,
            }
        )
        if current_value is not UNSET:
            field_dict["current_value"] = current_value
        if last_raised is not UNSET:
            field_dict["last_raised"] = last_raised
        if last_cleared is not UNSET:
            field_dict["last_cleared"] = last_cleared

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alert_type = ThresholdAlertType(d.pop("alert_type"))

        enabled = d.pop("enabled")

        value = d.pop("value")

        current_value = d.pop("current_value", UNSET)

        _last_raised = d.pop("last_raised", UNSET)
        last_raised: Union[Unset, None, datetime.datetime]
        if _last_raised is None:
            last_raised = None
        elif isinstance(_last_raised, Unset):
            last_raised = UNSET
        else:
            last_raised = isoparse(_last_raised)

        _last_cleared = d.pop("last_cleared", UNSET)
        last_cleared: Union[Unset, None, datetime.datetime]
        if _last_cleared is None:
            last_cleared = None
        elif isinstance(_last_cleared, Unset):
            last_cleared = UNSET
        else:
            last_cleared = isoparse(_last_cleared)

        threshold_alert = cls(
            alert_type=alert_type,
            enabled=enabled,
            value=value,
            current_value=current_value,
            last_raised=last_raised,
            last_cleared=last_cleared,
        )

        threshold_alert.additional_properties = d
        return threshold_alert

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
