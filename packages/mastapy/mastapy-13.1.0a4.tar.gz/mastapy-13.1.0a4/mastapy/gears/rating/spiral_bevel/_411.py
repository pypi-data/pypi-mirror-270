"""SpiralBevelGearSetRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.bevel import _563
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.SpiralBevel", "SpiralBevelGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.spiral_bevel import _979
    from mastapy.gears.rating.spiral_bevel import _410, _409
    from mastapy.gears.rating.agma_gleason_conical import _574
    from mastapy.gears.rating.conical import _549
    from mastapy.gears.rating import _370, _362
    from mastapy.gears.analysis import _1227


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetRating",)


Self = TypeVar("Self", bound="SpiralBevelGearSetRating")


class SpiralBevelGearSetRating(_563.BevelGearSetRating):
    """SpiralBevelGearSetRating

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearSetRating")

    class _Cast_SpiralBevelGearSetRating:
        """Special nested class for casting SpiralBevelGearSetRating to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating",
            parent: "SpiralBevelGearSetRating",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_rating(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating",
        ) -> "_563.BevelGearSetRating":
            return self._parent._cast(_563.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating",
        ) -> "_574.AGMAGleasonConicalGearSetRating":
            from mastapy.gears.rating.agma_gleason_conical import _574

            return self._parent._cast(_574.AGMAGleasonConicalGearSetRating)

        @property
        def conical_gear_set_rating(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating",
        ) -> "_549.ConicalGearSetRating":
            from mastapy.gears.rating.conical import _549

            return self._parent._cast(_549.ConicalGearSetRating)

        @property
        def gear_set_rating(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating",
        ) -> "_370.GearSetRating":
            from mastapy.gears.rating import _370

            return self._parent._cast(_370.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating",
        ) -> "_362.AbstractGearSetRating":
            from mastapy.gears.rating import _362

            return self._parent._cast(_362.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating",
        ) -> "_1227.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.AbstractGearSetAnalysis)

        @property
        def spiral_bevel_gear_set_rating(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating",
        ) -> "SpiralBevelGearSetRating":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearSetRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def spiral_bevel_gear_set(self: Self) -> "_979.SpiralBevelGearSetDesign":
        """mastapy.gears.gear_designs.spiral_bevel.SpiralBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def spiral_bevel_gear_ratings(self: Self) -> "List[_410.SpiralBevelGearRating]":
        """List[mastapy.gears.rating.spiral_bevel.SpiralBevelGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_mesh_ratings(self: Self) -> "List[_409.SpiralBevelGearMeshRating]":
        """List[mastapy.gears.rating.spiral_bevel.SpiralBevelGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearSetRating._Cast_SpiralBevelGearSetRating":
        return self._Cast_SpiralBevelGearSetRating(self)
