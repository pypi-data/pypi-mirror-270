"""StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6183,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2564
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6143,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6270,
        _6271,
        _6171,
        _6199,
        _6225,
        _6263,
        _6165,
        _6244,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation"
)


class StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation(
    _6183.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
):
    """StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6183.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6183.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6171.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6171,
            )

            return self._parent._cast(
                _6171.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6199.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6199,
            )

            return self._parent._cast(
                _6199.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6225.GearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6225,
            )

            return self._parent._cast(
                _6225.GearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6263.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6263,
            )

            return self._parent._cast(
                _6263.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6165.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6165,
            )

            return self._parent._cast(
                _6165.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6244.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6244,
            )

            return self._parent._cast(
                _6244.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2564.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2564.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

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
    ) -> "List[_6143.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation]

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
    def straight_bevel_diff_gears_compound_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6270.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.StraightBevelDiffGearsCompoundHarmonicAnalysisOfSingleExcitation
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_compound_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6271.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.StraightBevelDiffMeshesCompoundHarmonicAnalysisOfSingleExcitation
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6143.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation]

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
    ) -> "StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
