"""ExternalCADModelDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ExternalCADModelDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2470
    from mastapy.system_model.analyses_and_results.static_loads import _6910
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelDynamicAnalysis",)


Self = TypeVar("Self", bound="ExternalCADModelDynamicAnalysis")


class ExternalCADModelDynamicAnalysis(_6328.ComponentDynamicAnalysis):
    """ExternalCADModelDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ExternalCADModelDynamicAnalysis")

    class _Cast_ExternalCADModelDynamicAnalysis:
        """Special nested class for casting ExternalCADModelDynamicAnalysis to subclasses."""

        def __init__(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
            parent: "ExternalCADModelDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def component_dynamic_analysis(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ) -> "_6328.ComponentDynamicAnalysis":
            return self._parent._cast(_6328.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ) -> "_6384.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def external_cad_model_dynamic_analysis(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ) -> "ExternalCADModelDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ExternalCADModelDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2470.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6910.ExternalCADModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase

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
    ) -> "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis":
        return self._Cast_ExternalCADModelDynamicAnalysis(self)
