"""BevelDifferentialGearSetCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5923
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "BevelDifferentialGearSetCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5718
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5916,
        _5917,
        _5911,
        _5939,
        _5965,
        _6003,
        _5905,
        _5984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetCompoundHarmonicAnalysis")


class BevelDifferentialGearSetCompoundHarmonicAnalysis(
    _5923.BevelGearSetCompoundHarmonicAnalysis
):
    """BevelDifferentialGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis"
    )

    class _Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting BevelDifferentialGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
            parent: "BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_harmonic_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_5923.BevelGearSetCompoundHarmonicAnalysis":
            return self._parent._cast(_5923.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_5911.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5911,
            )

            return self._parent._cast(
                _5911.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_5939.ConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5939,
            )

            return self._parent._cast(_5939.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_5965.GearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5965,
            )

            return self._parent._cast(_5965.GearSetCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_6003.SpecialisedAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6003,
            )

            return self._parent._cast(_6003.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_5905.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5905,
            )

            return self._parent._cast(_5905.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_5984.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(_5984.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
        ) -> "BevelDifferentialGearSetCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis",
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
        instance_to_wrap: "BevelDifferentialGearSetCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2534.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2534.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5718.BevelDifferentialGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearSetHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_gears_compound_harmonic_analysis(
        self: Self,
    ) -> "List[_5916.BevelDifferentialGearCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.BevelDifferentialGearCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsCompoundHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_compound_harmonic_analysis(
        self: Self,
    ) -> "List[_5917.BevelDifferentialGearMeshCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.BevelDifferentialGearMeshCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesCompoundHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5718.BevelDifferentialGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearSetHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis":
        return self._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis(self)
