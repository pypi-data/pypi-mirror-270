"""ConnectorCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4267
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ConnectorCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4091
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4198,
        _4268,
        _4286,
        _4215,
        _4269,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCompoundPowerFlow",)


Self = TypeVar("Self", bound="ConnectorCompoundPowerFlow")


class ConnectorCompoundPowerFlow(_4267.MountableComponentCompoundPowerFlow):
    """ConnectorCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorCompoundPowerFlow")

    class _Cast_ConnectorCompoundPowerFlow:
        """Special nested class for casting ConnectorCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
            parent: "ConnectorCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_power_flow(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_4267.MountableComponentCompoundPowerFlow":
            return self._parent._cast(_4267.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_4215.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4215,
            )

            return self._parent._cast(_4215.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_4269.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bearing_compound_power_flow(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_4198.BearingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.BearingCompoundPowerFlow)

        @property
        def oil_seal_compound_power_flow(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_4268.OilSealCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4268,
            )

            return self._parent._cast(_4268.OilSealCompoundPowerFlow)

        @property
        def shaft_hub_connection_compound_power_flow(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "_4286.ShaftHubConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4286,
            )

            return self._parent._cast(_4286.ShaftHubConnectionCompoundPowerFlow)

        @property
        def connector_compound_power_flow(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
        ) -> "ConnectorCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4091.ConnectorPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConnectorPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4091.ConnectorPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConnectorPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorCompoundPowerFlow._Cast_ConnectorCompoundPowerFlow":
        return self._Cast_ConnectorCompoundPowerFlow(self)
