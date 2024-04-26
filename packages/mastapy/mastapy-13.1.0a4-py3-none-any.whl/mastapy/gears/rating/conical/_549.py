"""ConicalGearSetRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _370
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Conical", "ConicalGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs import _951
    from mastapy.gears.rating.zerol_bevel import _378
    from mastapy.gears.rating.straight_bevel import _404
    from mastapy.gears.rating.straight_bevel_diff import _407
    from mastapy.gears.rating.spiral_bevel import _411
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _414
    from mastapy.gears.rating.klingelnberg_hypoid import _417
    from mastapy.gears.rating.klingelnberg_conical import _420
    from mastapy.gears.rating.hypoid import _447
    from mastapy.gears.rating.bevel import _563
    from mastapy.gears.rating.agma_gleason_conical import _574
    from mastapy.gears.rating import _362
    from mastapy.gears.analysis import _1227


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetRating",)


Self = TypeVar("Self", bound="ConicalGearSetRating")


class ConicalGearSetRating(_370.GearSetRating):
    """ConicalGearSetRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetRating")

    class _Cast_ConicalGearSetRating:
        """Special nested class for casting ConicalGearSetRating to subclasses."""

        def __init__(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
            parent: "ConicalGearSetRating",
        ):
            self._parent = parent

        @property
        def gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_370.GearSetRating":
            return self._parent._cast(_370.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_362.AbstractGearSetRating":
            from mastapy.gears.rating import _362

            return self._parent._cast(_362.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_1227.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.AbstractGearSetAnalysis)

        @property
        def zerol_bevel_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_378.ZerolBevelGearSetRating":
            from mastapy.gears.rating.zerol_bevel import _378

            return self._parent._cast(_378.ZerolBevelGearSetRating)

        @property
        def straight_bevel_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_404.StraightBevelGearSetRating":
            from mastapy.gears.rating.straight_bevel import _404

            return self._parent._cast(_404.StraightBevelGearSetRating)

        @property
        def straight_bevel_diff_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_407.StraightBevelDiffGearSetRating":
            from mastapy.gears.rating.straight_bevel_diff import _407

            return self._parent._cast(_407.StraightBevelDiffGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_411.SpiralBevelGearSetRating":
            from mastapy.gears.rating.spiral_bevel import _411

            return self._parent._cast(_411.SpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_414.KlingelnbergCycloPalloidSpiralBevelGearSetRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _414

            return self._parent._cast(
                _414.KlingelnbergCycloPalloidSpiralBevelGearSetRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_417.KlingelnbergCycloPalloidHypoidGearSetRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _417

            return self._parent._cast(_417.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_420.KlingelnbergCycloPalloidConicalGearSetRating":
            from mastapy.gears.rating.klingelnberg_conical import _420

            return self._parent._cast(_420.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def hypoid_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_447.HypoidGearSetRating":
            from mastapy.gears.rating.hypoid import _447

            return self._parent._cast(_447.HypoidGearSetRating)

        @property
        def bevel_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_563.BevelGearSetRating":
            from mastapy.gears.rating.bevel import _563

            return self._parent._cast(_563.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "_574.AGMAGleasonConicalGearSetRating":
            from mastapy.gears.rating.agma_gleason_conical import _574

            return self._parent._cast(_574.AGMAGleasonConicalGearSetRating)

        @property
        def conical_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "ConicalGearSetRating":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating_settings(self: Self) -> "_951.BevelHypoidGearRatingSettingsItem":
        """mastapy.gears.gear_designs.BevelHypoidGearRatingSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConicalGearSetRating._Cast_ConicalGearSetRating":
        return self._Cast_ConicalGearSetRating(self)
