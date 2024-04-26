"""PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6214,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6120,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6225,
        _6263,
        _6165,
        _6244,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation"
)


class PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation(
    _6214.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation
):
    """PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6214.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6214.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6225.GearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6225,
            )

            return self._parent._cast(
                _6225.GearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6263.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6263,
            )

            return self._parent._cast(
                _6263.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6165.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6165,
            )

            return self._parent._cast(
                _6165.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6244.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6244,
            )

            return self._parent._cast(
                _6244.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6120.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6120.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation]

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
    ) -> "PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
