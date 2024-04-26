"""FEPartStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3787
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "FEPartStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.static_loads import _6914
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3811,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("FEPartStabilityAnalysis",)


Self = TypeVar("Self", bound="FEPartStabilityAnalysis")


class FEPartStabilityAnalysis(_3787.AbstractShaftOrHousingStabilityAnalysis):
    """FEPartStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_PART_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartStabilityAnalysis")

    class _Cast_FEPartStabilityAnalysis:
        """Special nested class for casting FEPartStabilityAnalysis to subclasses."""

        def __init__(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
            parent: "FEPartStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_stability_analysis(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "_3787.AbstractShaftOrHousingStabilityAnalysis":
            return self._parent._cast(_3787.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "_3811.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def fe_part_stability_analysis(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis",
        ) -> "FEPartStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2471.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6914.FEPartLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[FEPartStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.FEPartStabilityAnalysis]

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
    def cast_to(self: Self) -> "FEPartStabilityAnalysis._Cast_FEPartStabilityAnalysis":
        return self._Cast_FEPartStabilityAnalysis(self)
