"""ProfileReliefWithDeviation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1138
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROFILE_RELIEF_WITH_DEVIATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "ProfileReliefWithDeviation",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1033
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import (
        _1135,
        _1137,
        _1141,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ProfileReliefWithDeviation",)


Self = TypeVar("Self", bound="ProfileReliefWithDeviation")


class ProfileReliefWithDeviation(_1138.ReliefWithDeviation):
    """ProfileReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _PROFILE_RELIEF_WITH_DEVIATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ProfileReliefWithDeviation")

    class _Cast_ProfileReliefWithDeviation:
        """Special nested class for casting ProfileReliefWithDeviation to subclasses."""

        def __init__(
            self: "ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation",
            parent: "ProfileReliefWithDeviation",
        ):
            self._parent = parent

        @property
        def relief_with_deviation(
            self: "ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation",
        ) -> "_1138.ReliefWithDeviation":
            return self._parent._cast(_1138.ReliefWithDeviation)

        @property
        def profile_form_relief_with_deviation(
            self: "ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation",
        ) -> "_1135.ProfileFormReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1135

            return self._parent._cast(_1135.ProfileFormReliefWithDeviation)

        @property
        def profile_slope_relief_with_deviation(
            self: "ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation",
        ) -> "_1137.ProfileSlopeReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1137

            return self._parent._cast(_1137.ProfileSlopeReliefWithDeviation)

        @property
        def total_profile_relief_with_deviation(
            self: "ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation",
        ) -> "_1141.TotalProfileReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1141

            return self._parent._cast(_1141.TotalProfileReliefWithDeviation)

        @property
        def profile_relief_with_deviation(
            self: "ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation",
        ) -> "ProfileReliefWithDeviation":
            return self._parent

        def __getattr__(
            self: "ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ProfileReliefWithDeviation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def profile_relief(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileRelief

        if temp is None:
            return 0.0

        return temp

    @property
    def roll_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def position_on_profile(self: Self) -> "_1033.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PositionOnProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ProfileReliefWithDeviation._Cast_ProfileReliefWithDeviation":
        return self._Cast_ProfileReliefWithDeviation(self)
