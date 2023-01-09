from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.change_kernel_type import ChangeKernelType

T = TypeVar("T", bound="ChangeKernel")


@attr.s(auto_attribs=True)
class ChangeKernel:
    """Change the Kernel of a Server

    Attributes:
        type (ChangeKernelType):
        kernel (int): The ID of the kernel to use.
    """

    type: ChangeKernelType
    kernel: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        kernel = self.kernel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "kernel": kernel,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ChangeKernelType(d.pop("type"))

        kernel = d.pop("kernel")

        change_kernel = cls(
            type=type,
            kernel=kernel,
        )

        change_kernel.additional_properties = d
        return change_kernel

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
