"""SpiralBevelGearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating.bevel import _562
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.SpiralBevel", "SpiralBevelGearRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.spiral_bevel import _977
    from mastapy.gears.rating.agma_gleason_conical import _573
    from mastapy.gears.rating.conical import _547
    from mastapy.gears.rating import _368, _361
    from mastapy.gears.analysis import _1225


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearRating",)


Self = TypeVar("Self", bound="SpiralBevelGearRating")


class SpiralBevelGearRating(_562.BevelGearRating):
    """SpiralBevelGearRating

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearRating")

    class _Cast_SpiralBevelGearRating:
        """Special nested class for casting SpiralBevelGearRating to subclasses."""

        def __init__(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating",
            parent: "SpiralBevelGearRating",
        ):
            self._parent = parent

        @property
        def bevel_gear_rating(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating",
        ) -> "_562.BevelGearRating":
            return self._parent._cast(_562.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating",
        ) -> "_573.AGMAGleasonConicalGearRating":
            from mastapy.gears.rating.agma_gleason_conical import _573

            return self._parent._cast(_573.AGMAGleasonConicalGearRating)

        @property
        def conical_gear_rating(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating",
        ) -> "_547.ConicalGearRating":
            from mastapy.gears.rating.conical import _547

            return self._parent._cast(_547.ConicalGearRating)

        @property
        def gear_rating(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating",
        ) -> "_368.GearRating":
            from mastapy.gears.rating import _368

            return self._parent._cast(_368.GearRating)

        @property
        def abstract_gear_rating(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating",
        ) -> "_361.AbstractGearRating":
            from mastapy.gears.rating import _361

            return self._parent._cast(_361.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating",
        ) -> "_1225.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.AbstractGearAnalysis)

        @property
        def spiral_bevel_gear_rating(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating",
        ) -> "SpiralBevelGearRating":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearRating._Cast_SpiralBevelGearRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def spiral_bevel_gear(self: Self) -> "_977.SpiralBevelGearDesign":
        """mastapy.gears.gear_designs.spiral_bevel.SpiralBevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "SpiralBevelGearRating._Cast_SpiralBevelGearRating":
        return self._Cast_SpiralBevelGearRating(self)
