"""AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7169,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7033,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7212,
        _7262,
        _7192,
        _7246,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7169.AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7169.AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7169.AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7192.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7192,
            )

            return self._parent._cast(
                _7192.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7246.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7246,
            )

            return self._parent._cast(
                _7246.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7212.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7212,
            )

            return self._parent._cast(
                _7212.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7262.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7262,
            )

            return self._parent._cast(
                _7262.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7033.AbstractShaftAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AbstractShaftAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7033.AbstractShaftAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AbstractShaftAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation":
        return (
            self._Cast_AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation(
                self
            )
        )
