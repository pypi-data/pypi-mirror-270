"""StraightBevelGearSetRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.bevel import _563
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.StraightBevel", "StraightBevelGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel import _971
    from mastapy.gears.rating.straight_bevel import _403, _402
    from mastapy.gears.rating.agma_gleason_conical import _574
    from mastapy.gears.rating.conical import _549
    from mastapy.gears.rating import _370, _362
    from mastapy.gears.analysis import _1227


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSetRating",)


Self = TypeVar("Self", bound="StraightBevelGearSetRating")


class StraightBevelGearSetRating(_563.BevelGearSetRating):
    """StraightBevelGearSetRating

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearSetRating")

    class _Cast_StraightBevelGearSetRating:
        """Special nested class for casting StraightBevelGearSetRating to subclasses."""

        def __init__(
            self: "StraightBevelGearSetRating._Cast_StraightBevelGearSetRating",
            parent: "StraightBevelGearSetRating",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_rating(
            self: "StraightBevelGearSetRating._Cast_StraightBevelGearSetRating",
        ) -> "_563.BevelGearSetRating":
            return self._parent._cast(_563.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "StraightBevelGearSetRating._Cast_StraightBevelGearSetRating",
        ) -> "_574.AGMAGleasonConicalGearSetRating":
            from mastapy.gears.rating.agma_gleason_conical import _574

            return self._parent._cast(_574.AGMAGleasonConicalGearSetRating)

        @property
        def conical_gear_set_rating(
            self: "StraightBevelGearSetRating._Cast_StraightBevelGearSetRating",
        ) -> "_549.ConicalGearSetRating":
            from mastapy.gears.rating.conical import _549

            return self._parent._cast(_549.ConicalGearSetRating)

        @property
        def gear_set_rating(
            self: "StraightBevelGearSetRating._Cast_StraightBevelGearSetRating",
        ) -> "_370.GearSetRating":
            from mastapy.gears.rating import _370

            return self._parent._cast(_370.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "StraightBevelGearSetRating._Cast_StraightBevelGearSetRating",
        ) -> "_362.AbstractGearSetRating":
            from mastapy.gears.rating import _362

            return self._parent._cast(_362.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "StraightBevelGearSetRating._Cast_StraightBevelGearSetRating",
        ) -> "_1227.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.AbstractGearSetAnalysis)

        @property
        def straight_bevel_gear_set_rating(
            self: "StraightBevelGearSetRating._Cast_StraightBevelGearSetRating",
        ) -> "StraightBevelGearSetRating":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSetRating._Cast_StraightBevelGearSetRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelGearSetRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def straight_bevel_gear_set(self: Self) -> "_971.StraightBevelGearSetDesign":
        """mastapy.gears.gear_designs.straight_bevel.StraightBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_gear_ratings(self: Self) -> "List[_403.StraightBevelGearRating]":
        """List[mastapy.gears.rating.straight_bevel.StraightBevelGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_mesh_ratings(
        self: Self,
    ) -> "List[_402.StraightBevelGearMeshRating]":
        """List[mastapy.gears.rating.straight_bevel.StraightBevelGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearSetRating._Cast_StraightBevelGearSetRating":
        return self._Cast_StraightBevelGearSetRating(self)
