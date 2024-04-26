"""CycloidalDiscStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3788
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CycloidalDiscStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2587
    from mastapy.system_model.analyses_and_results.static_loads import _6886
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3787,
        _3811,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscStabilityAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscStabilityAnalysis")


class CycloidalDiscStabilityAnalysis(_3788.AbstractShaftStabilityAnalysis):
    """CycloidalDiscStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscStabilityAnalysis")

    class _Cast_CycloidalDiscStabilityAnalysis:
        """Special nested class for casting CycloidalDiscStabilityAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
            parent: "CycloidalDiscStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_stability_analysis(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_3788.AbstractShaftStabilityAnalysis":
            return self._parent._cast(_3788.AbstractShaftStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_stability_analysis(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_3787.AbstractShaftOrHousingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3787,
            )

            return self._parent._cast(_3787.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_3811.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_stability_analysis(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
        ) -> "CycloidalDiscStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscStabilityAnalysis.TYPE"):
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
    def component_load_case(self: Self) -> "_6886.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscStabilityAnalysis._Cast_CycloidalDiscStabilityAnalysis":
        return self._Cast_CycloidalDiscStabilityAnalysis(self)
