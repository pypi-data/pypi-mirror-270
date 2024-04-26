"""WormGearSetHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5784
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "WormGearSetHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2570
    from mastapy.system_model.analyses_and_results.static_loads import _7011
    from mastapy.system_model.analyses_and_results.system_deflections import _2860
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5864,
        _5865,
        _5836,
        _5704,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetHarmonicAnalysis",)


Self = TypeVar("Self", bound="WormGearSetHarmonicAnalysis")


class WormGearSetHarmonicAnalysis(_5784.GearSetHarmonicAnalysis):
    """WormGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearSetHarmonicAnalysis")

    class _Cast_WormGearSetHarmonicAnalysis:
        """Special nested class for casting WormGearSetHarmonicAnalysis to subclasses."""

        def __init__(
            self: "WormGearSetHarmonicAnalysis._Cast_WormGearSetHarmonicAnalysis",
            parent: "WormGearSetHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_harmonic_analysis(
            self: "WormGearSetHarmonicAnalysis._Cast_WormGearSetHarmonicAnalysis",
        ) -> "_5784.GearSetHarmonicAnalysis":
            return self._parent._cast(_5784.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "WormGearSetHarmonicAnalysis._Cast_WormGearSetHarmonicAnalysis",
        ) -> "_5836.SpecialisedAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5836,
            )

            return self._parent._cast(_5836.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "WormGearSetHarmonicAnalysis._Cast_WormGearSetHarmonicAnalysis",
        ) -> "_5704.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "WormGearSetHarmonicAnalysis._Cast_WormGearSetHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "WormGearSetHarmonicAnalysis._Cast_WormGearSetHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "WormGearSetHarmonicAnalysis._Cast_WormGearSetHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "WormGearSetHarmonicAnalysis._Cast_WormGearSetHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearSetHarmonicAnalysis._Cast_WormGearSetHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearSetHarmonicAnalysis._Cast_WormGearSetHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def worm_gear_set_harmonic_analysis(
            self: "WormGearSetHarmonicAnalysis._Cast_WormGearSetHarmonicAnalysis",
        ) -> "WormGearSetHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearSetHarmonicAnalysis._Cast_WormGearSetHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearSetHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2570.WormGearSet":
        """mastapy.system_model.part_model.gears.WormGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_7011.WormGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2860.WormGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.WormGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_harmonic_analysis(self: Self) -> "List[_5864.WormGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.WormGearHarmonicAnalysis]

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
    def worm_gears_harmonic_analysis(
        self: Self,
    ) -> "List[_5864.WormGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.WormGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5865.WormGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.WormGearMeshHarmonicAnalysis]

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
    def worm_meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5865.WormGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.WormGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearSetHarmonicAnalysis._Cast_WormGearSetHarmonicAnalysis":
        return self._Cast_WormGearSetHarmonicAnalysis(self)
