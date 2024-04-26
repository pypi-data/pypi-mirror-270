"""ZerolBevelGearCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4206
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ZerolBevelGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2571
    from mastapy.system_model.analyses_and_results.power_flows import _4188
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4194,
        _4222,
        _4248,
        _4267,
        _4215,
        _4269,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="ZerolBevelGearCompoundPowerFlow")


class ZerolBevelGearCompoundPowerFlow(_4206.BevelGearCompoundPowerFlow):
    """ZerolBevelGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearCompoundPowerFlow")

    class _Cast_ZerolBevelGearCompoundPowerFlow:
        """Special nested class for casting ZerolBevelGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ZerolBevelGearCompoundPowerFlow._Cast_ZerolBevelGearCompoundPowerFlow",
            parent: "ZerolBevelGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_power_flow(
            self: "ZerolBevelGearCompoundPowerFlow._Cast_ZerolBevelGearCompoundPowerFlow",
        ) -> "_4206.BevelGearCompoundPowerFlow":
            return self._parent._cast(_4206.BevelGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "ZerolBevelGearCompoundPowerFlow._Cast_ZerolBevelGearCompoundPowerFlow",
        ) -> "_4194.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "ZerolBevelGearCompoundPowerFlow._Cast_ZerolBevelGearCompoundPowerFlow",
        ) -> "_4222.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4222,
            )

            return self._parent._cast(_4222.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "ZerolBevelGearCompoundPowerFlow._Cast_ZerolBevelGearCompoundPowerFlow",
        ) -> "_4248.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "ZerolBevelGearCompoundPowerFlow._Cast_ZerolBevelGearCompoundPowerFlow",
        ) -> "_4267.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "ZerolBevelGearCompoundPowerFlow._Cast_ZerolBevelGearCompoundPowerFlow",
        ) -> "_4215.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4215,
            )

            return self._parent._cast(_4215.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "ZerolBevelGearCompoundPowerFlow._Cast_ZerolBevelGearCompoundPowerFlow",
        ) -> "_4269.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearCompoundPowerFlow._Cast_ZerolBevelGearCompoundPowerFlow",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearCompoundPowerFlow._Cast_ZerolBevelGearCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearCompoundPowerFlow._Cast_ZerolBevelGearCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "ZerolBevelGearCompoundPowerFlow._Cast_ZerolBevelGearCompoundPowerFlow",
        ) -> "ZerolBevelGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearCompoundPowerFlow._Cast_ZerolBevelGearCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2571.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4188.ZerolBevelGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ZerolBevelGearPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4188.ZerolBevelGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ZerolBevelGearPowerFlow]

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
    ) -> "ZerolBevelGearCompoundPowerFlow._Cast_ZerolBevelGearCompoundPowerFlow":
        return self._Cast_ZerolBevelGearCompoundPowerFlow(self)
