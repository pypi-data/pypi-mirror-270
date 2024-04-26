"""PlanetCarrierCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6649
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "PlanetCarrierCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2487
    from mastapy.system_model.analyses_and_results.static_loads import _6962
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6594,
        _6651,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="PlanetCarrierCriticalSpeedAnalysis")


class PlanetCarrierCriticalSpeedAnalysis(_6649.MountableComponentCriticalSpeedAnalysis):
    """PlanetCarrierCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetCarrierCriticalSpeedAnalysis")

    class _Cast_PlanetCarrierCriticalSpeedAnalysis:
        """Special nested class for casting PlanetCarrierCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
            parent: "PlanetCarrierCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_critical_speed_analysis(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "_6649.MountableComponentCriticalSpeedAnalysis":
            return self._parent._cast(_6649.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "_6594.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6594,
            )

            return self._parent._cast(_6594.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "_6651.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planet_carrier_critical_speed_analysis(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
        ) -> "PlanetCarrierCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "PlanetCarrierCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2487.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6962.PlanetCarrierLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase

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
    ) -> "PlanetCarrierCriticalSpeedAnalysis._Cast_PlanetCarrierCriticalSpeedAnalysis":
        return self._Cast_PlanetCarrierCriticalSpeedAnalysis(self)
