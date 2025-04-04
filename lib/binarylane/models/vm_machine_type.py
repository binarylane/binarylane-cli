from __future__ import annotations

from enum import Enum


class VmMachineType(str, Enum):
    PC_I440FX_1POINT5 = "pc_i440fx_1point5"
    PC_I440FX_2POINT11 = "pc_i440fx_2point11"
    PC_I440FX_4POINT1 = "pc_i440fx_4point1"
    PC_I440FX_4POINT2 = "pc_i440fx_4point2"
    PC_I440FX_5POINT0 = "pc_i440fx_5point0"
    PC_I440FX_5POINT1 = "pc_i440fx_5point1"
    PC_I440FX_7POINT2 = "pc_i440fx_7point2"
    PC_I440FX_8POINT2 = "pc_i440fx_8point2"

    def __str__(self) -> str:
        return str(self.value)
