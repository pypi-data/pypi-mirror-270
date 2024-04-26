"""StraightBevelDiffGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.bevel import _1190
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.StraightBevelDiff", "StraightBevelDiffGearDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.bevel import _1195
    from mastapy.gears.gear_designs.agma_gleason_conical import _1203
    from mastapy.gears.gear_designs.conical import _1164
    from mastapy.gears.gear_designs import _955, _956


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearDesign",)


Self = TypeVar("Self", bound="StraightBevelDiffGearDesign")


class StraightBevelDiffGearDesign(_1190.BevelGearDesign):
    """StraightBevelDiffGearDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearDesign")

    class _Cast_StraightBevelDiffGearDesign:
        """Special nested class for casting StraightBevelDiffGearDesign to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearDesign._Cast_StraightBevelDiffGearDesign",
            parent: "StraightBevelDiffGearDesign",
        ):
            self._parent = parent

        @property
        def bevel_gear_design(
            self: "StraightBevelDiffGearDesign._Cast_StraightBevelDiffGearDesign",
        ) -> "_1190.BevelGearDesign":
            return self._parent._cast(_1190.BevelGearDesign)

        @property
        def agma_gleason_conical_gear_design(
            self: "StraightBevelDiffGearDesign._Cast_StraightBevelDiffGearDesign",
        ) -> "_1203.AGMAGleasonConicalGearDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1203

            return self._parent._cast(_1203.AGMAGleasonConicalGearDesign)

        @property
        def conical_gear_design(
            self: "StraightBevelDiffGearDesign._Cast_StraightBevelDiffGearDesign",
        ) -> "_1164.ConicalGearDesign":
            from mastapy.gears.gear_designs.conical import _1164

            return self._parent._cast(_1164.ConicalGearDesign)

        @property
        def gear_design(
            self: "StraightBevelDiffGearDesign._Cast_StraightBevelDiffGearDesign",
        ) -> "_955.GearDesign":
            from mastapy.gears.gear_designs import _955

            return self._parent._cast(_955.GearDesign)

        @property
        def gear_design_component(
            self: "StraightBevelDiffGearDesign._Cast_StraightBevelDiffGearDesign",
        ) -> "_956.GearDesignComponent":
            from mastapy.gears.gear_designs import _956

            return self._parent._cast(_956.GearDesignComponent)

        @property
        def straight_bevel_diff_gear_design(
            self: "StraightBevelDiffGearDesign._Cast_StraightBevelDiffGearDesign",
        ) -> "StraightBevelDiffGearDesign":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearDesign._Cast_StraightBevelDiffGearDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelDiffGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_peak_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowablePeakBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_performance_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowablePerformanceBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def edge_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EdgeRadius

        if temp is None:
            return 0.0

        return temp

    @edge_radius.setter
    @enforce_parameter_types
    def edge_radius(self: Self, value: "float"):
        self.wrapped.EdgeRadius = float(value) if value is not None else 0.0

    @property
    def edge_radius_from(self: Self) -> "_1195.EdgeRadiusType":
        """mastapy.gears.gear_designs.bevel.EdgeRadiusType"""
        temp = self.wrapped.EdgeRadiusFrom

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Bevel.EdgeRadiusType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.bevel._1195", "EdgeRadiusType"
        )(value)

    @edge_radius_from.setter
    @enforce_parameter_types
    def edge_radius_from(self: Self, value: "_1195.EdgeRadiusType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Bevel.EdgeRadiusType"
        )
        self.wrapped.EdgeRadiusFrom = value

    @property
    def limited_point_width_large_end(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LimitedPointWidthLargeEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def limited_point_width_small_end(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LimitedPointWidthSmallEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def max_radius_cutter_blades(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaxRadiusCutterBlades

        if temp is None:
            return 0.0

        return temp

    @property
    def max_radius_interference(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaxRadiusInterference

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_edge_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumEdgeRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_chordal_addendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterChordalAddendum

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_chordal_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterChordalThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearDesign._Cast_StraightBevelDiffGearDesign":
        return self._Cast_StraightBevelDiffGearDesign(self)
