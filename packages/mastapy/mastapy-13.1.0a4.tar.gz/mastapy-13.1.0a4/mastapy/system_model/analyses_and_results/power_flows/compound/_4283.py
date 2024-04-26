"""RollingRingConnectionCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4255
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "RollingRingConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2310
    from mastapy.system_model.analyses_and_results.power_flows import _4152
    from mastapy.system_model.analyses_and_results.power_flows.compound import _4225
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="RollingRingConnectionCompoundPowerFlow")


class RollingRingConnectionCompoundPowerFlow(
    _4255.InterMountableComponentConnectionCompoundPowerFlow
):
    """RollingRingConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingConnectionCompoundPowerFlow"
    )

    class _Cast_RollingRingConnectionCompoundPowerFlow:
        """Special nested class for casting RollingRingConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "RollingRingConnectionCompoundPowerFlow._Cast_RollingRingConnectionCompoundPowerFlow",
            parent: "RollingRingConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "RollingRingConnectionCompoundPowerFlow._Cast_RollingRingConnectionCompoundPowerFlow",
        ) -> "_4255.InterMountableComponentConnectionCompoundPowerFlow":
            return self._parent._cast(
                _4255.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "RollingRingConnectionCompoundPowerFlow._Cast_RollingRingConnectionCompoundPowerFlow",
        ) -> "_4225.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "RollingRingConnectionCompoundPowerFlow._Cast_RollingRingConnectionCompoundPowerFlow",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingConnectionCompoundPowerFlow._Cast_RollingRingConnectionCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionCompoundPowerFlow._Cast_RollingRingConnectionCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_compound_power_flow(
            self: "RollingRingConnectionCompoundPowerFlow._Cast_RollingRingConnectionCompoundPowerFlow",
        ) -> "RollingRingConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionCompoundPowerFlow._Cast_RollingRingConnectionCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "RollingRingConnectionCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2310.RollingRingConnection":
        """mastapy.system_model.connections_and_sockets.RollingRingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2310.RollingRingConnection":
        """mastapy.system_model.connections_and_sockets.RollingRingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4152.RollingRingConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.RollingRingConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4152.RollingRingConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.RollingRingConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingConnectionCompoundPowerFlow._Cast_RollingRingConnectionCompoundPowerFlow":
        return self._Cast_RollingRingConnectionCompoundPowerFlow(self)
