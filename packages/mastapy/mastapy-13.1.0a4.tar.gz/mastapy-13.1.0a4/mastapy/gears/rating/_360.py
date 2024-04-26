"""AbstractGearMeshRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1226
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "AbstractGearMeshRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _367, _372
    from mastapy.gears.rating.zerol_bevel import _376
    from mastapy.gears.rating.worm import _380, _384
    from mastapy.gears.rating.straight_bevel import _402
    from mastapy.gears.rating.straight_bevel_diff import _405
    from mastapy.gears.rating.spiral_bevel import _409
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _412
    from mastapy.gears.rating.klingelnberg_hypoid import _415
    from mastapy.gears.rating.klingelnberg_conical import _418
    from mastapy.gears.rating.hypoid import _445
    from mastapy.gears.rating.face import _453, _454
    from mastapy.gears.rating.cylindrical import _465, _473
    from mastapy.gears.rating.conical import _546, _551
    from mastapy.gears.rating.concept import _556, _557
    from mastapy.gears.rating.bevel import _561
    from mastapy.gears.rating.agma_gleason_conical import _572


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearMeshRating",)


Self = TypeVar("Self", bound="AbstractGearMeshRating")


class AbstractGearMeshRating(_1226.AbstractGearMeshAnalysis):
    """AbstractGearMeshRating

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearMeshRating")

    class _Cast_AbstractGearMeshRating:
        """Special nested class for casting AbstractGearMeshRating to subclasses."""

        def __init__(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
            parent: "AbstractGearMeshRating",
        ):
            self._parent = parent

        @property
        def abstract_gear_mesh_analysis(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_1226.AbstractGearMeshAnalysis":
            return self._parent._cast(_1226.AbstractGearMeshAnalysis)

        @property
        def gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_367.GearMeshRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearMeshRating)

        @property
        def mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_372.MeshDutyCycleRating":
            from mastapy.gears.rating import _372

            return self._parent._cast(_372.MeshDutyCycleRating)

        @property
        def zerol_bevel_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_376.ZerolBevelGearMeshRating":
            from mastapy.gears.rating.zerol_bevel import _376

            return self._parent._cast(_376.ZerolBevelGearMeshRating)

        @property
        def worm_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_380.WormGearMeshRating":
            from mastapy.gears.rating.worm import _380

            return self._parent._cast(_380.WormGearMeshRating)

        @property
        def worm_mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_384.WormMeshDutyCycleRating":
            from mastapy.gears.rating.worm import _384

            return self._parent._cast(_384.WormMeshDutyCycleRating)

        @property
        def straight_bevel_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_402.StraightBevelGearMeshRating":
            from mastapy.gears.rating.straight_bevel import _402

            return self._parent._cast(_402.StraightBevelGearMeshRating)

        @property
        def straight_bevel_diff_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_405.StraightBevelDiffGearMeshRating":
            from mastapy.gears.rating.straight_bevel_diff import _405

            return self._parent._cast(_405.StraightBevelDiffGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_409.SpiralBevelGearMeshRating":
            from mastapy.gears.rating.spiral_bevel import _409

            return self._parent._cast(_409.SpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_412.KlingelnbergCycloPalloidSpiralBevelGearMeshRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _412

            return self._parent._cast(
                _412.KlingelnbergCycloPalloidSpiralBevelGearMeshRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_415.KlingelnbergCycloPalloidHypoidGearMeshRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _415

            return self._parent._cast(_415.KlingelnbergCycloPalloidHypoidGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_418.KlingelnbergCycloPalloidConicalGearMeshRating":
            from mastapy.gears.rating.klingelnberg_conical import _418

            return self._parent._cast(
                _418.KlingelnbergCycloPalloidConicalGearMeshRating
            )

        @property
        def hypoid_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_445.HypoidGearMeshRating":
            from mastapy.gears.rating.hypoid import _445

            return self._parent._cast(_445.HypoidGearMeshRating)

        @property
        def face_gear_mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_453.FaceGearMeshDutyCycleRating":
            from mastapy.gears.rating.face import _453

            return self._parent._cast(_453.FaceGearMeshDutyCycleRating)

        @property
        def face_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_454.FaceGearMeshRating":
            from mastapy.gears.rating.face import _454

            return self._parent._cast(_454.FaceGearMeshRating)

        @property
        def cylindrical_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_465.CylindricalGearMeshRating":
            from mastapy.gears.rating.cylindrical import _465

            return self._parent._cast(_465.CylindricalGearMeshRating)

        @property
        def cylindrical_mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_473.CylindricalMeshDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _473

            return self._parent._cast(_473.CylindricalMeshDutyCycleRating)

        @property
        def conical_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_546.ConicalGearMeshRating":
            from mastapy.gears.rating.conical import _546

            return self._parent._cast(_546.ConicalGearMeshRating)

        @property
        def conical_mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_551.ConicalMeshDutyCycleRating":
            from mastapy.gears.rating.conical import _551

            return self._parent._cast(_551.ConicalMeshDutyCycleRating)

        @property
        def concept_gear_mesh_duty_cycle_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_556.ConceptGearMeshDutyCycleRating":
            from mastapy.gears.rating.concept import _556

            return self._parent._cast(_556.ConceptGearMeshDutyCycleRating)

        @property
        def concept_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_557.ConceptGearMeshRating":
            from mastapy.gears.rating.concept import _557

            return self._parent._cast(_557.ConceptGearMeshRating)

        @property
        def bevel_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_561.BevelGearMeshRating":
            from mastapy.gears.rating.bevel import _561

            return self._parent._cast(_561.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "_572.AGMAGleasonConicalGearMeshRating":
            from mastapy.gears.rating.agma_gleason_conical import _572

            return self._parent._cast(_572.AGMAGleasonConicalGearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating",
        ) -> "AbstractGearMeshRating":
            return self._parent

        def __getattr__(
            self: "AbstractGearMeshRating._Cast_AbstractGearMeshRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_efficiency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshEfficiency

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
    def cast_to(self: Self) -> "AbstractGearMeshRating._Cast_AbstractGearMeshRating":
        return self._Cast_AbstractGearMeshRating(self)
