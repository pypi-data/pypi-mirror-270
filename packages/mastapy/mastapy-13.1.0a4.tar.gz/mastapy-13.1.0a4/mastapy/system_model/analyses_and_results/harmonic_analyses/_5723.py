"""BevelGearSetHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5711
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "BevelGearSetHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5721,
        _5722,
        _5718,
        _5840,
        _5847,
        _5850,
        _5869,
        _5740,
        _5784,
        _5836,
        _5704,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2730
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetHarmonicAnalysis",)


Self = TypeVar("Self", bound="BevelGearSetHarmonicAnalysis")


class BevelGearSetHarmonicAnalysis(_5711.AGMAGleasonConicalGearSetHarmonicAnalysis):
    """BevelGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetHarmonicAnalysis")

    class _Cast_BevelGearSetHarmonicAnalysis:
        """Special nested class for casting BevelGearSetHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
            parent: "BevelGearSetHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5711.AGMAGleasonConicalGearSetHarmonicAnalysis":
            return self._parent._cast(_5711.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5740.ConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5740,
            )

            return self._parent._cast(_5740.ConicalGearSetHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5784.GearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5836.SpecialisedAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5836,
            )

            return self._parent._cast(_5836.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5704.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5718.BevelDifferentialGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5718,
            )

            return self._parent._cast(_5718.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5840.SpiralBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5840,
            )

            return self._parent._cast(_5840.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5847.StraightBevelDiffGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5847,
            )

            return self._parent._cast(_5847.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5850.StraightBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5850,
            )

            return self._parent._cast(_5850.StraightBevelGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5869.ZerolBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5869,
            )

            return self._parent._cast(_5869.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "BevelGearSetHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSetHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2538.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def agma_gleason_conical_gears_harmonic_analysis(
        self: Self,
    ) -> "List[_5721.BevelGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMAGleasonConicalGearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_gears_harmonic_analysis(
        self: Self,
    ) -> "List[_5721.BevelGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def agma_gleason_conical_meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5722.BevelGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMAGleasonConicalMeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5722.BevelGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelMeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: Self) -> "_2730.BevelGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelGearSetSystemDeflection

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
    ) -> "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis":
        return self._Cast_BevelGearSetHarmonicAnalysis(self)
