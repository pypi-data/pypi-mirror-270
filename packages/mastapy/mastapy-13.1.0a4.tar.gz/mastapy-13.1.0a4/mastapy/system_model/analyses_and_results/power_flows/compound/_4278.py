"""PulleyCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4229
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "PulleyCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.power_flows import _4148
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4232,
        _4267,
        _4215,
        _4269,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("PulleyCompoundPowerFlow",)


Self = TypeVar("Self", bound="PulleyCompoundPowerFlow")


class PulleyCompoundPowerFlow(_4229.CouplingHalfCompoundPowerFlow):
    """PulleyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _PULLEY_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyCompoundPowerFlow")

    class _Cast_PulleyCompoundPowerFlow:
        """Special nested class for casting PulleyCompoundPowerFlow to subclasses."""

        def __init__(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
            parent: "PulleyCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_power_flow(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "_4229.CouplingHalfCompoundPowerFlow":
            return self._parent._cast(_4229.CouplingHalfCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "_4267.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "_4215.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4215,
            )

            return self._parent._cast(_4215.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "_4269.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_power_flow(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "_4232.CVTPulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4232,
            )

            return self._parent._cast(_4232.CVTPulleyCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow",
        ) -> "PulleyCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PulleyCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4148.PulleyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PulleyPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4148.PulleyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PulleyPowerFlow]

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
    def cast_to(self: Self) -> "PulleyCompoundPowerFlow._Cast_PulleyCompoundPowerFlow":
        return self._Cast_PulleyCompoundPowerFlow(self)
