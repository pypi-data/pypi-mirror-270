"""PulleyDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "PulleyDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.static_loads import _6967
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6345,
        _6382,
        _6328,
        _6384,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PulleyDynamicAnalysis",)


Self = TypeVar("Self", bound="PulleyDynamicAnalysis")


class PulleyDynamicAnalysis(_6342.CouplingHalfDynamicAnalysis):
    """PulleyDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PULLEY_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyDynamicAnalysis")

    class _Cast_PulleyDynamicAnalysis:
        """Special nested class for casting PulleyDynamicAnalysis to subclasses."""

        def __init__(
            self: "PulleyDynamicAnalysis._Cast_PulleyDynamicAnalysis",
            parent: "PulleyDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_dynamic_analysis(
            self: "PulleyDynamicAnalysis._Cast_PulleyDynamicAnalysis",
        ) -> "_6342.CouplingHalfDynamicAnalysis":
            return self._parent._cast(_6342.CouplingHalfDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "PulleyDynamicAnalysis._Cast_PulleyDynamicAnalysis",
        ) -> "_6382.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "PulleyDynamicAnalysis._Cast_PulleyDynamicAnalysis",
        ) -> "_6328.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "PulleyDynamicAnalysis._Cast_PulleyDynamicAnalysis",
        ) -> "_6384.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "PulleyDynamicAnalysis._Cast_PulleyDynamicAnalysis",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PulleyDynamicAnalysis._Cast_PulleyDynamicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PulleyDynamicAnalysis._Cast_PulleyDynamicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PulleyDynamicAnalysis._Cast_PulleyDynamicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PulleyDynamicAnalysis._Cast_PulleyDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyDynamicAnalysis._Cast_PulleyDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "PulleyDynamicAnalysis._Cast_PulleyDynamicAnalysis",
        ) -> "_6345.CVTPulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345

            return self._parent._cast(_6345.CVTPulleyDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(
            self: "PulleyDynamicAnalysis._Cast_PulleyDynamicAnalysis",
        ) -> "PulleyDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PulleyDynamicAnalysis._Cast_PulleyDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PulleyDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6967.PulleyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PulleyDynamicAnalysis._Cast_PulleyDynamicAnalysis":
        return self._Cast_PulleyDynamicAnalysis(self)
