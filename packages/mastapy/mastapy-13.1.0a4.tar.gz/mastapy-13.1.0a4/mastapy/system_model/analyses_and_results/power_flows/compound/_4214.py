"""CoaxialConnectionCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4287
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "CoaxialConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.power_flows import _4079
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4234,
        _4193,
        _4225,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="CoaxialConnectionCompoundPowerFlow")


class CoaxialConnectionCompoundPowerFlow(
    _4287.ShaftToMountableComponentConnectionCompoundPowerFlow
):
    """CoaxialConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoaxialConnectionCompoundPowerFlow")

    class _Cast_CoaxialConnectionCompoundPowerFlow:
        """Special nested class for casting CoaxialConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "CoaxialConnectionCompoundPowerFlow._Cast_CoaxialConnectionCompoundPowerFlow",
            parent: "CoaxialConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_power_flow(
            self: "CoaxialConnectionCompoundPowerFlow._Cast_CoaxialConnectionCompoundPowerFlow",
        ) -> "_4287.ShaftToMountableComponentConnectionCompoundPowerFlow":
            return self._parent._cast(
                _4287.ShaftToMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_power_flow(
            self: "CoaxialConnectionCompoundPowerFlow._Cast_CoaxialConnectionCompoundPowerFlow",
        ) -> "_4193.AbstractShaftToMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4193,
            )

            return self._parent._cast(
                _4193.AbstractShaftToMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "CoaxialConnectionCompoundPowerFlow._Cast_CoaxialConnectionCompoundPowerFlow",
        ) -> "_4225.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "CoaxialConnectionCompoundPowerFlow._Cast_CoaxialConnectionCompoundPowerFlow",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CoaxialConnectionCompoundPowerFlow._Cast_CoaxialConnectionCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCompoundPowerFlow._Cast_CoaxialConnectionCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_power_flow(
            self: "CoaxialConnectionCompoundPowerFlow._Cast_CoaxialConnectionCompoundPowerFlow",
        ) -> "_4234.CycloidalDiscCentralBearingConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4234,
            )

            return self._parent._cast(
                _4234.CycloidalDiscCentralBearingConnectionCompoundPowerFlow
            )

        @property
        def coaxial_connection_compound_power_flow(
            self: "CoaxialConnectionCompoundPowerFlow._Cast_CoaxialConnectionCompoundPowerFlow",
        ) -> "CoaxialConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCompoundPowerFlow._Cast_CoaxialConnectionCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "CoaxialConnectionCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2287.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4079.CoaxialConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CoaxialConnectionPowerFlow]

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
    ) -> "List[_4079.CoaxialConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CoaxialConnectionPowerFlow]

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
    ) -> "CoaxialConnectionCompoundPowerFlow._Cast_CoaxialConnectionCompoundPowerFlow":
        return self._Cast_CoaxialConnectionCompoundPowerFlow(self)
