"""HypoidGearPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4060
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "HypoidGearPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2552
    from mastapy.gears.rating.hypoid import _446
    from mastapy.system_model.analyses_and_results.static_loads import _6932
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4088,
        _4117,
        _4135,
        _4080,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearPowerFlow",)


Self = TypeVar("Self", bound="HypoidGearPowerFlow")


class HypoidGearPowerFlow(_4060.AGMAGleasonConicalGearPowerFlow):
    """HypoidGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearPowerFlow")

    class _Cast_HypoidGearPowerFlow:
        """Special nested class for casting HypoidGearPowerFlow to subclasses."""

        def __init__(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
            parent: "HypoidGearPowerFlow",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ) -> "_4060.AGMAGleasonConicalGearPowerFlow":
            return self._parent._cast(_4060.AGMAGleasonConicalGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ) -> "_4088.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.ConicalGearPowerFlow)

        @property
        def gear_power_flow(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ) -> "_4117.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(_4117.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ) -> "_4135.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ) -> "_4080.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def hypoid_gear_power_flow(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ) -> "HypoidGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2552.HypoidGear":
        """mastapy.system_model.part_model.gears.HypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_446.HypoidGearRating":
        """mastapy.gears.rating.hypoid.HypoidGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6932.HypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow":
        return self._Cast_HypoidGearPowerFlow(self)
