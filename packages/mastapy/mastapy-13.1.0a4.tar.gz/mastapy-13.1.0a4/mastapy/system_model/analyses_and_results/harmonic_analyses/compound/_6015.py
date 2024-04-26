"""StraightBevelGearSetCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5923
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "StraightBevelGearSetCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2566
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5850
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _6013,
        _6014,
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
__all__ = ("StraightBevelGearSetCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearSetCompoundHarmonicAnalysis")


class StraightBevelGearSetCompoundHarmonicAnalysis(
    _5923.BevelGearSetCompoundHarmonicAnalysis
):
    """StraightBevelGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearSetCompoundHarmonicAnalysis"
    )

    class _Cast_StraightBevelGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting StraightBevelGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearSetCompoundHarmonicAnalysis._Cast_StraightBevelGearSetCompoundHarmonicAnalysis",
            parent: "StraightBevelGearSetCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_harmonic_analysis(
            self: "StraightBevelGearSetCompoundHarmonicAnalysis._Cast_StraightBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_5923.BevelGearSetCompoundHarmonicAnalysis":
            return self._parent._cast(_5923.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(
            self: "StraightBevelGearSetCompoundHarmonicAnalysis._Cast_StraightBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_5911.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5911,
            )

            return self._parent._cast(
                _5911.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "StraightBevelGearSetCompoundHarmonicAnalysis._Cast_StraightBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_5939.ConicalGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5939,
            )

            return self._parent._cast(_5939.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "StraightBevelGearSetCompoundHarmonicAnalysis._Cast_StraightBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_5965.GearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5965,
            )

            return self._parent._cast(_5965.GearSetCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "StraightBevelGearSetCompoundHarmonicAnalysis._Cast_StraightBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_6003.SpecialisedAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6003,
            )

            return self._parent._cast(_6003.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "StraightBevelGearSetCompoundHarmonicAnalysis._Cast_StraightBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_5905.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5905,
            )

            return self._parent._cast(_5905.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "StraightBevelGearSetCompoundHarmonicAnalysis._Cast_StraightBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_5984.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(_5984.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelGearSetCompoundHarmonicAnalysis._Cast_StraightBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearSetCompoundHarmonicAnalysis._Cast_StraightBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearSetCompoundHarmonicAnalysis._Cast_StraightBevelGearSetCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis(
            self: "StraightBevelGearSetCompoundHarmonicAnalysis._Cast_StraightBevelGearSetCompoundHarmonicAnalysis",
        ) -> "StraightBevelGearSetCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSetCompoundHarmonicAnalysis._Cast_StraightBevelGearSetCompoundHarmonicAnalysis",
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
        instance_to_wrap: "StraightBevelGearSetCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2566.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2566.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

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
    ) -> "List[_5850.StraightBevelGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelGearSetHarmonicAnalysis]

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
    def straight_bevel_gears_compound_harmonic_analysis(
        self: Self,
    ) -> "List[_6013.StraightBevelGearCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.StraightBevelGearCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearsCompoundHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes_compound_harmonic_analysis(
        self: Self,
    ) -> "List[_6014.StraightBevelGearMeshCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.StraightBevelGearMeshCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshesCompoundHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5850.StraightBevelGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelGearSetHarmonicAnalysis]

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
    ) -> "StraightBevelGearSetCompoundHarmonicAnalysis._Cast_StraightBevelGearSetCompoundHarmonicAnalysis":
        return self._Cast_StraightBevelGearSetCompoundHarmonicAnalysis(self)
