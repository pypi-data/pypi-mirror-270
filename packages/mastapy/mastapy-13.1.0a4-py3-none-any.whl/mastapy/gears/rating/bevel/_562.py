"""BevelGearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.agma_gleason_conical import _573
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Bevel", "BevelGearRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.zerol_bevel import _377
    from mastapy.gears.rating.straight_bevel import _403
    from mastapy.gears.rating.spiral_bevel import _410
    from mastapy.gears.rating.conical import _547
    from mastapy.gears.rating import _368, _361
    from mastapy.gears.analysis import _1225


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearRating",)


Self = TypeVar("Self", bound="BevelGearRating")


class BevelGearRating(_573.AGMAGleasonConicalGearRating):
    """BevelGearRating

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearRating")

    class _Cast_BevelGearRating:
        """Special nested class for casting BevelGearRating to subclasses."""

        def __init__(
            self: "BevelGearRating._Cast_BevelGearRating", parent: "BevelGearRating"
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "_573.AGMAGleasonConicalGearRating":
            return self._parent._cast(_573.AGMAGleasonConicalGearRating)

        @property
        def conical_gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "_547.ConicalGearRating":
            from mastapy.gears.rating.conical import _547

            return self._parent._cast(_547.ConicalGearRating)

        @property
        def gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "_368.GearRating":
            from mastapy.gears.rating import _368

            return self._parent._cast(_368.GearRating)

        @property
        def abstract_gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "_361.AbstractGearRating":
            from mastapy.gears.rating import _361

            return self._parent._cast(_361.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "_1225.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.AbstractGearAnalysis)

        @property
        def zerol_bevel_gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "_377.ZerolBevelGearRating":
            from mastapy.gears.rating.zerol_bevel import _377

            return self._parent._cast(_377.ZerolBevelGearRating)

        @property
        def straight_bevel_gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "_403.StraightBevelGearRating":
            from mastapy.gears.rating.straight_bevel import _403

            return self._parent._cast(_403.StraightBevelGearRating)

        @property
        def spiral_bevel_gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "_410.SpiralBevelGearRating":
            from mastapy.gears.rating.spiral_bevel import _410

            return self._parent._cast(_410.SpiralBevelGearRating)

        @property
        def bevel_gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "BevelGearRating":
            return self._parent

        def __getattr__(self: "BevelGearRating._Cast_BevelGearRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BevelGearRating._Cast_BevelGearRating":
        return self._Cast_BevelGearRating(self)
