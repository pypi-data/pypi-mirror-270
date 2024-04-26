"""AbstractShaftOrHousingCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6459
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "AbstractShaftOrHousingCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6435,
        _6479,
        _6490,
        _6529,
        _6513,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundDynamicAnalysis")


class AbstractShaftOrHousingCompoundDynamicAnalysis(
    _6459.ComponentCompoundDynamicAnalysis
):
    """AbstractShaftOrHousingCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCompoundDynamicAnalysis"
    )

    class _Cast_AbstractShaftOrHousingCompoundDynamicAnalysis:
        """Special nested class for casting AbstractShaftOrHousingCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
            parent: "AbstractShaftOrHousingCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_dynamic_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ) -> "_6459.ComponentCompoundDynamicAnalysis":
            return self._parent._cast(_6459.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ) -> "_6513.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6513,
            )

            return self._parent._cast(_6513.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_dynamic_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ) -> "_6435.AbstractShaftCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6435,
            )

            return self._parent._cast(_6435.AbstractShaftCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_compound_dynamic_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ) -> "_6479.CycloidalDiscCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6479,
            )

            return self._parent._cast(_6479.CycloidalDiscCompoundDynamicAnalysis)

        @property
        def fe_part_compound_dynamic_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ) -> "_6490.FEPartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6490,
            )

            return self._parent._cast(_6490.FEPartCompoundDynamicAnalysis)

        @property
        def shaft_compound_dynamic_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ) -> "_6529.ShaftCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6529,
            )

            return self._parent._cast(_6529.ShaftCompoundDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_dynamic_analysis(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
        ) -> "AbstractShaftOrHousingCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6305.AbstractShaftOrHousingDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftOrHousingDynamicAnalysis]

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
    ) -> "List[_6305.AbstractShaftOrHousingDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftOrHousingDynamicAnalysis]

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
    ) -> "AbstractShaftOrHousingCompoundDynamicAnalysis._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis":
        return self._Cast_AbstractShaftOrHousingCompoundDynamicAnalysis(self)
