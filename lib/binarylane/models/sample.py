from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="Sample")


@attr.s(auto_attribs=True)
class Sample:
    """
    Attributes:
        cpu_usage_percent (float): The usage percentage of all CPU; 100% is the maximum possible even with multiple
            processors.
        cpu_usage_detailed (List[float]): The usage percentage of each virtual CPU.
        memory_usage_bytes (float): The virtual memory used in bytes.
        network_incoming_kbps (float): The incoming network data rate in Kb per second.
        network_outgoing_kbps (float): The outgoing network data rate in Kb per second.
        storage_usage_megabytes (float): The total storage used in MB.
        storage_read_kbps (float): The storage read rate in Kb per second.
        storage_write_kbps (float): The storage write rate in Kb per second.
        storage_read_requests_per_second (float): The storage read requests per second.
        storage_write_requests_per_second (float): The storage write requests per second.
    """

    cpu_usage_percent: float
    cpu_usage_detailed: List[float]
    memory_usage_bytes: float
    network_incoming_kbps: float
    network_outgoing_kbps: float
    storage_usage_megabytes: float
    storage_read_kbps: float
    storage_write_kbps: float
    storage_read_requests_per_second: float
    storage_write_requests_per_second: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cpu_usage_percent = self.cpu_usage_percent
        cpu_usage_detailed = self.cpu_usage_detailed

        memory_usage_bytes = self.memory_usage_bytes
        network_incoming_kbps = self.network_incoming_kbps
        network_outgoing_kbps = self.network_outgoing_kbps
        storage_usage_megabytes = self.storage_usage_megabytes
        storage_read_kbps = self.storage_read_kbps
        storage_write_kbps = self.storage_write_kbps
        storage_read_requests_per_second = self.storage_read_requests_per_second
        storage_write_requests_per_second = self.storage_write_requests_per_second

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpu_usage_percent": cpu_usage_percent,
                "cpu_usage_detailed": cpu_usage_detailed,
                "memory_usage_bytes": memory_usage_bytes,
                "network_incoming_kbps": network_incoming_kbps,
                "network_outgoing_kbps": network_outgoing_kbps,
                "storage_usage_megabytes": storage_usage_megabytes,
                "storage_read_kbps": storage_read_kbps,
                "storage_write_kbps": storage_write_kbps,
                "storage_read_requests_per_second": storage_read_requests_per_second,
                "storage_write_requests_per_second": storage_write_requests_per_second,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cpu_usage_percent = d.pop("cpu_usage_percent")

        cpu_usage_detailed = cast(List[float], d.pop("cpu_usage_detailed"))

        memory_usage_bytes = d.pop("memory_usage_bytes")

        network_incoming_kbps = d.pop("network_incoming_kbps")

        network_outgoing_kbps = d.pop("network_outgoing_kbps")

        storage_usage_megabytes = d.pop("storage_usage_megabytes")

        storage_read_kbps = d.pop("storage_read_kbps")

        storage_write_kbps = d.pop("storage_write_kbps")

        storage_read_requests_per_second = d.pop("storage_read_requests_per_second")

        storage_write_requests_per_second = d.pop("storage_write_requests_per_second")

        sample = cls(
            cpu_usage_percent=cpu_usage_percent,
            cpu_usage_detailed=cpu_usage_detailed,
            memory_usage_bytes=memory_usage_bytes,
            network_incoming_kbps=network_incoming_kbps,
            network_outgoing_kbps=network_outgoing_kbps,
            storage_usage_megabytes=storage_usage_megabytes,
            storage_read_kbps=storage_read_kbps,
            storage_write_kbps=storage_write_kbps,
            storage_read_requests_per_second=storage_read_requests_per_second,
            storage_write_requests_per_second=storage_write_requests_per_second,
        )

        sample.additional_properties = d
        return sample

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
