"""CycloidalDiscCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5906
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "CycloidalDiscCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2587
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5751
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5907,
        _5930,
        _5984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscCompoundHarmonicAnalysis")


class CycloidalDiscCompoundHarmonicAnalysis(
    _5906.AbstractShaftCompoundHarmonicAnalysis
):
    """CycloidalDiscCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCompoundHarmonicAnalysis"
    )

    class _Cast_CycloidalDiscCompoundHarmonicAnalysis:
        """Special nested class for casting CycloidalDiscCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
            parent: "CycloidalDiscCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_harmonic_analysis(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
        ) -> "_5906.AbstractShaftCompoundHarmonicAnalysis":
            return self._parent._cast(_5906.AbstractShaftCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
        ) -> "_5907.AbstractShaftOrHousingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5907,
            )

            return self._parent._cast(
                _5907.AbstractShaftOrHousingCompoundHarmonicAnalysis
            )

        @property
        def component_compound_harmonic_analysis(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
        ) -> "_5930.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
        ) -> "_5984.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(_5984.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_harmonic_analysis(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
        ) -> "CycloidalDiscCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "CycloidalDiscCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2587.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5751.CycloidalDiscHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscHarmonicAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5751.CycloidalDiscHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis":
        return self._Cast_CycloidalDiscCompoundHarmonicAnalysis(self)
