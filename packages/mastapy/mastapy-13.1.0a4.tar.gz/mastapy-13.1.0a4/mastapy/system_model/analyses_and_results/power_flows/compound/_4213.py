"""ClutchHalfCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4229
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ClutchHalfCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.power_flows import _4077
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4267,
        _4215,
        _4269,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfCompoundPowerFlow",)


Self = TypeVar("Self", bound="ClutchHalfCompoundPowerFlow")


class ClutchHalfCompoundPowerFlow(_4229.CouplingHalfCompoundPowerFlow):
    """ClutchHalfCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchHalfCompoundPowerFlow")

    class _Cast_ClutchHalfCompoundPowerFlow:
        """Special nested class for casting ClutchHalfCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ClutchHalfCompoundPowerFlow._Cast_ClutchHalfCompoundPowerFlow",
            parent: "ClutchHalfCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_power_flow(
            self: "ClutchHalfCompoundPowerFlow._Cast_ClutchHalfCompoundPowerFlow",
        ) -> "_4229.CouplingHalfCompoundPowerFlow":
            return self._parent._cast(_4229.CouplingHalfCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "ClutchHalfCompoundPowerFlow._Cast_ClutchHalfCompoundPowerFlow",
        ) -> "_4267.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "ClutchHalfCompoundPowerFlow._Cast_ClutchHalfCompoundPowerFlow",
        ) -> "_4215.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4215,
            )

            return self._parent._cast(_4215.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "ClutchHalfCompoundPowerFlow._Cast_ClutchHalfCompoundPowerFlow",
        ) -> "_4269.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ClutchHalfCompoundPowerFlow._Cast_ClutchHalfCompoundPowerFlow",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchHalfCompoundPowerFlow._Cast_ClutchHalfCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfCompoundPowerFlow._Cast_ClutchHalfCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_compound_power_flow(
            self: "ClutchHalfCompoundPowerFlow._Cast_ClutchHalfCompoundPowerFlow",
        ) -> "ClutchHalfCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ClutchHalfCompoundPowerFlow._Cast_ClutchHalfCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchHalfCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2597.ClutchHalf":
        """mastapy.system_model.part_model.couplings.ClutchHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4077.ClutchHalfPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ClutchHalfPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4077.ClutchHalfPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ClutchHalfPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "ClutchHalfCompoundPowerFlow._Cast_ClutchHalfCompoundPowerFlow":
        return self._Cast_ClutchHalfCompoundPowerFlow(self)
