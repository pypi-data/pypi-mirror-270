"""AGMAGleasonConicalGearSetRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.conical import _549
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.AGMAGleasonConical", "AGMAGleasonConicalGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.zerol_bevel import _378
    from mastapy.gears.rating.straight_bevel import _404
    from mastapy.gears.rating.spiral_bevel import _411
    from mastapy.gears.rating.hypoid import _447
    from mastapy.gears.rating.bevel import _563
    from mastapy.gears.rating import _370, _362
    from mastapy.gears.analysis import _1227


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetRating",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetRating")


class AGMAGleasonConicalGearSetRating(_549.ConicalGearSetRating):
    """AGMAGleasonConicalGearSetRating

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetRating")

    class _Cast_AGMAGleasonConicalGearSetRating:
        """Special nested class for casting AGMAGleasonConicalGearSetRating to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
            parent: "AGMAGleasonConicalGearSetRating",
        ):
            self._parent = parent

        @property
        def conical_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_549.ConicalGearSetRating":
            return self._parent._cast(_549.ConicalGearSetRating)

        @property
        def gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_370.GearSetRating":
            from mastapy.gears.rating import _370

            return self._parent._cast(_370.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_362.AbstractGearSetRating":
            from mastapy.gears.rating import _362

            return self._parent._cast(_362.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_1227.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.AbstractGearSetAnalysis)

        @property
        def zerol_bevel_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_378.ZerolBevelGearSetRating":
            from mastapy.gears.rating.zerol_bevel import _378

            return self._parent._cast(_378.ZerolBevelGearSetRating)

        @property
        def straight_bevel_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_404.StraightBevelGearSetRating":
            from mastapy.gears.rating.straight_bevel import _404

            return self._parent._cast(_404.StraightBevelGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_411.SpiralBevelGearSetRating":
            from mastapy.gears.rating.spiral_bevel import _411

            return self._parent._cast(_411.SpiralBevelGearSetRating)

        @property
        def hypoid_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_447.HypoidGearSetRating":
            from mastapy.gears.rating.hypoid import _447

            return self._parent._cast(_447.HypoidGearSetRating)

        @property
        def bevel_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "_563.BevelGearSetRating":
            from mastapy.gears.rating.bevel import _563

            return self._parent._cast(_563.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "AGMAGleasonConicalGearSetRating":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating":
        return self._Cast_AGMAGleasonConicalGearSetRating(self)
