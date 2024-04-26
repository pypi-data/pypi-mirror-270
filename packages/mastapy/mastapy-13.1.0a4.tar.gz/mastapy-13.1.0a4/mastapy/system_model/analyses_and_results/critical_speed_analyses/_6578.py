"""BeltConnectionCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6637
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "BeltConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2286
    from mastapy.system_model.analyses_and_results.static_loads import _6847
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6612,
        _6604,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BeltConnectionCriticalSpeedAnalysis")


class BeltConnectionCriticalSpeedAnalysis(
    _6637.InterMountableComponentConnectionCriticalSpeedAnalysis
):
    """BeltConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltConnectionCriticalSpeedAnalysis")

    class _Cast_BeltConnectionCriticalSpeedAnalysis:
        """Special nested class for casting BeltConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
            parent: "BeltConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ) -> "_6637.InterMountableComponentConnectionCriticalSpeedAnalysis":
            return self._parent._cast(
                _6637.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ) -> "_6604.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6604,
            )

            return self._parent._cast(_6604.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_critical_speed_analysis(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ) -> "_6612.CVTBeltConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6612,
            )

            return self._parent._cast(_6612.CVTBeltConnectionCriticalSpeedAnalysis)

        @property
        def belt_connection_critical_speed_analysis(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ) -> "BeltConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "BeltConnectionCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2286.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6847.BeltConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase

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
    ) -> (
        "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis"
    ):
        return self._Cast_BeltConnectionCriticalSpeedAnalysis(self)
