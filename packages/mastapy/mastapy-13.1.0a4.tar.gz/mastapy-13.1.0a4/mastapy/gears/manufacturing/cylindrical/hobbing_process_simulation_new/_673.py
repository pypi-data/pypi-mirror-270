"""HobbingProcessCalculation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _687
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_CALCULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "HobbingProcessCalculation",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _674,
        _675,
        _676,
        _677,
        _678,
        _682,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HobbingProcessCalculation",)


Self = TypeVar("Self", bound="HobbingProcessCalculation")


class HobbingProcessCalculation(_687.ProcessCalculation):
    """HobbingProcessCalculation

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_CALCULATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HobbingProcessCalculation")

    class _Cast_HobbingProcessCalculation:
        """Special nested class for casting HobbingProcessCalculation to subclasses."""

        def __init__(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
            parent: "HobbingProcessCalculation",
        ):
            self._parent = parent

        @property
        def process_calculation(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
        ) -> "_687.ProcessCalculation":
            return self._parent._cast(_687.ProcessCalculation)

        @property
        def hobbing_process_gear_shape(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
        ) -> "_674.HobbingProcessGearShape":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _674,
            )

            return self._parent._cast(_674.HobbingProcessGearShape)

        @property
        def hobbing_process_lead_calculation(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
        ) -> "_675.HobbingProcessLeadCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _675,
            )

            return self._parent._cast(_675.HobbingProcessLeadCalculation)

        @property
        def hobbing_process_mark_on_shaft(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
        ) -> "_676.HobbingProcessMarkOnShaft":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _676,
            )

            return self._parent._cast(_676.HobbingProcessMarkOnShaft)

        @property
        def hobbing_process_pitch_calculation(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
        ) -> "_677.HobbingProcessPitchCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _677,
            )

            return self._parent._cast(_677.HobbingProcessPitchCalculation)

        @property
        def hobbing_process_profile_calculation(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
        ) -> "_678.HobbingProcessProfileCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _678,
            )

            return self._parent._cast(_678.HobbingProcessProfileCalculation)

        @property
        def hobbing_process_total_modification_calculation(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
        ) -> "_682.HobbingProcessTotalModificationCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _682,
            )

            return self._parent._cast(_682.HobbingProcessTotalModificationCalculation)

        @property
        def hobbing_process_calculation(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
        ) -> "HobbingProcessCalculation":
            return self._parent

        def __getattr__(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HobbingProcessCalculation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "HobbingProcessCalculation._Cast_HobbingProcessCalculation":
        return self._Cast_HobbingProcessCalculation(self)
