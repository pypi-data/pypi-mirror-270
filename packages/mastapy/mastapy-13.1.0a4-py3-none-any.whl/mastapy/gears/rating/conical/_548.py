"""ConicalGearSetDutyCycleRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.gears.rating import _369
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Conical", "ConicalGearSetDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.conical import _551
    from mastapy.gears.rating import _362
    from mastapy.gears.analysis import _1227


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetDutyCycleRating",)


Self = TypeVar("Self", bound="ConicalGearSetDutyCycleRating")


class ConicalGearSetDutyCycleRating(_369.GearSetDutyCycleRating):
    """ConicalGearSetDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetDutyCycleRating")

    class _Cast_ConicalGearSetDutyCycleRating:
        """Special nested class for casting ConicalGearSetDutyCycleRating to subclasses."""

        def __init__(
            self: "ConicalGearSetDutyCycleRating._Cast_ConicalGearSetDutyCycleRating",
            parent: "ConicalGearSetDutyCycleRating",
        ):
            self._parent = parent

        @property
        def gear_set_duty_cycle_rating(
            self: "ConicalGearSetDutyCycleRating._Cast_ConicalGearSetDutyCycleRating",
        ) -> "_369.GearSetDutyCycleRating":
            return self._parent._cast(_369.GearSetDutyCycleRating)

        @property
        def abstract_gear_set_rating(
            self: "ConicalGearSetDutyCycleRating._Cast_ConicalGearSetDutyCycleRating",
        ) -> "_362.AbstractGearSetRating":
            from mastapy.gears.rating import _362

            return self._parent._cast(_362.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "ConicalGearSetDutyCycleRating._Cast_ConicalGearSetDutyCycleRating",
        ) -> "_1227.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.AbstractGearSetAnalysis)

        @property
        def conical_gear_set_duty_cycle_rating(
            self: "ConicalGearSetDutyCycleRating._Cast_ConicalGearSetDutyCycleRating",
        ) -> "ConicalGearSetDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetDutyCycleRating._Cast_ConicalGearSetDutyCycleRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_mesh_duty_cycle_ratings(
        self: Self,
    ) -> "List[_551.ConicalMeshDutyCycleRating]":
        """List[mastapy.gears.rating.conical.ConicalMeshDutyCycleRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshDutyCycleRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_mesh_duty_cycle_ratings(
        self: Self,
    ) -> "List[_551.ConicalMeshDutyCycleRating]":
        """List[mastapy.gears.rating.conical.ConicalMeshDutyCycleRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshDutyCycleRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetDutyCycleRating._Cast_ConicalGearSetDutyCycleRating":
        return self._Cast_ConicalGearSetDutyCycleRating(self)
