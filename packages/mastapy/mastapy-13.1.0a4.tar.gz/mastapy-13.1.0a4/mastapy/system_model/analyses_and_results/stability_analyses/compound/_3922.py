"""AbstractShaftOrHousingCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3945
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "AbstractShaftOrHousingCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3787
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3921,
        _3965,
        _3976,
        _4015,
        _3999,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundStabilityAnalysis")


class AbstractShaftOrHousingCompoundStabilityAnalysis(
    _3945.ComponentCompoundStabilityAnalysis
):
    """AbstractShaftOrHousingCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCompoundStabilityAnalysis"
    )

    class _Cast_AbstractShaftOrHousingCompoundStabilityAnalysis:
        """Special nested class for casting AbstractShaftOrHousingCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
            parent: "AbstractShaftOrHousingCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_stability_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ) -> "_3945.ComponentCompoundStabilityAnalysis":
            return self._parent._cast(_3945.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ) -> "_3999.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_stability_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ) -> "_3921.AbstractShaftCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3921,
            )

            return self._parent._cast(_3921.AbstractShaftCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_compound_stability_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ) -> "_3965.CycloidalDiscCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3965,
            )

            return self._parent._cast(_3965.CycloidalDiscCompoundStabilityAnalysis)

        @property
        def fe_part_compound_stability_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ) -> "_3976.FEPartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.FEPartCompoundStabilityAnalysis)

        @property
        def shaft_compound_stability_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ) -> "_4015.ShaftCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4015,
            )

            return self._parent._cast(_4015.ShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ) -> "AbstractShaftOrHousingCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3787.AbstractShaftOrHousingStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractShaftOrHousingStabilityAnalysis]

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
    ) -> "List[_3787.AbstractShaftOrHousingStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractShaftOrHousingStabilityAnalysis]

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
    ) -> "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis":
        return self._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis(self)
