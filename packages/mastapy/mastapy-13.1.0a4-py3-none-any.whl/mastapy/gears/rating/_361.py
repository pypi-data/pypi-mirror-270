"""AbstractGearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1225
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "AbstractGearRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _365, _368
    from mastapy.gears.rating.zerol_bevel import _377
    from mastapy.gears.rating.worm import _379, _381
    from mastapy.gears.rating.straight_bevel import _403
    from mastapy.gears.rating.straight_bevel_diff import _406
    from mastapy.gears.rating.spiral_bevel import _410
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _413
    from mastapy.gears.rating.klingelnberg_hypoid import _416
    from mastapy.gears.rating.klingelnberg_conical import _419
    from mastapy.gears.rating.hypoid import _446
    from mastapy.gears.rating.face import _452, _455
    from mastapy.gears.rating.cylindrical import _462, _467
    from mastapy.gears.rating.conical import _545, _547
    from mastapy.gears.rating.concept import _555, _558
    from mastapy.gears.rating.bevel import _562
    from mastapy.gears.rating.agma_gleason_conical import _573


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearRating",)


Self = TypeVar("Self", bound="AbstractGearRating")


class AbstractGearRating(_1225.AbstractGearAnalysis):
    """AbstractGearRating

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearRating")

    class _Cast_AbstractGearRating:
        """Special nested class for casting AbstractGearRating to subclasses."""

        def __init__(
            self: "AbstractGearRating._Cast_AbstractGearRating",
            parent: "AbstractGearRating",
        ):
            self._parent = parent

        @property
        def abstract_gear_analysis(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_1225.AbstractGearAnalysis":
            return self._parent._cast(_1225.AbstractGearAnalysis)

        @property
        def gear_duty_cycle_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_365.GearDutyCycleRating":
            from mastapy.gears.rating import _365

            return self._parent._cast(_365.GearDutyCycleRating)

        @property
        def gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_368.GearRating":
            from mastapy.gears.rating import _368

            return self._parent._cast(_368.GearRating)

        @property
        def zerol_bevel_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_377.ZerolBevelGearRating":
            from mastapy.gears.rating.zerol_bevel import _377

            return self._parent._cast(_377.ZerolBevelGearRating)

        @property
        def worm_gear_duty_cycle_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_379.WormGearDutyCycleRating":
            from mastapy.gears.rating.worm import _379

            return self._parent._cast(_379.WormGearDutyCycleRating)

        @property
        def worm_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_381.WormGearRating":
            from mastapy.gears.rating.worm import _381

            return self._parent._cast(_381.WormGearRating)

        @property
        def straight_bevel_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_403.StraightBevelGearRating":
            from mastapy.gears.rating.straight_bevel import _403

            return self._parent._cast(_403.StraightBevelGearRating)

        @property
        def straight_bevel_diff_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_406.StraightBevelDiffGearRating":
            from mastapy.gears.rating.straight_bevel_diff import _406

            return self._parent._cast(_406.StraightBevelDiffGearRating)

        @property
        def spiral_bevel_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_410.SpiralBevelGearRating":
            from mastapy.gears.rating.spiral_bevel import _410

            return self._parent._cast(_410.SpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_413.KlingelnbergCycloPalloidSpiralBevelGearRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _413

            return self._parent._cast(
                _413.KlingelnbergCycloPalloidSpiralBevelGearRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_416.KlingelnbergCycloPalloidHypoidGearRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _416

            return self._parent._cast(_416.KlingelnbergCycloPalloidHypoidGearRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_419.KlingelnbergCycloPalloidConicalGearRating":
            from mastapy.gears.rating.klingelnberg_conical import _419

            return self._parent._cast(_419.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def hypoid_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_446.HypoidGearRating":
            from mastapy.gears.rating.hypoid import _446

            return self._parent._cast(_446.HypoidGearRating)

        @property
        def face_gear_duty_cycle_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_452.FaceGearDutyCycleRating":
            from mastapy.gears.rating.face import _452

            return self._parent._cast(_452.FaceGearDutyCycleRating)

        @property
        def face_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_455.FaceGearRating":
            from mastapy.gears.rating.face import _455

            return self._parent._cast(_455.FaceGearRating)

        @property
        def cylindrical_gear_duty_cycle_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_462.CylindricalGearDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _462

            return self._parent._cast(_462.CylindricalGearDutyCycleRating)

        @property
        def cylindrical_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_467.CylindricalGearRating":
            from mastapy.gears.rating.cylindrical import _467

            return self._parent._cast(_467.CylindricalGearRating)

        @property
        def conical_gear_duty_cycle_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_545.ConicalGearDutyCycleRating":
            from mastapy.gears.rating.conical import _545

            return self._parent._cast(_545.ConicalGearDutyCycleRating)

        @property
        def conical_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_547.ConicalGearRating":
            from mastapy.gears.rating.conical import _547

            return self._parent._cast(_547.ConicalGearRating)

        @property
        def concept_gear_duty_cycle_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_555.ConceptGearDutyCycleRating":
            from mastapy.gears.rating.concept import _555

            return self._parent._cast(_555.ConceptGearDutyCycleRating)

        @property
        def concept_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_558.ConceptGearRating":
            from mastapy.gears.rating.concept import _558

            return self._parent._cast(_558.ConceptGearRating)

        @property
        def bevel_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_562.BevelGearRating":
            from mastapy.gears.rating.bevel import _562

            return self._parent._cast(_562.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "_573.AGMAGleasonConicalGearRating":
            from mastapy.gears.rating.agma_gleason_conical import _573

            return self._parent._cast(_573.AGMAGleasonConicalGearRating)

        @property
        def abstract_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "AbstractGearRating":
            return self._parent

        def __getattr__(self: "AbstractGearRating._Cast_AbstractGearRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def cycles_to_fail(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CyclesToFail

        if temp is None:
            return 0.0

        return temp

    @property
    def cycles_to_fail_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CyclesToFailBending

        if temp is None:
            return 0.0

        return temp

    @property
    def cycles_to_fail_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CyclesToFailContact

        if temp is None:
            return 0.0

        return temp

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
    def gear_reliability_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearReliabilityBending

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_reliability_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearReliabilityContact

        if temp is None:
            return 0.0

        return temp

    @property
    def normalised_bending_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedBendingSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalised_bending_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedBendingSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def normalised_contact_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedContactSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalised_contact_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedContactSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def normalised_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalised_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeToFail

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeToFailBending

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeToFailContact

        if temp is None:
            return 0.0

        return temp

    @property
    def total_gear_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalGearReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "AbstractGearRating._Cast_AbstractGearRating":
        return self._Cast_AbstractGearRating(self)
