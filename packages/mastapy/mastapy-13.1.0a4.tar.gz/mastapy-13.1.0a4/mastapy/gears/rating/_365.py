"""GearDutyCycleRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _361
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "GearDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _369, _366, _368
    from mastapy.gears.rating.worm import _379
    from mastapy.gears.rating.face import _452
    from mastapy.gears.rating.cylindrical import _462
    from mastapy.gears.rating.conical import _545
    from mastapy.gears.rating.concept import _555
    from mastapy.gears.analysis import _1225


__docformat__ = "restructuredtext en"
__all__ = ("GearDutyCycleRating",)


Self = TypeVar("Self", bound="GearDutyCycleRating")


class GearDutyCycleRating(_361.AbstractGearRating):
    """GearDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _GEAR_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearDutyCycleRating")

    class _Cast_GearDutyCycleRating:
        """Special nested class for casting GearDutyCycleRating to subclasses."""

        def __init__(
            self: "GearDutyCycleRating._Cast_GearDutyCycleRating",
            parent: "GearDutyCycleRating",
        ):
            self._parent = parent

        @property
        def abstract_gear_rating(
            self: "GearDutyCycleRating._Cast_GearDutyCycleRating",
        ) -> "_361.AbstractGearRating":
            return self._parent._cast(_361.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "GearDutyCycleRating._Cast_GearDutyCycleRating",
        ) -> "_1225.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.AbstractGearAnalysis)

        @property
        def worm_gear_duty_cycle_rating(
            self: "GearDutyCycleRating._Cast_GearDutyCycleRating",
        ) -> "_379.WormGearDutyCycleRating":
            from mastapy.gears.rating.worm import _379

            return self._parent._cast(_379.WormGearDutyCycleRating)

        @property
        def face_gear_duty_cycle_rating(
            self: "GearDutyCycleRating._Cast_GearDutyCycleRating",
        ) -> "_452.FaceGearDutyCycleRating":
            from mastapy.gears.rating.face import _452

            return self._parent._cast(_452.FaceGearDutyCycleRating)

        @property
        def cylindrical_gear_duty_cycle_rating(
            self: "GearDutyCycleRating._Cast_GearDutyCycleRating",
        ) -> "_462.CylindricalGearDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _462

            return self._parent._cast(_462.CylindricalGearDutyCycleRating)

        @property
        def conical_gear_duty_cycle_rating(
            self: "GearDutyCycleRating._Cast_GearDutyCycleRating",
        ) -> "_545.ConicalGearDutyCycleRating":
            from mastapy.gears.rating.conical import _545

            return self._parent._cast(_545.ConicalGearDutyCycleRating)

        @property
        def concept_gear_duty_cycle_rating(
            self: "GearDutyCycleRating._Cast_GearDutyCycleRating",
        ) -> "_555.ConceptGearDutyCycleRating":
            from mastapy.gears.rating.concept import _555

            return self._parent._cast(_555.ConceptGearDutyCycleRating)

        @property
        def gear_duty_cycle_rating(
            self: "GearDutyCycleRating._Cast_GearDutyCycleRating",
        ) -> "GearDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "GearDutyCycleRating._Cast_GearDutyCycleRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def damage_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DamageBending

        if temp is None:
            return 0.0

        return temp

    @property
    def damage_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DamageContact

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_set_design_duty_cycle(self: Self) -> "_369.GearSetDutyCycleRating":
        """mastapy.gears.rating.GearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDesignDutyCycle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def left_flank_rating(self: Self) -> "_366.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank_rating(self: Self) -> "_366.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_ratings(self: Self) -> "List[_368.GearRating]":
        """List[mastapy.gears.rating.GearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "GearDutyCycleRating._Cast_GearDutyCycleRating":
        return self._Cast_GearDutyCycleRating(self)
