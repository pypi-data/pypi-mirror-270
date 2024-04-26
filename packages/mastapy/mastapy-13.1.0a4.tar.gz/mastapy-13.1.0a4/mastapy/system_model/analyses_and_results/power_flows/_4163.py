"""SpringDamperHalfPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4093
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "SpringDamperHalfPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2624
    from mastapy.system_model.analyses_and_results.static_loads import _6984
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4135,
        _4080,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfPowerFlow",)


Self = TypeVar("Self", bound="SpringDamperHalfPowerFlow")


class SpringDamperHalfPowerFlow(_4093.CouplingHalfPowerFlow):
    """SpringDamperHalfPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperHalfPowerFlow")

    class _Cast_SpringDamperHalfPowerFlow:
        """Special nested class for casting SpringDamperHalfPowerFlow to subclasses."""

        def __init__(
            self: "SpringDamperHalfPowerFlow._Cast_SpringDamperHalfPowerFlow",
            parent: "SpringDamperHalfPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_power_flow(
            self: "SpringDamperHalfPowerFlow._Cast_SpringDamperHalfPowerFlow",
        ) -> "_4093.CouplingHalfPowerFlow":
            return self._parent._cast(_4093.CouplingHalfPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "SpringDamperHalfPowerFlow._Cast_SpringDamperHalfPowerFlow",
        ) -> "_4135.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "SpringDamperHalfPowerFlow._Cast_SpringDamperHalfPowerFlow",
        ) -> "_4080.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "SpringDamperHalfPowerFlow._Cast_SpringDamperHalfPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperHalfPowerFlow._Cast_SpringDamperHalfPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperHalfPowerFlow._Cast_SpringDamperHalfPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperHalfPowerFlow._Cast_SpringDamperHalfPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperHalfPowerFlow._Cast_SpringDamperHalfPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfPowerFlow._Cast_SpringDamperHalfPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spring_damper_half_power_flow(
            self: "SpringDamperHalfPowerFlow._Cast_SpringDamperHalfPowerFlow",
        ) -> "SpringDamperHalfPowerFlow":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfPowerFlow._Cast_SpringDamperHalfPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperHalfPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2624.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6984.SpringDamperHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperHalfPowerFlow._Cast_SpringDamperHalfPowerFlow":
        return self._Cast_SpringDamperHalfPowerFlow(self)
