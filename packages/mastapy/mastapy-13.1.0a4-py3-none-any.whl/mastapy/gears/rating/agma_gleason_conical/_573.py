"""AGMAGleasonConicalGearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.conical import _547
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.AGMAGleasonConical", "AGMAGleasonConicalGearRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.zerol_bevel import _377
    from mastapy.gears.rating.straight_bevel import _403
    from mastapy.gears.rating.spiral_bevel import _410
    from mastapy.gears.rating.hypoid import _446
    from mastapy.gears.rating.bevel import _562
    from mastapy.gears.rating import _368, _361
    from mastapy.gears.analysis import _1225


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearRating",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearRating")


class AGMAGleasonConicalGearRating(_547.ConicalGearRating):
    """AGMAGleasonConicalGearRating

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearRating")

    class _Cast_AGMAGleasonConicalGearRating:
        """Special nested class for casting AGMAGleasonConicalGearRating to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
            parent: "AGMAGleasonConicalGearRating",
        ):
            self._parent = parent

        @property
        def conical_gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ) -> "_547.ConicalGearRating":
            return self._parent._cast(_547.ConicalGearRating)

        @property
        def gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ) -> "_368.GearRating":
            from mastapy.gears.rating import _368

            return self._parent._cast(_368.GearRating)

        @property
        def abstract_gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ) -> "_361.AbstractGearRating":
            from mastapy.gears.rating import _361

            return self._parent._cast(_361.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ) -> "_1225.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.AbstractGearAnalysis)

        @property
        def zerol_bevel_gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ) -> "_377.ZerolBevelGearRating":
            from mastapy.gears.rating.zerol_bevel import _377

            return self._parent._cast(_377.ZerolBevelGearRating)

        @property
        def straight_bevel_gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ) -> "_403.StraightBevelGearRating":
            from mastapy.gears.rating.straight_bevel import _403

            return self._parent._cast(_403.StraightBevelGearRating)

        @property
        def spiral_bevel_gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ) -> "_410.SpiralBevelGearRating":
            from mastapy.gears.rating.spiral_bevel import _410

            return self._parent._cast(_410.SpiralBevelGearRating)

        @property
        def hypoid_gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ) -> "_446.HypoidGearRating":
            from mastapy.gears.rating.hypoid import _446

            return self._parent._cast(_446.HypoidGearRating)

        @property
        def bevel_gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ) -> "_562.BevelGearRating":
            from mastapy.gears.rating.bevel import _562

            return self._parent._cast(_562.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ) -> "AGMAGleasonConicalGearRating":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating":
        return self._Cast_AGMAGleasonConicalGearRating(self)
