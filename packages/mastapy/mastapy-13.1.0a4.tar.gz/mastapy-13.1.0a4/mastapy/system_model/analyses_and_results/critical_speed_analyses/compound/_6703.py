"""AbstractShaftOrHousingCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6726,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6571
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6702,
        _6746,
        _6757,
        _6796,
        _6780,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundCriticalSpeedAnalysis")


class AbstractShaftOrHousingCompoundCriticalSpeedAnalysis(
    _6726.ComponentCompoundCriticalSpeedAnalysis
):
    """AbstractShaftOrHousingCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis"
    )

    class _Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis:
        """Special nested class for casting AbstractShaftOrHousingCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
            parent: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_critical_speed_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ) -> "_6726.ComponentCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6726.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ) -> "_6780.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(_6780.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_critical_speed_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ) -> "_6702.AbstractShaftCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6702,
            )

            return self._parent._cast(_6702.AbstractShaftCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_compound_critical_speed_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ) -> "_6746.CycloidalDiscCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6746,
            )

            return self._parent._cast(_6746.CycloidalDiscCompoundCriticalSpeedAnalysis)

        @property
        def fe_part_compound_critical_speed_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ) -> "_6757.FEPartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6757,
            )

            return self._parent._cast(_6757.FEPartCompoundCriticalSpeedAnalysis)

        @property
        def shaft_compound_critical_speed_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ) -> "_6796.ShaftCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6796,
            )

            return self._parent._cast(_6796.ShaftCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_compound_critical_speed_analysis(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
        ) -> "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6571.AbstractShaftOrHousingCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractShaftOrHousingCriticalSpeedAnalysis]

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
    ) -> "List[_6571.AbstractShaftOrHousingCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractShaftOrHousingCriticalSpeedAnalysis]

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
    ) -> "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis":
        return self._Cast_AbstractShaftOrHousingCompoundCriticalSpeedAnalysis(self)
