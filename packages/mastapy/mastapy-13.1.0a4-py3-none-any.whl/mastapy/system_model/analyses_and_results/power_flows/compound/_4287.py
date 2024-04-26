"""ShaftToMountableComponentConnectionCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4193
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ShaftToMountableComponentConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4157
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4214,
        _4234,
        _4273,
        _4225,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionCompoundPowerFlow")


class ShaftToMountableComponentConnectionCompoundPowerFlow(
    _4193.AbstractShaftToMountableComponentConnectionCompoundPowerFlow
):
    """ShaftToMountableComponentConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftToMountableComponentConnectionCompoundPowerFlow"
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundPowerFlow:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
            parent: "ShaftToMountableComponentConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_power_flow(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "_4193.AbstractShaftToMountableComponentConnectionCompoundPowerFlow":
            return self._parent._cast(
                _4193.AbstractShaftToMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "_4225.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_power_flow(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "_4214.CoaxialConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4214,
            )

            return self._parent._cast(_4214.CoaxialConnectionCompoundPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_compound_power_flow(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "_4234.CycloidalDiscCentralBearingConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4234,
            )

            return self._parent._cast(
                _4234.CycloidalDiscCentralBearingConnectionCompoundPowerFlow
            )

        @property
        def planetary_connection_compound_power_flow(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "_4273.PlanetaryConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.PlanetaryConnectionCompoundPowerFlow)

        @property
        def shaft_to_mountable_component_connection_compound_power_flow(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "ShaftToMountableComponentConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4157.ShaftToMountableComponentConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ShaftToMountableComponentConnectionPowerFlow]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4157.ShaftToMountableComponentConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ShaftToMountableComponentConnectionPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionCompoundPowerFlow._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow":
        return self._Cast_ShaftToMountableComponentConnectionCompoundPowerFlow(self)
