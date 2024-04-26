"""CoaxialConnectionPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4157
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "CoaxialConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.static_loads import _6863
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4099,
        _4058,
        _4090,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionPowerFlow",)


Self = TypeVar("Self", bound="CoaxialConnectionPowerFlow")


class CoaxialConnectionPowerFlow(_4157.ShaftToMountableComponentConnectionPowerFlow):
    """CoaxialConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoaxialConnectionPowerFlow")

    class _Cast_CoaxialConnectionPowerFlow:
        """Special nested class for casting CoaxialConnectionPowerFlow to subclasses."""

        def __init__(
            self: "CoaxialConnectionPowerFlow._Cast_CoaxialConnectionPowerFlow",
            parent: "CoaxialConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_power_flow(
            self: "CoaxialConnectionPowerFlow._Cast_CoaxialConnectionPowerFlow",
        ) -> "_4157.ShaftToMountableComponentConnectionPowerFlow":
            return self._parent._cast(
                _4157.ShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def abstract_shaft_to_mountable_component_connection_power_flow(
            self: "CoaxialConnectionPowerFlow._Cast_CoaxialConnectionPowerFlow",
        ) -> "_4058.AbstractShaftToMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4058

            return self._parent._cast(
                _4058.AbstractShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def connection_power_flow(
            self: "CoaxialConnectionPowerFlow._Cast_CoaxialConnectionPowerFlow",
        ) -> "_4090.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4090

            return self._parent._cast(_4090.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionPowerFlow._Cast_CoaxialConnectionPowerFlow",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionPowerFlow._Cast_CoaxialConnectionPowerFlow",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionPowerFlow._Cast_CoaxialConnectionPowerFlow",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionPowerFlow._Cast_CoaxialConnectionPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionPowerFlow._Cast_CoaxialConnectionPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_power_flow(
            self: "CoaxialConnectionPowerFlow._Cast_CoaxialConnectionPowerFlow",
        ) -> "_4099.CycloidalDiscCentralBearingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(
                _4099.CycloidalDiscCentralBearingConnectionPowerFlow
            )

        @property
        def coaxial_connection_power_flow(
            self: "CoaxialConnectionPowerFlow._Cast_CoaxialConnectionPowerFlow",
        ) -> "CoaxialConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionPowerFlow._Cast_CoaxialConnectionPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CoaxialConnectionPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2287.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6863.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

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
    ) -> "CoaxialConnectionPowerFlow._Cast_CoaxialConnectionPowerFlow":
        return self._Cast_CoaxialConnectionPowerFlow(self)
