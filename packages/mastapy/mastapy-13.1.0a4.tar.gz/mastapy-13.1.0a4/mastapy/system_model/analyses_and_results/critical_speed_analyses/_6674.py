"""SpringDamperConnectionCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6606
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "SpringDamperConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2368
    from mastapy.system_model.analyses_and_results.static_loads import _6983
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6637,
        _6604,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SpringDamperConnectionCriticalSpeedAnalysis")


class SpringDamperConnectionCriticalSpeedAnalysis(
    _6606.CouplingConnectionCriticalSpeedAnalysis
):
    """SpringDamperConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperConnectionCriticalSpeedAnalysis"
    )

    class _Cast_SpringDamperConnectionCriticalSpeedAnalysis:
        """Special nested class for casting SpringDamperConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperConnectionCriticalSpeedAnalysis._Cast_SpringDamperConnectionCriticalSpeedAnalysis",
            parent: "SpringDamperConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_critical_speed_analysis(
            self: "SpringDamperConnectionCriticalSpeedAnalysis._Cast_SpringDamperConnectionCriticalSpeedAnalysis",
        ) -> "_6606.CouplingConnectionCriticalSpeedAnalysis":
            return self._parent._cast(_6606.CouplingConnectionCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "SpringDamperConnectionCriticalSpeedAnalysis._Cast_SpringDamperConnectionCriticalSpeedAnalysis",
        ) -> "_6637.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6637,
            )

            return self._parent._cast(
                _6637.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "SpringDamperConnectionCriticalSpeedAnalysis._Cast_SpringDamperConnectionCriticalSpeedAnalysis",
        ) -> "_6604.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6604,
            )

            return self._parent._cast(_6604.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "SpringDamperConnectionCriticalSpeedAnalysis._Cast_SpringDamperConnectionCriticalSpeedAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpringDamperConnectionCriticalSpeedAnalysis._Cast_SpringDamperConnectionCriticalSpeedAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpringDamperConnectionCriticalSpeedAnalysis._Cast_SpringDamperConnectionCriticalSpeedAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperConnectionCriticalSpeedAnalysis._Cast_SpringDamperConnectionCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionCriticalSpeedAnalysis._Cast_SpringDamperConnectionCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spring_damper_connection_critical_speed_analysis(
            self: "SpringDamperConnectionCriticalSpeedAnalysis._Cast_SpringDamperConnectionCriticalSpeedAnalysis",
        ) -> "SpringDamperConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionCriticalSpeedAnalysis._Cast_SpringDamperConnectionCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "SpringDamperConnectionCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2368.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6983.SpringDamperConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase

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
    ) -> "SpringDamperConnectionCriticalSpeedAnalysis._Cast_SpringDamperConnectionCriticalSpeedAnalysis":
        return self._Cast_SpringDamperConnectionCriticalSpeedAnalysis(self)
