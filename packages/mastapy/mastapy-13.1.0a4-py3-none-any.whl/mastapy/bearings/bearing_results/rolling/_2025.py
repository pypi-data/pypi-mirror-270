"""LoadedCylindricalRollerBearingDutyCycle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2041
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_CYLINDRICAL_ROLLER_BEARING_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedCylindricalRollerBearingDutyCycle",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1977, _1974, _1966


__docformat__ = "restructuredtext en"
__all__ = ("LoadedCylindricalRollerBearingDutyCycle",)


Self = TypeVar("Self", bound="LoadedCylindricalRollerBearingDutyCycle")


class LoadedCylindricalRollerBearingDutyCycle(
    _2041.LoadedNonBarrelRollerBearingDutyCycle
):
    """LoadedCylindricalRollerBearingDutyCycle

    This is a mastapy class.
    """

    TYPE = _LOADED_CYLINDRICAL_ROLLER_BEARING_DUTY_CYCLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedCylindricalRollerBearingDutyCycle"
    )

    class _Cast_LoadedCylindricalRollerBearingDutyCycle:
        """Special nested class for casting LoadedCylindricalRollerBearingDutyCycle to subclasses."""

        def __init__(
            self: "LoadedCylindricalRollerBearingDutyCycle._Cast_LoadedCylindricalRollerBearingDutyCycle",
            parent: "LoadedCylindricalRollerBearingDutyCycle",
        ):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_bearing_duty_cycle(
            self: "LoadedCylindricalRollerBearingDutyCycle._Cast_LoadedCylindricalRollerBearingDutyCycle",
        ) -> "_2041.LoadedNonBarrelRollerBearingDutyCycle":
            return self._parent._cast(_2041.LoadedNonBarrelRollerBearingDutyCycle)

        @property
        def loaded_rolling_bearing_duty_cycle(
            self: "LoadedCylindricalRollerBearingDutyCycle._Cast_LoadedCylindricalRollerBearingDutyCycle",
        ) -> "_1977.LoadedRollingBearingDutyCycle":
            from mastapy.bearings.bearing_results import _1977

            return self._parent._cast(_1977.LoadedRollingBearingDutyCycle)

        @property
        def loaded_non_linear_bearing_duty_cycle_results(
            self: "LoadedCylindricalRollerBearingDutyCycle._Cast_LoadedCylindricalRollerBearingDutyCycle",
        ) -> "_1974.LoadedNonLinearBearingDutyCycleResults":
            from mastapy.bearings.bearing_results import _1974

            return self._parent._cast(_1974.LoadedNonLinearBearingDutyCycleResults)

        @property
        def loaded_bearing_duty_cycle(
            self: "LoadedCylindricalRollerBearingDutyCycle._Cast_LoadedCylindricalRollerBearingDutyCycle",
        ) -> "_1966.LoadedBearingDutyCycle":
            from mastapy.bearings.bearing_results import _1966

            return self._parent._cast(_1966.LoadedBearingDutyCycle)

        @property
        def loaded_cylindrical_roller_bearing_duty_cycle(
            self: "LoadedCylindricalRollerBearingDutyCycle._Cast_LoadedCylindricalRollerBearingDutyCycle",
        ) -> "LoadedCylindricalRollerBearingDutyCycle":
            return self._parent

        def __getattr__(
            self: "LoadedCylindricalRollerBearingDutyCycle._Cast_LoadedCylindricalRollerBearingDutyCycle",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "LoadedCylindricalRollerBearingDutyCycle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def permissible_continuous_axial_load_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleContinuousAxialLoadSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedCylindricalRollerBearingDutyCycle._Cast_LoadedCylindricalRollerBearingDutyCycle":
        return self._Cast_LoadedCylindricalRollerBearingDutyCycle(self)
