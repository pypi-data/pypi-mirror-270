"""UnbalancedMassStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3913
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "UnbalancedMassStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2495
    from mastapy.system_model.analyses_and_results.static_loads import _7007
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3865,
        _3811,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassStabilityAnalysis",)


Self = TypeVar("Self", bound="UnbalancedMassStabilityAnalysis")


class UnbalancedMassStabilityAnalysis(_3913.VirtualComponentStabilityAnalysis):
    """UnbalancedMassStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UnbalancedMassStabilityAnalysis")

    class _Cast_UnbalancedMassStabilityAnalysis:
        """Special nested class for casting UnbalancedMassStabilityAnalysis to subclasses."""

        def __init__(
            self: "UnbalancedMassStabilityAnalysis._Cast_UnbalancedMassStabilityAnalysis",
            parent: "UnbalancedMassStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_stability_analysis(
            self: "UnbalancedMassStabilityAnalysis._Cast_UnbalancedMassStabilityAnalysis",
        ) -> "_3913.VirtualComponentStabilityAnalysis":
            return self._parent._cast(_3913.VirtualComponentStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "UnbalancedMassStabilityAnalysis._Cast_UnbalancedMassStabilityAnalysis",
        ) -> "_3865.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "UnbalancedMassStabilityAnalysis._Cast_UnbalancedMassStabilityAnalysis",
        ) -> "_3811.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "UnbalancedMassStabilityAnalysis._Cast_UnbalancedMassStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "UnbalancedMassStabilityAnalysis._Cast_UnbalancedMassStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "UnbalancedMassStabilityAnalysis._Cast_UnbalancedMassStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "UnbalancedMassStabilityAnalysis._Cast_UnbalancedMassStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "UnbalancedMassStabilityAnalysis._Cast_UnbalancedMassStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassStabilityAnalysis._Cast_UnbalancedMassStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(
            self: "UnbalancedMassStabilityAnalysis._Cast_UnbalancedMassStabilityAnalysis",
        ) -> "UnbalancedMassStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassStabilityAnalysis._Cast_UnbalancedMassStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "UnbalancedMassStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2495.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_7007.UnbalancedMassLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase

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
    ) -> "UnbalancedMassStabilityAnalysis._Cast_UnbalancedMassStabilityAnalysis":
        return self._Cast_UnbalancedMassStabilityAnalysis(self)
