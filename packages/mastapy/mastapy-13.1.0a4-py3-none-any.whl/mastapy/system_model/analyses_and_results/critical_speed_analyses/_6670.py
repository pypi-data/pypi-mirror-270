"""SpecialisedAssemblyCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6569
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "SpecialisedAssemblyCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2494
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6575,
        _6579,
        _6582,
        _6587,
        _6589,
        _6591,
        _6596,
        _6600,
        _6603,
        _6607,
        _6613,
        _6615,
        _6621,
        _6627,
        _6629,
        _6632,
        _6636,
        _6640,
        _6643,
        _6646,
        _6653,
        _6656,
        _6663,
        _6673,
        _6675,
        _6679,
        _6682,
        _6685,
        _6690,
        _6697,
        _6700,
        _6651,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCriticalSpeedAnalysis")


class SpecialisedAssemblyCriticalSpeedAnalysis(
    _6569.AbstractAssemblyCriticalSpeedAnalysis
):
    """SpecialisedAssemblyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCriticalSpeedAnalysis"
    )

    class _Cast_SpecialisedAssemblyCriticalSpeedAnalysis:
        """Special nested class for casting SpecialisedAssemblyCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
            parent: "SpecialisedAssemblyCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6569.AbstractAssemblyCriticalSpeedAnalysis":
            return self._parent._cast(_6569.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6651.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6575.AGMAGleasonConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6575,
            )

            return self._parent._cast(
                _6575.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def belt_drive_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6579.BeltDriveCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6579,
            )

            return self._parent._cast(_6579.BeltDriveCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6582.BevelDifferentialGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6582,
            )

            return self._parent._cast(
                _6582.BevelDifferentialGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6587.BevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6587,
            )

            return self._parent._cast(_6587.BevelGearSetCriticalSpeedAnalysis)

        @property
        def bolted_joint_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6589.BoltedJointCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(_6589.BoltedJointCriticalSpeedAnalysis)

        @property
        def clutch_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6591.ClutchCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6591,
            )

            return self._parent._cast(_6591.ClutchCriticalSpeedAnalysis)

        @property
        def concept_coupling_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6596.ConceptCouplingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6596,
            )

            return self._parent._cast(_6596.ConceptCouplingCriticalSpeedAnalysis)

        @property
        def concept_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6600.ConceptGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6600,
            )

            return self._parent._cast(_6600.ConceptGearSetCriticalSpeedAnalysis)

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6603.ConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6603,
            )

            return self._parent._cast(_6603.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def coupling_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6607.CouplingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6607,
            )

            return self._parent._cast(_6607.CouplingCriticalSpeedAnalysis)

        @property
        def cvt_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6613.CVTCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6613,
            )

            return self._parent._cast(_6613.CVTCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6615.CycloidalAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6615,
            )

            return self._parent._cast(_6615.CycloidalAssemblyCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6621.CylindricalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(_6621.CylindricalGearSetCriticalSpeedAnalysis)

        @property
        def face_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6627.FaceGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(_6627.FaceGearSetCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6629.FlexiblePinAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6629,
            )

            return self._parent._cast(_6629.FlexiblePinAssemblyCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6632.GearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6632,
            )

            return self._parent._cast(_6632.GearSetCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6636.HypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6636,
            )

            return self._parent._cast(_6636.HypoidGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6640.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6640,
            )

            return self._parent._cast(
                _6640.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6643.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6643,
            )

            return self._parent._cast(
                _6643.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6646.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(
                _6646.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6653.PartToPartShearCouplingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6653,
            )

            return self._parent._cast(
                _6653.PartToPartShearCouplingCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6656.PlanetaryGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6656,
            )

            return self._parent._cast(_6656.PlanetaryGearSetCriticalSpeedAnalysis)

        @property
        def rolling_ring_assembly_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6663.RollingRingAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6663,
            )

            return self._parent._cast(_6663.RollingRingAssemblyCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6673.SpiralBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6673,
            )

            return self._parent._cast(_6673.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def spring_damper_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6675.SpringDamperCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6675,
            )

            return self._parent._cast(_6675.SpringDamperCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6679.StraightBevelDiffGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6679,
            )

            return self._parent._cast(
                _6679.StraightBevelDiffGearSetCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6682.StraightBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6682,
            )

            return self._parent._cast(_6682.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def synchroniser_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6685.SynchroniserCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6685,
            )

            return self._parent._cast(_6685.SynchroniserCriticalSpeedAnalysis)

        @property
        def torque_converter_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6690.TorqueConverterCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6690,
            )

            return self._parent._cast(_6690.TorqueConverterCriticalSpeedAnalysis)

        @property
        def worm_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6697.WormGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6697,
            )

            return self._parent._cast(_6697.WormGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "_6700.ZerolBevelGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6700,
            )

            return self._parent._cast(_6700.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
        ) -> "SpecialisedAssemblyCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "SpecialisedAssemblyCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2494.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCriticalSpeedAnalysis":
        return self._Cast_SpecialisedAssemblyCriticalSpeedAnalysis(self)
