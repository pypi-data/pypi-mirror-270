"""PlanetaryConnectionCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6669
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "PlanetaryConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2305
    from mastapy.system_model.analyses_and_results.static_loads import _6959
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6572,
        _6604,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="PlanetaryConnectionCriticalSpeedAnalysis")


class PlanetaryConnectionCriticalSpeedAnalysis(
    _6669.ShaftToMountableComponentConnectionCriticalSpeedAnalysis
):
    """PlanetaryConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionCriticalSpeedAnalysis"
    )

    class _Cast_PlanetaryConnectionCriticalSpeedAnalysis:
        """Special nested class for casting PlanetaryConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
            parent: "PlanetaryConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "_6669.ShaftToMountableComponentConnectionCriticalSpeedAnalysis":
            return self._parent._cast(
                _6669.ShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "_6572.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6572,
            )

            return self._parent._cast(
                _6572.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "_6604.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6604,
            )

            return self._parent._cast(_6604.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planetary_connection_critical_speed_analysis(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
        ) -> "PlanetaryConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryConnectionCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2305.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6959.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryConnectionCriticalSpeedAnalysis._Cast_PlanetaryConnectionCriticalSpeedAnalysis":
        return self._Cast_PlanetaryConnectionCriticalSpeedAnalysis(self)
