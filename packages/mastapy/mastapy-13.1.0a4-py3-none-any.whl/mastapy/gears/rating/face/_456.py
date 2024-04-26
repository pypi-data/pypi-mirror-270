"""FaceGearSetDutyCycleRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating import _369
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Face", "FaceGearSetDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _362
    from mastapy.gears.analysis import _1227


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetDutyCycleRating",)


Self = TypeVar("Self", bound="FaceGearSetDutyCycleRating")


class FaceGearSetDutyCycleRating(_369.GearSetDutyCycleRating):
    """FaceGearSetDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetDutyCycleRating")

    class _Cast_FaceGearSetDutyCycleRating:
        """Special nested class for casting FaceGearSetDutyCycleRating to subclasses."""

        def __init__(
            self: "FaceGearSetDutyCycleRating._Cast_FaceGearSetDutyCycleRating",
            parent: "FaceGearSetDutyCycleRating",
        ):
            self._parent = parent

        @property
        def gear_set_duty_cycle_rating(
            self: "FaceGearSetDutyCycleRating._Cast_FaceGearSetDutyCycleRating",
        ) -> "_369.GearSetDutyCycleRating":
            return self._parent._cast(_369.GearSetDutyCycleRating)

        @property
        def abstract_gear_set_rating(
            self: "FaceGearSetDutyCycleRating._Cast_FaceGearSetDutyCycleRating",
        ) -> "_362.AbstractGearSetRating":
            from mastapy.gears.rating import _362

            return self._parent._cast(_362.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "FaceGearSetDutyCycleRating._Cast_FaceGearSetDutyCycleRating",
        ) -> "_1227.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.AbstractGearSetAnalysis)

        @property
        def face_gear_set_duty_cycle_rating(
            self: "FaceGearSetDutyCycleRating._Cast_FaceGearSetDutyCycleRating",
        ) -> "FaceGearSetDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "FaceGearSetDutyCycleRating._Cast_FaceGearSetDutyCycleRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetDutyCycleRating._Cast_FaceGearSetDutyCycleRating":
        return self._Cast_FaceGearSetDutyCycleRating(self)
