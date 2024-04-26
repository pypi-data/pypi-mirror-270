"""CycloidalDiscCentralBearingConnectionCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4214
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4099
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4287,
        _4193,
        _4225,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="CycloidalDiscCentralBearingConnectionCompoundPowerFlow")


class CycloidalDiscCentralBearingConnectionCompoundPowerFlow(
    _4214.CoaxialConnectionCompoundPowerFlow
):
    """CycloidalDiscCentralBearingConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundPowerFlow:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundPowerFlow._Cast_CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
            parent: "CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_power_flow(
            self: "CycloidalDiscCentralBearingConnectionCompoundPowerFlow._Cast_CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
        ) -> "_4214.CoaxialConnectionCompoundPowerFlow":
            return self._parent._cast(_4214.CoaxialConnectionCompoundPowerFlow)

        @property
        def shaft_to_mountable_component_connection_compound_power_flow(
            self: "CycloidalDiscCentralBearingConnectionCompoundPowerFlow._Cast_CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
        ) -> "_4287.ShaftToMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4287,
            )

            return self._parent._cast(
                _4287.ShaftToMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_power_flow(
            self: "CycloidalDiscCentralBearingConnectionCompoundPowerFlow._Cast_CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
        ) -> "_4193.AbstractShaftToMountableComponentConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4193,
            )

            return self._parent._cast(
                _4193.AbstractShaftToMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "CycloidalDiscCentralBearingConnectionCompoundPowerFlow._Cast_CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
        ) -> "_4225.ConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundPowerFlow._Cast_CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundPowerFlow._Cast_CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundPowerFlow._Cast_CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_power_flow(
            self: "CycloidalDiscCentralBearingConnectionCompoundPowerFlow._Cast_CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundPowerFlow._Cast_CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4099.CycloidalDiscCentralBearingConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CycloidalDiscCentralBearingConnectionPowerFlow]

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
    ) -> "List[_4099.CycloidalDiscCentralBearingConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CycloidalDiscCentralBearingConnectionPowerFlow]

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
    ) -> "CycloidalDiscCentralBearingConnectionCompoundPowerFlow._Cast_CycloidalDiscCentralBearingConnectionCompoundPowerFlow":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundPowerFlow(self)
