"""AbstractShaftOrHousingCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4215
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "AbstractShaftOrHousingCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4056
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4191,
        _4235,
        _4246,
        _4285,
        _4269,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundPowerFlow",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundPowerFlow")


class AbstractShaftOrHousingCompoundPowerFlow(_4215.ComponentCompoundPowerFlow):
    """AbstractShaftOrHousingCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCompoundPowerFlow"
    )

    class _Cast_AbstractShaftOrHousingCompoundPowerFlow:
        """Special nested class for casting AbstractShaftOrHousingCompoundPowerFlow to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
            parent: "AbstractShaftOrHousingCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def component_compound_power_flow(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_4215.ComponentCompoundPowerFlow":
            return self._parent._cast(_4215.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_4269.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_power_flow(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_4191.AbstractShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4191,
            )

            return self._parent._cast(_4191.AbstractShaftCompoundPowerFlow)

        @property
        def cycloidal_disc_compound_power_flow(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_4235.CycloidalDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(_4235.CycloidalDiscCompoundPowerFlow)

        @property
        def fe_part_compound_power_flow(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_4246.FEPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.FEPartCompoundPowerFlow)

        @property
        def shaft_compound_power_flow(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "_4285.ShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4285,
            )

            return self._parent._cast(_4285.ShaftCompoundPowerFlow)

        @property
        def abstract_shaft_or_housing_compound_power_flow(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
        ) -> "AbstractShaftOrHousingCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4056.AbstractShaftOrHousingPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AbstractShaftOrHousingPowerFlow]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4056.AbstractShaftOrHousingPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AbstractShaftOrHousingPowerFlow]

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
    ) -> "AbstractShaftOrHousingCompoundPowerFlow._Cast_AbstractShaftOrHousingCompoundPowerFlow":
        return self._Cast_AbstractShaftOrHousingCompoundPowerFlow(self)
