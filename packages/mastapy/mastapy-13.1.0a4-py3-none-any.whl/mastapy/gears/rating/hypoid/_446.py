"""HypoidGearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating.agma_gleason_conical import _573
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Hypoid", "HypoidGearRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.hypoid import _993
    from mastapy.gears.rating.conical import _547
    from mastapy.gears.rating import _368, _361
    from mastapy.gears.analysis import _1225


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearRating",)


Self = TypeVar("Self", bound="HypoidGearRating")


class HypoidGearRating(_573.AGMAGleasonConicalGearRating):
    """HypoidGearRating

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearRating")

    class _Cast_HypoidGearRating:
        """Special nested class for casting HypoidGearRating to subclasses."""

        def __init__(
            self: "HypoidGearRating._Cast_HypoidGearRating", parent: "HypoidGearRating"
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_rating(
            self: "HypoidGearRating._Cast_HypoidGearRating",
        ) -> "_573.AGMAGleasonConicalGearRating":
            return self._parent._cast(_573.AGMAGleasonConicalGearRating)

        @property
        def conical_gear_rating(
            self: "HypoidGearRating._Cast_HypoidGearRating",
        ) -> "_547.ConicalGearRating":
            from mastapy.gears.rating.conical import _547

            return self._parent._cast(_547.ConicalGearRating)

        @property
        def gear_rating(
            self: "HypoidGearRating._Cast_HypoidGearRating",
        ) -> "_368.GearRating":
            from mastapy.gears.rating import _368

            return self._parent._cast(_368.GearRating)

        @property
        def abstract_gear_rating(
            self: "HypoidGearRating._Cast_HypoidGearRating",
        ) -> "_361.AbstractGearRating":
            from mastapy.gears.rating import _361

            return self._parent._cast(_361.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "HypoidGearRating._Cast_HypoidGearRating",
        ) -> "_1225.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.AbstractGearAnalysis)

        @property
        def hypoid_gear_rating(
            self: "HypoidGearRating._Cast_HypoidGearRating",
        ) -> "HypoidGearRating":
            return self._parent

        def __getattr__(self: "HypoidGearRating._Cast_HypoidGearRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hypoid_gear(self: Self) -> "_993.HypoidGearDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "HypoidGearRating._Cast_HypoidGearRating":
        return self._Cast_HypoidGearRating(self)
