"""BoltCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3945
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "BoltCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.stability_analyses import _3806
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3999,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BoltCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="BoltCompoundStabilityAnalysis")


class BoltCompoundStabilityAnalysis(_3945.ComponentCompoundStabilityAnalysis):
    """BoltCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLT_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltCompoundStabilityAnalysis")

    class _Cast_BoltCompoundStabilityAnalysis:
        """Special nested class for casting BoltCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "BoltCompoundStabilityAnalysis._Cast_BoltCompoundStabilityAnalysis",
            parent: "BoltCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_stability_analysis(
            self: "BoltCompoundStabilityAnalysis._Cast_BoltCompoundStabilityAnalysis",
        ) -> "_3945.ComponentCompoundStabilityAnalysis":
            return self._parent._cast(_3945.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "BoltCompoundStabilityAnalysis._Cast_BoltCompoundStabilityAnalysis",
        ) -> "_3999.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "BoltCompoundStabilityAnalysis._Cast_BoltCompoundStabilityAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BoltCompoundStabilityAnalysis._Cast_BoltCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltCompoundStabilityAnalysis._Cast_BoltCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bolt_compound_stability_analysis(
            self: "BoltCompoundStabilityAnalysis._Cast_BoltCompoundStabilityAnalysis",
        ) -> "BoltCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltCompoundStabilityAnalysis._Cast_BoltCompoundStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltCompoundStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2460.Bolt":
        """mastapy.system_model.part_model.Bolt

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
    ) -> "List[_3806.BoltStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BoltStabilityAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_3806.BoltStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BoltStabilityAnalysis]

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
    ) -> "BoltCompoundStabilityAnalysis._Cast_BoltCompoundStabilityAnalysis":
        return self._Cast_BoltCompoundStabilityAnalysis(self)
