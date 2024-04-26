"""RollingRingAssemblyStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3886
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "RollingRingAssemblyStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2617
    from mastapy.system_model.analyses_and_results.static_loads import _6972
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3786,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyStabilityAnalysis",)


Self = TypeVar("Self", bound="RollingRingAssemblyStabilityAnalysis")


class RollingRingAssemblyStabilityAnalysis(_3886.SpecialisedAssemblyStabilityAnalysis):
    """RollingRingAssemblyStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingAssemblyStabilityAnalysis")

    class _Cast_RollingRingAssemblyStabilityAnalysis:
        """Special nested class for casting RollingRingAssemblyStabilityAnalysis to subclasses."""

        def __init__(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
            parent: "RollingRingAssemblyStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_stability_analysis(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "_3886.SpecialisedAssemblyStabilityAnalysis":
            return self._parent._cast(_3886.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "_3786.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_stability_analysis(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "RollingRingAssemblyStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
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
        self: Self, instance_to_wrap: "RollingRingAssemblyStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2617.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6972.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

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
    ) -> "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis":
        return self._Cast_RollingRingAssemblyStabilityAnalysis(self)
