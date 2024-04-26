"""ShaftStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3788
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ShaftStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2500
    from mastapy.system_model.analyses_and_results.static_loads import _6977
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3826,
        _3787,
        _3811,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ShaftStabilityAnalysis",)


Self = TypeVar("Self", bound="ShaftStabilityAnalysis")


class ShaftStabilityAnalysis(_3788.AbstractShaftStabilityAnalysis):
    """ShaftStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftStabilityAnalysis")

    class _Cast_ShaftStabilityAnalysis:
        """Special nested class for casting ShaftStabilityAnalysis to subclasses."""

        def __init__(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
            parent: "ShaftStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_stability_analysis(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_3788.AbstractShaftStabilityAnalysis":
            return self._parent._cast(_3788.AbstractShaftStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_stability_analysis(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_3787.AbstractShaftOrHousingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3787,
            )

            return self._parent._cast(_3787.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_3811.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def shaft_stability_analysis(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis",
        ) -> "ShaftStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2500.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6977.ShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def critical_speeds(self: Self) -> "List[_3826.CriticalSpeed]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CriticalSpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CriticalSpeeds

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[ShaftStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ShaftStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis":
        return self._Cast_ShaftStabilityAnalysis(self)
