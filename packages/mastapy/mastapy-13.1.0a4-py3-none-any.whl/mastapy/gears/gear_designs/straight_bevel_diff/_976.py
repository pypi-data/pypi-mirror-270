"""StraightBevelDiffMeshedGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.bevel import _1193
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.StraightBevelDiff",
    "StraightBevelDiffMeshedGearDesign",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.agma_gleason_conical import _1206
    from mastapy.gears.gear_designs.conical import _1169
    from mastapy.gears.gear_designs import _956


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffMeshedGearDesign",)


Self = TypeVar("Self", bound="StraightBevelDiffMeshedGearDesign")


class StraightBevelDiffMeshedGearDesign(_1193.BevelMeshedGearDesign):
    """StraightBevelDiffMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_MESHED_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffMeshedGearDesign")

    class _Cast_StraightBevelDiffMeshedGearDesign:
        """Special nested class for casting StraightBevelDiffMeshedGearDesign to subclasses."""

        def __init__(
            self: "StraightBevelDiffMeshedGearDesign._Cast_StraightBevelDiffMeshedGearDesign",
            parent: "StraightBevelDiffMeshedGearDesign",
        ):
            self._parent = parent

        @property
        def bevel_meshed_gear_design(
            self: "StraightBevelDiffMeshedGearDesign._Cast_StraightBevelDiffMeshedGearDesign",
        ) -> "_1193.BevelMeshedGearDesign":
            return self._parent._cast(_1193.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(
            self: "StraightBevelDiffMeshedGearDesign._Cast_StraightBevelDiffMeshedGearDesign",
        ) -> "_1206.AGMAGleasonConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1206

            return self._parent._cast(_1206.AGMAGleasonConicalMeshedGearDesign)

        @property
        def conical_meshed_gear_design(
            self: "StraightBevelDiffMeshedGearDesign._Cast_StraightBevelDiffMeshedGearDesign",
        ) -> "_1169.ConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.conical import _1169

            return self._parent._cast(_1169.ConicalMeshedGearDesign)

        @property
        def gear_design_component(
            self: "StraightBevelDiffMeshedGearDesign._Cast_StraightBevelDiffMeshedGearDesign",
        ) -> "_956.GearDesignComponent":
            from mastapy.gears.gear_designs import _956

            return self._parent._cast(_956.GearDesignComponent)

        @property
        def straight_bevel_diff_meshed_gear_design(
            self: "StraightBevelDiffMeshedGearDesign._Cast_StraightBevelDiffMeshedGearDesign",
        ) -> "StraightBevelDiffMeshedGearDesign":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffMeshedGearDesign._Cast_StraightBevelDiffMeshedGearDesign",
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
        self: Self, instance_to_wrap: "StraightBevelDiffMeshedGearDesign.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def geometry_factor_j(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactorJ

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_topland(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanTopland

        if temp is None:
            return 0.0

        return temp

    @property
    def strength_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrengthFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffMeshedGearDesign._Cast_StraightBevelDiffMeshedGearDesign":
        return self._Cast_StraightBevelDiffMeshedGearDesign(self)
