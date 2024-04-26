"""MeasurementComponentCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6694
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "MeasurementComponentCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2481
    from mastapy.system_model.analyses_and_results.static_loads import _6949
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6649,
        _6594,
        _6651,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="MeasurementComponentCriticalSpeedAnalysis")


class MeasurementComponentCriticalSpeedAnalysis(
    _6694.VirtualComponentCriticalSpeedAnalysis
):
    """MeasurementComponentCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentCriticalSpeedAnalysis"
    )

    class _Cast_MeasurementComponentCriticalSpeedAnalysis:
        """Special nested class for casting MeasurementComponentCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
            parent: "MeasurementComponentCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_critical_speed_analysis(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ) -> "_6694.VirtualComponentCriticalSpeedAnalysis":
            return self._parent._cast(_6694.VirtualComponentCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ) -> "_6649.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6649,
            )

            return self._parent._cast(_6649.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ) -> "_6594.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6594,
            )

            return self._parent._cast(_6594.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ) -> "_6651.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def measurement_component_critical_speed_analysis(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ) -> "MeasurementComponentCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "MeasurementComponentCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2481.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6949.MeasurementComponentLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase

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
    ) -> "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis":
        return self._Cast_MeasurementComponentCriticalSpeedAnalysis(self)
