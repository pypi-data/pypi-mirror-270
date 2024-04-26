"""ExternalCADModelCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ExternalCADModelCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2470
    from mastapy.system_model.analyses_and_results.static_loads import _6910
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6651
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ExternalCADModelCriticalSpeedAnalysis")


class ExternalCADModelCriticalSpeedAnalysis(_6594.ComponentCriticalSpeedAnalysis):
    """ExternalCADModelCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ExternalCADModelCriticalSpeedAnalysis"
    )

    class _Cast_ExternalCADModelCriticalSpeedAnalysis:
        """Special nested class for casting ExternalCADModelCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ExternalCADModelCriticalSpeedAnalysis._Cast_ExternalCADModelCriticalSpeedAnalysis",
            parent: "ExternalCADModelCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def component_critical_speed_analysis(
            self: "ExternalCADModelCriticalSpeedAnalysis._Cast_ExternalCADModelCriticalSpeedAnalysis",
        ) -> "_6594.ComponentCriticalSpeedAnalysis":
            return self._parent._cast(_6594.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "ExternalCADModelCriticalSpeedAnalysis._Cast_ExternalCADModelCriticalSpeedAnalysis",
        ) -> "_6651.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ExternalCADModelCriticalSpeedAnalysis._Cast_ExternalCADModelCriticalSpeedAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ExternalCADModelCriticalSpeedAnalysis._Cast_ExternalCADModelCriticalSpeedAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ExternalCADModelCriticalSpeedAnalysis._Cast_ExternalCADModelCriticalSpeedAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ExternalCADModelCriticalSpeedAnalysis._Cast_ExternalCADModelCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelCriticalSpeedAnalysis._Cast_ExternalCADModelCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def external_cad_model_critical_speed_analysis(
            self: "ExternalCADModelCriticalSpeedAnalysis._Cast_ExternalCADModelCriticalSpeedAnalysis",
        ) -> "ExternalCADModelCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelCriticalSpeedAnalysis._Cast_ExternalCADModelCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "ExternalCADModelCriticalSpeedAnalysis.TYPE"
    ):
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
    ) -> "ExternalCADModelCriticalSpeedAnalysis._Cast_ExternalCADModelCriticalSpeedAnalysis":
        return self._Cast_ExternalCADModelCriticalSpeedAnalysis(self)
