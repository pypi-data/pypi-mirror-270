"""ConicalGearSetHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5784
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ConicalGearSetHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5738,
        _5739,
        _5711,
        _5718,
        _5723,
        _5799,
        _5803,
        _5806,
        _5809,
        _5840,
        _5847,
        _5850,
        _5869,
        _5836,
        _5704,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2748
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetHarmonicAnalysis")


class ConicalGearSetHarmonicAnalysis(_5784.GearSetHarmonicAnalysis):
    """ConicalGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetHarmonicAnalysis")

    class _Cast_ConicalGearSetHarmonicAnalysis:
        """Special nested class for casting ConicalGearSetHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
            parent: "ConicalGearSetHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5784.GearSetHarmonicAnalysis":
            return self._parent._cast(_5784.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5836.SpecialisedAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5836,
            )

            return self._parent._cast(_5836.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5704.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5711.AGMAGleasonConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5718.BevelDifferentialGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5718,
            )

            return self._parent._cast(_5718.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5723.BevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.BevelGearSetHarmonicAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5799.HypoidGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5799,
            )

            return self._parent._cast(_5799.HypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5803.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5803,
            )

            return self._parent._cast(
                _5803.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5806.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(
                _5806.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5809.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(
                _5809.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5840.SpiralBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5840,
            )

            return self._parent._cast(_5840.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5847.StraightBevelDiffGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5847,
            )

            return self._parent._cast(_5847.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5850.StraightBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5850,
            )

            return self._parent._cast(_5850.StraightBevelGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "_5869.ZerolBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5869,
            )

            return self._parent._cast(_5869.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
        ) -> "ConicalGearSetHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2542.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_harmonic_analysis(
        self: Self,
    ) -> "List[_5738.ConicalGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_gears_harmonic_analysis(
        self: Self,
    ) -> "List[_5738.ConicalGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5739.ConicalGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5739.ConicalGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: Self) -> "_2748.ConicalGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSetSystemDeflection

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
    ) -> "ConicalGearSetHarmonicAnalysis._Cast_ConicalGearSetHarmonicAnalysis":
        return self._Cast_ConicalGearSetHarmonicAnalysis(self)
