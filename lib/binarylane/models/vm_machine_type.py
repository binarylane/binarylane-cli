from __future__ import annotations

from enum import Enum


class VmMachineType(str, Enum):
    PC_I440_FX_1_POINT_5 = "pc_i440_fx_1_point_5"
    PC_I440_FX_2_POINT_11 = "pc_i440_fx_2_point_11"
    PC_I440_FX_4POINT_1 = "pc_i440_fx_4point_1"
    PC_I440_FX_4POINT_2 = "pc_i440_fx_4point_2"
    PC_I440_FX_5POINT_0 = "pc_i440_fx_5point_0"
    PC_I440_FX_5POINT_1 = "pc_i440_fx_5point_1"

    def __str__(self) -> str:
        return str(self.value)
