"""GearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _361
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_RATING = python_net_import("SMT.MastaAPI.Gears.Rating", "GearRating")

if TYPE_CHECKING:
    from mastapy.materials import _287
    from mastapy.gears.rating import _363
    from mastapy.gears.rating.zerol_bevel import _377
    from mastapy.gears.rating.worm import _381
    from mastapy.gears.rating.straight_bevel import _403
    from mastapy.gears.rating.straight_bevel_diff import _406
    from mastapy.gears.rating.spiral_bevel import _410
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _413
    from mastapy.gears.rating.klingelnberg_hypoid import _416
    from mastapy.gears.rating.klingelnberg_conical import _419
    from mastapy.gears.rating.hypoid import _446
    from mastapy.gears.rating.face import _455
    from mastapy.gears.rating.cylindrical import _467
    from mastapy.gears.rating.conical import _547
    from mastapy.gears.rating.concept import _558
    from mastapy.gears.rating.bevel import _562
    from mastapy.gears.rating.agma_gleason_conical import _573
    from mastapy.gears.analysis import _1225


__docformat__ = "restructuredtext en"
__all__ = ("GearRating",)


Self = TypeVar("Self", bound="GearRating")


class GearRating(_361.AbstractGearRating):
    """GearRating

    This is a mastapy class.
    """

    TYPE = _GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearRating")

    class _Cast_GearRating:
        """Special nested class for casting GearRating to subclasses."""

        def __init__(self: "GearRating._Cast_GearRating", parent: "GearRating"):
            self._parent = parent

        @property
        def abstract_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_361.AbstractGearRating":
            return self._parent._cast(_361.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "GearRating._Cast_GearRating",
        ) -> "_1225.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.AbstractGearAnalysis)

        @property
        def zerol_bevel_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_377.ZerolBevelGearRating":
            from mastapy.gears.rating.zerol_bevel import _377

            return self._parent._cast(_377.ZerolBevelGearRating)

        @property
        def worm_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_381.WormGearRating":
            from mastapy.gears.rating.worm import _381

            return self._parent._cast(_381.WormGearRating)

        @property
        def straight_bevel_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_403.StraightBevelGearRating":
            from mastapy.gears.rating.straight_bevel import _403

            return self._parent._cast(_403.StraightBevelGearRating)

        @property
        def straight_bevel_diff_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_406.StraightBevelDiffGearRating":
            from mastapy.gears.rating.straight_bevel_diff import _406

            return self._parent._cast(_406.StraightBevelDiffGearRating)

        @property
        def spiral_bevel_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_410.SpiralBevelGearRating":
            from mastapy.gears.rating.spiral_bevel import _410

            return self._parent._cast(_410.SpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_413.KlingelnbergCycloPalloidSpiralBevelGearRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _413

            return self._parent._cast(
                _413.KlingelnbergCycloPalloidSpiralBevelGearRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_416.KlingelnbergCycloPalloidHypoidGearRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _416

            return self._parent._cast(_416.KlingelnbergCycloPalloidHypoidGearRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_419.KlingelnbergCycloPalloidConicalGearRating":
            from mastapy.gears.rating.klingelnberg_conical import _419

            return self._parent._cast(_419.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def hypoid_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_446.HypoidGearRating":
            from mastapy.gears.rating.hypoid import _446

            return self._parent._cast(_446.HypoidGearRating)

        @property
        def face_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_455.FaceGearRating":
            from mastapy.gears.rating.face import _455

            return self._parent._cast(_455.FaceGearRating)

        @property
        def cylindrical_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_467.CylindricalGearRating":
            from mastapy.gears.rating.cylindrical import _467

            return self._parent._cast(_467.CylindricalGearRating)

        @property
        def conical_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_547.ConicalGearRating":
            from mastapy.gears.rating.conical import _547

            return self._parent._cast(_547.ConicalGearRating)

        @property
        def concept_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_558.ConceptGearRating":
            from mastapy.gears.rating.concept import _558

            return self._parent._cast(_558.ConceptGearRating)

        @property
        def bevel_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_562.BevelGearRating":
            from mastapy.gears.rating.bevel import _562

            return self._parent._cast(_562.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(
            self: "GearRating._Cast_GearRating",
        ) -> "_573.AGMAGleasonConicalGearRating":
            from mastapy.gears.rating.agma_gleason_conical import _573

            return self._parent._cast(_573.AGMAGleasonConicalGearRating)

        @property
        def gear_rating(self: "GearRating._Cast_GearRating") -> "GearRating":
            return self._parent

        def __getattr__(self: "GearRating._Cast_GearRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_safety_factor_results(self: Self) -> "_287.SafetyFactorItem":
        """mastapy.materials.SafetyFactorItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def contact_safety_factor_results(self: Self) -> "_287.SafetyFactorItem":
        """mastapy.materials.SafetyFactorItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def static_safety_factor(self: Self) -> "_363.BendingAndContactReportingObject":
        """mastapy.gears.rating.BendingAndContactReportingObject

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticSafetyFactor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearRating._Cast_GearRating":
        return self._Cast_GearRating(self)
