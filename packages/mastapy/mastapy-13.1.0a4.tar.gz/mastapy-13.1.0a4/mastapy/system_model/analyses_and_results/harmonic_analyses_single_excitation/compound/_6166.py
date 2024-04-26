"""AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6167,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6035,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6210,
        _6260,
        _6190,
        _6244,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation")


class AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation(
    _6167.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation
):
    """AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6167.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6167.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6190.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6190,
            )

            return self._parent._cast(
                _6190.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6244.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6244,
            )

            return self._parent._cast(
                _6244.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6210.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6210,
            )

            return self._parent._cast(
                _6210.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6260.ShaftCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6260,
            )

            return self._parent._cast(
                _6260.ShaftCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6035.AbstractShaftHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.AbstractShaftHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6035.AbstractShaftHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.AbstractShaftHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation(self)
