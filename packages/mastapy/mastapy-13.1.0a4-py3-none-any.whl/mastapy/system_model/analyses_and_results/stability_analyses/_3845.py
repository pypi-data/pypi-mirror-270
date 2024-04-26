"""FlexiblePinAssemblyStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3886
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "FlexiblePinAssemblyStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.static_loads import _6915
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3786,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyStabilityAnalysis",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyStabilityAnalysis")


class FlexiblePinAssemblyStabilityAnalysis(_3886.SpecialisedAssemblyStabilityAnalysis):
    """FlexiblePinAssemblyStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FlexiblePinAssemblyStabilityAnalysis")

    class _Cast_FlexiblePinAssemblyStabilityAnalysis:
        """Special nested class for casting FlexiblePinAssemblyStabilityAnalysis to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyStabilityAnalysis._Cast_FlexiblePinAssemblyStabilityAnalysis",
            parent: "FlexiblePinAssemblyStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_stability_analysis(
            self: "FlexiblePinAssemblyStabilityAnalysis._Cast_FlexiblePinAssemblyStabilityAnalysis",
        ) -> "_3886.SpecialisedAssemblyStabilityAnalysis":
            return self._parent._cast(_3886.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "FlexiblePinAssemblyStabilityAnalysis._Cast_FlexiblePinAssemblyStabilityAnalysis",
        ) -> "_3786.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "FlexiblePinAssemblyStabilityAnalysis._Cast_FlexiblePinAssemblyStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FlexiblePinAssemblyStabilityAnalysis._Cast_FlexiblePinAssemblyStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FlexiblePinAssemblyStabilityAnalysis._Cast_FlexiblePinAssemblyStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FlexiblePinAssemblyStabilityAnalysis._Cast_FlexiblePinAssemblyStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FlexiblePinAssemblyStabilityAnalysis._Cast_FlexiblePinAssemblyStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyStabilityAnalysis._Cast_FlexiblePinAssemblyStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_stability_analysis(
            self: "FlexiblePinAssemblyStabilityAnalysis._Cast_FlexiblePinAssemblyStabilityAnalysis",
        ) -> "FlexiblePinAssemblyStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyStabilityAnalysis._Cast_FlexiblePinAssemblyStabilityAnalysis",
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
        self: Self, instance_to_wrap: "FlexiblePinAssemblyStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2472.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6915.FlexiblePinAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAssemblyStabilityAnalysis._Cast_FlexiblePinAssemblyStabilityAnalysis":
        return self._Cast_FlexiblePinAssemblyStabilityAnalysis(self)
