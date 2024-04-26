"""ConicalGearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _368
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Conical", "ConicalGearRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _366, _361
    from mastapy.gears.rating.zerol_bevel import _377
    from mastapy.gears.rating.straight_bevel import _403
    from mastapy.gears.rating.straight_bevel_diff import _406
    from mastapy.gears.rating.spiral_bevel import _410
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _413
    from mastapy.gears.rating.klingelnberg_hypoid import _416
    from mastapy.gears.rating.klingelnberg_conical import _419
    from mastapy.gears.rating.hypoid import _446
    from mastapy.gears.rating.bevel import _562
    from mastapy.gears.rating.agma_gleason_conical import _573
    from mastapy.gears.analysis import _1225


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearRating",)


Self = TypeVar("Self", bound="ConicalGearRating")


class ConicalGearRating(_368.GearRating):
    """ConicalGearRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearRating")

    class _Cast_ConicalGearRating:
        """Special nested class for casting ConicalGearRating to subclasses."""

        def __init__(
            self: "ConicalGearRating._Cast_ConicalGearRating",
            parent: "ConicalGearRating",
        ):
            self._parent = parent

        @property
        def gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_368.GearRating":
            return self._parent._cast(_368.GearRating)

        @property
        def abstract_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_361.AbstractGearRating":
            from mastapy.gears.rating import _361

            return self._parent._cast(_361.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_1225.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.AbstractGearAnalysis)

        @property
        def zerol_bevel_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_377.ZerolBevelGearRating":
            from mastapy.gears.rating.zerol_bevel import _377

            return self._parent._cast(_377.ZerolBevelGearRating)

        @property
        def straight_bevel_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_403.StraightBevelGearRating":
            from mastapy.gears.rating.straight_bevel import _403

            return self._parent._cast(_403.StraightBevelGearRating)

        @property
        def straight_bevel_diff_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_406.StraightBevelDiffGearRating":
            from mastapy.gears.rating.straight_bevel_diff import _406

            return self._parent._cast(_406.StraightBevelDiffGearRating)

        @property
        def spiral_bevel_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_410.SpiralBevelGearRating":
            from mastapy.gears.rating.spiral_bevel import _410

            return self._parent._cast(_410.SpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_413.KlingelnbergCycloPalloidSpiralBevelGearRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _413

            return self._parent._cast(
                _413.KlingelnbergCycloPalloidSpiralBevelGearRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_416.KlingelnbergCycloPalloidHypoidGearRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _416

            return self._parent._cast(_416.KlingelnbergCycloPalloidHypoidGearRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_419.KlingelnbergCycloPalloidConicalGearRating":
            from mastapy.gears.rating.klingelnberg_conical import _419

            return self._parent._cast(_419.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def hypoid_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_446.HypoidGearRating":
            from mastapy.gears.rating.hypoid import _446

            return self._parent._cast(_446.HypoidGearRating)

        @property
        def bevel_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_562.BevelGearRating":
            from mastapy.gears.rating.bevel import _562

            return self._parent._cast(_562.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "_573.AGMAGleasonConicalGearRating":
            from mastapy.gears.rating.agma_gleason_conical import _573

            return self._parent._cast(_573.AGMAGleasonConicalGearRating)

        @property
        def conical_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "ConicalGearRating":
            return self._parent

        def __getattr__(self: "ConicalGearRating._Cast_ConicalGearRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def concave_flank_rating(self: Self) -> "_366.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConcaveFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def convex_flank_rating(self: Self) -> "_366.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConvexFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConicalGearRating._Cast_ConicalGearRating":
        return self._Cast_ConicalGearRating(self)
