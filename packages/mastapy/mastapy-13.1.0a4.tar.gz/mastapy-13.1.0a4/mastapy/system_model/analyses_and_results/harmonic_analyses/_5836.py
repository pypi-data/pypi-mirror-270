"""SpecialisedAssemblyHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5704
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "SpecialisedAssemblyHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2494
    from mastapy.system_model.analyses_and_results.system_deflections import _2829
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5711,
        _5715,
        _5718,
        _5723,
        _5724,
        _5728,
        _5734,
        _5737,
        _5740,
        _5745,
        _5747,
        _5749,
        _5755,
        _5775,
        _5777,
        _5784,
        _5799,
        _5803,
        _5806,
        _5809,
        _5817,
        _5820,
        _5828,
        _5840,
        _5843,
        _5847,
        _5850,
        _5854,
        _5858,
        _5866,
        _5869,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyHarmonicAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyHarmonicAnalysis")


class SpecialisedAssemblyHarmonicAnalysis(_5704.AbstractAssemblyHarmonicAnalysis):
    """SpecialisedAssemblyHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblyHarmonicAnalysis")

    class _Cast_SpecialisedAssemblyHarmonicAnalysis:
        """Special nested class for casting SpecialisedAssemblyHarmonicAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
            parent: "SpecialisedAssemblyHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5704.AbstractAssemblyHarmonicAnalysis":
            return self._parent._cast(_5704.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5711.AGMAGleasonConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def belt_drive_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5715.BeltDriveHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5715,
            )

            return self._parent._cast(_5715.BeltDriveHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5718.BevelDifferentialGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5718,
            )

            return self._parent._cast(_5718.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5723.BevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.BevelGearSetHarmonicAnalysis)

        @property
        def bolted_joint_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5724.BoltedJointHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5724,
            )

            return self._parent._cast(_5724.BoltedJointHarmonicAnalysis)

        @property
        def clutch_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5728.ClutchHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5728,
            )

            return self._parent._cast(_5728.ClutchHarmonicAnalysis)

        @property
        def concept_coupling_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5734.ConceptCouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5734,
            )

            return self._parent._cast(_5734.ConceptCouplingHarmonicAnalysis)

        @property
        def concept_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5737.ConceptGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5737,
            )

            return self._parent._cast(_5737.ConceptGearSetHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5740.ConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5740,
            )

            return self._parent._cast(_5740.ConicalGearSetHarmonicAnalysis)

        @property
        def coupling_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5745.CouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5745,
            )

            return self._parent._cast(_5745.CouplingHarmonicAnalysis)

        @property
        def cvt_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5747.CVTHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5747,
            )

            return self._parent._cast(_5747.CVTHarmonicAnalysis)

        @property
        def cycloidal_assembly_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5749.CycloidalAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5749,
            )

            return self._parent._cast(_5749.CycloidalAssemblyHarmonicAnalysis)

        @property
        def cylindrical_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5755.CylindricalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5755,
            )

            return self._parent._cast(_5755.CylindricalGearSetHarmonicAnalysis)

        @property
        def face_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5775.FaceGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5775,
            )

            return self._parent._cast(_5775.FaceGearSetHarmonicAnalysis)

        @property
        def flexible_pin_assembly_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5777.FlexiblePinAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5777,
            )

            return self._parent._cast(_5777.FlexiblePinAssemblyHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5784.GearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.GearSetHarmonicAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5799.HypoidGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5799,
            )

            return self._parent._cast(_5799.HypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5803.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5803,
            )

            return self._parent._cast(
                _5803.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5806.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(
                _5806.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5809.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(
                _5809.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5817.PartToPartShearCouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5817,
            )

            return self._parent._cast(_5817.PartToPartShearCouplingHarmonicAnalysis)

        @property
        def planetary_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5820.PlanetaryGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5820,
            )

            return self._parent._cast(_5820.PlanetaryGearSetHarmonicAnalysis)

        @property
        def rolling_ring_assembly_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5828.RollingRingAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5828,
            )

            return self._parent._cast(_5828.RollingRingAssemblyHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5840.SpiralBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5840,
            )

            return self._parent._cast(_5840.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def spring_damper_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5843.SpringDamperHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5843,
            )

            return self._parent._cast(_5843.SpringDamperHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5847.StraightBevelDiffGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5847,
            )

            return self._parent._cast(_5847.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5850.StraightBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5850,
            )

            return self._parent._cast(_5850.StraightBevelGearSetHarmonicAnalysis)

        @property
        def synchroniser_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5854.SynchroniserHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5854,
            )

            return self._parent._cast(_5854.SynchroniserHarmonicAnalysis)

        @property
        def torque_converter_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5858.TorqueConverterHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5858,
            )

            return self._parent._cast(_5858.TorqueConverterHarmonicAnalysis)

        @property
        def worm_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5866.WormGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5866,
            )

            return self._parent._cast(_5866.WormGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "_5869.ZerolBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5869,
            )

            return self._parent._cast(_5869.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
        ) -> "SpecialisedAssemblyHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyHarmonicAnalysis.TYPE"
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
    def system_deflection_results(
        self: Self,
    ) -> "_2829.SpecialisedAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "SpecialisedAssemblyHarmonicAnalysis._Cast_SpecialisedAssemblyHarmonicAnalysis"
    ):
        return self._Cast_SpecialisedAssemblyHarmonicAnalysis(self)
