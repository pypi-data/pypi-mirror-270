"""SpringDamperHalfStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3824
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "SpringDamperHalfStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2624
    from mastapy.system_model.analyses_and_results.static_loads import _6984
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3865,
        _3811,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfStabilityAnalysis",)


Self = TypeVar("Self", bound="SpringDamperHalfStabilityAnalysis")


class SpringDamperHalfStabilityAnalysis(_3824.CouplingHalfStabilityAnalysis):
    """SpringDamperHalfStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperHalfStabilityAnalysis")

    class _Cast_SpringDamperHalfStabilityAnalysis:
        """Special nested class for casting SpringDamperHalfStabilityAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperHalfStabilityAnalysis._Cast_SpringDamperHalfStabilityAnalysis",
            parent: "SpringDamperHalfStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_stability_analysis(
            self: "SpringDamperHalfStabilityAnalysis._Cast_SpringDamperHalfStabilityAnalysis",
        ) -> "_3824.CouplingHalfStabilityAnalysis":
            return self._parent._cast(_3824.CouplingHalfStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "SpringDamperHalfStabilityAnalysis._Cast_SpringDamperHalfStabilityAnalysis",
        ) -> "_3865.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "SpringDamperHalfStabilityAnalysis._Cast_SpringDamperHalfStabilityAnalysis",
        ) -> "_3811.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "SpringDamperHalfStabilityAnalysis._Cast_SpringDamperHalfStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperHalfStabilityAnalysis._Cast_SpringDamperHalfStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperHalfStabilityAnalysis._Cast_SpringDamperHalfStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperHalfStabilityAnalysis._Cast_SpringDamperHalfStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperHalfStabilityAnalysis._Cast_SpringDamperHalfStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfStabilityAnalysis._Cast_SpringDamperHalfStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spring_damper_half_stability_analysis(
            self: "SpringDamperHalfStabilityAnalysis._Cast_SpringDamperHalfStabilityAnalysis",
        ) -> "SpringDamperHalfStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfStabilityAnalysis._Cast_SpringDamperHalfStabilityAnalysis",
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
        self: Self, instance_to_wrap: "SpringDamperHalfStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2624.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6984.SpringDamperHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase

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
    ) -> "SpringDamperHalfStabilityAnalysis._Cast_SpringDamperHalfStabilityAnalysis":
        return self._Cast_SpringDamperHalfStabilityAnalysis(self)
