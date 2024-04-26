"""CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6572
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
        "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2356
    from mastapy.system_model.analyses_and_results.static_loads import _6887
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6604
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis"
)


class CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis(
    _6572.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
):
    """CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
            parent: "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
        ) -> "_6572.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis":
            return self._parent._cast(
                _6572.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
        ) -> "_6604.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6604,
            )

            return self._parent._cast(_6604.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_critical_speed_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
        ) -> "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
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
        self: Self,
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2356.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6887.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase

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
    ) -> "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis(
            self
        )
