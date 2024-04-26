"""KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5803
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2557
    from mastapy.system_model.analyses_and_results.static_loads import _6944
    from mastapy.system_model.analyses_and_results.system_deflections import _2795
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5804,
        _5805,
        _5740,
        _5784,
        _5836,
        _5704,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis")


class KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis(
    _5803.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
        ) -> "_5803.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis":
            return self._parent._cast(
                _5803.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
            )

        @property
        def conical_gear_set_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
        ) -> "_5740.ConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5740,
            )

            return self._parent._cast(_5740.ConicalGearSetHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
        ) -> "_5784.GearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
        ) -> "_5836.SpecialisedAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5836,
            )

            return self._parent._cast(_5836.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
        ) -> "_5704.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2557.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6944.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2795.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_conical_gears_harmonic_analysis(
        self: Self,
    ) -> "List[_5804.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidConicalGearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_harmonic_analysis(
        self: Self,
    ) -> "List[_5804.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_conical_meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5805.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidConicalMeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5805.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis(self)
