"""AbstractShaftCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5907
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "AbstractShaftCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5706
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5950,
        _6000,
        _5930,
        _5984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftCompoundHarmonicAnalysis")


class AbstractShaftCompoundHarmonicAnalysis(
    _5907.AbstractShaftOrHousingCompoundHarmonicAnalysis
):
    """AbstractShaftCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftCompoundHarmonicAnalysis"
    )

    class _Cast_AbstractShaftCompoundHarmonicAnalysis:
        """Special nested class for casting AbstractShaftCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
            parent: "AbstractShaftCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "_5907.AbstractShaftOrHousingCompoundHarmonicAnalysis":
            return self._parent._cast(
                _5907.AbstractShaftOrHousingCompoundHarmonicAnalysis
            )

        @property
        def component_compound_harmonic_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "_5930.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "_5984.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(_5984.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_harmonic_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "_5950.CycloidalDiscCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5950,
            )

            return self._parent._cast(_5950.CycloidalDiscCompoundHarmonicAnalysis)

        @property
        def shaft_compound_harmonic_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "_6000.ShaftCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6000,
            )

            return self._parent._cast(_6000.ShaftCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_compound_harmonic_analysis(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
        ) -> "AbstractShaftCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5706.AbstractShaftHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractShaftHarmonicAnalysis]

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
    ) -> "List[_5706.AbstractShaftHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractShaftHarmonicAnalysis]

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
    ) -> "AbstractShaftCompoundHarmonicAnalysis._Cast_AbstractShaftCompoundHarmonicAnalysis":
        return self._Cast_AbstractShaftCompoundHarmonicAnalysis(self)
