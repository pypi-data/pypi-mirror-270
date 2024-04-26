"""AbstractGearSetRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1227
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "AbstractGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears import _335
    from mastapy.gears.rating import _360, _361, _369, _370
    from mastapy.gears.rating.zerol_bevel import _378
    from mastapy.gears.rating.worm import _382, _383
    from mastapy.gears.rating.straight_bevel import _404
    from mastapy.gears.rating.straight_bevel_diff import _407
    from mastapy.gears.rating.spiral_bevel import _411
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _414
    from mastapy.gears.rating.klingelnberg_hypoid import _417
    from mastapy.gears.rating.klingelnberg_conical import _420
    from mastapy.gears.rating.hypoid import _447
    from mastapy.gears.rating.face import _456, _457
    from mastapy.gears.rating.cylindrical import _470, _471, _487
    from mastapy.gears.rating.conical import _548, _549
    from mastapy.gears.rating.concept import _559, _560
    from mastapy.gears.rating.bevel import _563
    from mastapy.gears.rating.agma_gleason_conical import _574


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearSetRating",)


Self = TypeVar("Self", bound="AbstractGearSetRating")


class AbstractGearSetRating(_1227.AbstractGearSetAnalysis):
    """AbstractGearSetRating

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearSetRating")

    class _Cast_AbstractGearSetRating:
        """Special nested class for casting AbstractGearSetRating to subclasses."""

        def __init__(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
            parent: "AbstractGearSetRating",
        ):
            self._parent = parent

        @property
        def abstract_gear_set_analysis(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_1227.AbstractGearSetAnalysis":
            return self._parent._cast(_1227.AbstractGearSetAnalysis)

        @property
        def gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_369.GearSetDutyCycleRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.GearSetDutyCycleRating)

        @property
        def gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_370.GearSetRating":
            from mastapy.gears.rating import _370

            return self._parent._cast(_370.GearSetRating)

        @property
        def zerol_bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_378.ZerolBevelGearSetRating":
            from mastapy.gears.rating.zerol_bevel import _378

            return self._parent._cast(_378.ZerolBevelGearSetRating)

        @property
        def worm_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_382.WormGearSetDutyCycleRating":
            from mastapy.gears.rating.worm import _382

            return self._parent._cast(_382.WormGearSetDutyCycleRating)

        @property
        def worm_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_383.WormGearSetRating":
            from mastapy.gears.rating.worm import _383

            return self._parent._cast(_383.WormGearSetRating)

        @property
        def straight_bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_404.StraightBevelGearSetRating":
            from mastapy.gears.rating.straight_bevel import _404

            return self._parent._cast(_404.StraightBevelGearSetRating)

        @property
        def straight_bevel_diff_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_407.StraightBevelDiffGearSetRating":
            from mastapy.gears.rating.straight_bevel_diff import _407

            return self._parent._cast(_407.StraightBevelDiffGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_411.SpiralBevelGearSetRating":
            from mastapy.gears.rating.spiral_bevel import _411

            return self._parent._cast(_411.SpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_414.KlingelnbergCycloPalloidSpiralBevelGearSetRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _414

            return self._parent._cast(
                _414.KlingelnbergCycloPalloidSpiralBevelGearSetRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_417.KlingelnbergCycloPalloidHypoidGearSetRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _417

            return self._parent._cast(_417.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_420.KlingelnbergCycloPalloidConicalGearSetRating":
            from mastapy.gears.rating.klingelnberg_conical import _420

            return self._parent._cast(_420.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def hypoid_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_447.HypoidGearSetRating":
            from mastapy.gears.rating.hypoid import _447

            return self._parent._cast(_447.HypoidGearSetRating)

        @property
        def face_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_456.FaceGearSetDutyCycleRating":
            from mastapy.gears.rating.face import _456

            return self._parent._cast(_456.FaceGearSetDutyCycleRating)

        @property
        def face_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_457.FaceGearSetRating":
            from mastapy.gears.rating.face import _457

            return self._parent._cast(_457.FaceGearSetRating)

        @property
        def cylindrical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_470.CylindricalGearSetDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _470

            return self._parent._cast(_470.CylindricalGearSetDutyCycleRating)

        @property
        def cylindrical_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_471.CylindricalGearSetRating":
            from mastapy.gears.rating.cylindrical import _471

            return self._parent._cast(_471.CylindricalGearSetRating)

        @property
        def reduced_cylindrical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_487.ReducedCylindricalGearSetDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _487

            return self._parent._cast(_487.ReducedCylindricalGearSetDutyCycleRating)

        @property
        def conical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_548.ConicalGearSetDutyCycleRating":
            from mastapy.gears.rating.conical import _548

            return self._parent._cast(_548.ConicalGearSetDutyCycleRating)

        @property
        def conical_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_549.ConicalGearSetRating":
            from mastapy.gears.rating.conical import _549

            return self._parent._cast(_549.ConicalGearSetRating)

        @property
        def concept_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_559.ConceptGearSetDutyCycleRating":
            from mastapy.gears.rating.concept import _559

            return self._parent._cast(_559.ConceptGearSetDutyCycleRating)

        @property
        def concept_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_560.ConceptGearSetRating":
            from mastapy.gears.rating.concept import _560

            return self._parent._cast(_560.ConceptGearSetRating)

        @property
        def bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_563.BevelGearSetRating":
            from mastapy.gears.rating.bevel import _563

            return self._parent._cast(_563.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "_574.AGMAGleasonConicalGearSetRating":
            from mastapy.gears.rating.agma_gleason_conical import _574

            return self._parent._cast(_574.AGMAGleasonConicalGearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "AbstractGearSetRating":
            return self._parent

        def __getattr__(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearSetRating.TYPE"):
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
    def normalised_safety_factor_for_fatigue_and_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedSafetyFactorForFatigueAndStatic

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
    def transmission_properties_gears(self: Self) -> "_335.GearSetDesignGroup":
        """mastapy.gears.GearSetDesignGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmissionPropertiesGears

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_mesh_ratings(self: Self) -> "List[_360.AbstractGearMeshRating]":
        """List[mastapy.gears.rating.AbstractGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_ratings(self: Self) -> "List[_361.AbstractGearRating]":
        """List[mastapy.gears.rating.AbstractGearRating]

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
    def cast_to(self: Self) -> "AbstractGearSetRating._Cast_AbstractGearSetRating":
        return self._Cast_AbstractGearSetRating(self)
