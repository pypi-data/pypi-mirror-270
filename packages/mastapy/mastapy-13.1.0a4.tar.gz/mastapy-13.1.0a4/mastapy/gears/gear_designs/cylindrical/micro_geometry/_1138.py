"""ReliefWithDeviation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RELIEF_WITH_DEVIATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry", "ReliefWithDeviation"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import (
        _1124,
        _1125,
        _1126,
        _1135,
        _1136,
        _1137,
        _1140,
        _1141,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ReliefWithDeviation",)


Self = TypeVar("Self", bound="ReliefWithDeviation")


class ReliefWithDeviation(_0.APIBase):
    """ReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _RELIEF_WITH_DEVIATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ReliefWithDeviation")

    class _Cast_ReliefWithDeviation:
        """Special nested class for casting ReliefWithDeviation to subclasses."""

        def __init__(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
            parent: "ReliefWithDeviation",
        ):
            self._parent = parent

        @property
        def lead_form_relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ) -> "_1124.LeadFormReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1124

            return self._parent._cast(_1124.LeadFormReliefWithDeviation)

        @property
        def lead_relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ) -> "_1125.LeadReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1125

            return self._parent._cast(_1125.LeadReliefWithDeviation)

        @property
        def lead_slope_relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ) -> "_1126.LeadSlopeReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1126

            return self._parent._cast(_1126.LeadSlopeReliefWithDeviation)

        @property
        def profile_form_relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ) -> "_1135.ProfileFormReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1135

            return self._parent._cast(_1135.ProfileFormReliefWithDeviation)

        @property
        def profile_relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ) -> "_1136.ProfileReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1136

            return self._parent._cast(_1136.ProfileReliefWithDeviation)

        @property
        def profile_slope_relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ) -> "_1137.ProfileSlopeReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1137

            return self._parent._cast(_1137.ProfileSlopeReliefWithDeviation)

        @property
        def total_lead_relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ) -> "_1140.TotalLeadReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1140

            return self._parent._cast(_1140.TotalLeadReliefWithDeviation)

        @property
        def total_profile_relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ) -> "_1141.TotalProfileReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1141

            return self._parent._cast(_1141.TotalProfileReliefWithDeviation)

        @property
        def relief_with_deviation(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation",
        ) -> "ReliefWithDeviation":
            return self._parent

        def __getattr__(
            self: "ReliefWithDeviation._Cast_ReliefWithDeviation", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ReliefWithDeviation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lower_limit(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LowerLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def relief(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Relief

        if temp is None:
            return 0.0

        return temp

    @property
    def section(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Section

        if temp is None:
            return ""

        return temp

    @property
    def upper_limit(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UpperLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ReliefWithDeviation._Cast_ReliefWithDeviation":
        return self._Cast_ReliefWithDeviation(self)
