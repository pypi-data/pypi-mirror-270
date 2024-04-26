"""AbstractShaftCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3922
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "AbstractShaftCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3788
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3965,
        _4015,
        _3945,
        _3999,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftCompoundStabilityAnalysis")


class AbstractShaftCompoundStabilityAnalysis(
    _3922.AbstractShaftOrHousingCompoundStabilityAnalysis
):
    """AbstractShaftCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftCompoundStabilityAnalysis"
    )

    class _Cast_AbstractShaftCompoundStabilityAnalysis:
        """Special nested class for casting AbstractShaftCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
            parent: "AbstractShaftCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_3922.AbstractShaftOrHousingCompoundStabilityAnalysis":
            return self._parent._cast(
                _3922.AbstractShaftOrHousingCompoundStabilityAnalysis
            )

        @property
        def component_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_3945.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3945,
            )

            return self._parent._cast(_3945.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_3999.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_3965.CycloidalDiscCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3965,
            )

            return self._parent._cast(_3965.CycloidalDiscCompoundStabilityAnalysis)

        @property
        def shaft_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "_4015.ShaftCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4015,
            )

            return self._parent._cast(_4015.ShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_compound_stability_analysis(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
        ) -> "AbstractShaftCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3788.AbstractShaftStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractShaftStabilityAnalysis]

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
    ) -> "List[_3788.AbstractShaftStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractShaftStabilityAnalysis]

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
    ) -> "AbstractShaftCompoundStabilityAnalysis._Cast_AbstractShaftCompoundStabilityAnalysis":
        return self._Cast_AbstractShaftCompoundStabilityAnalysis(self)
