"""TorqueConverterPumpPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4093
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "TorqueConverterPumpPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2631
    from mastapy.system_model.analyses_and_results.static_loads import _7001
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4135,
        _4080,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpPowerFlow",)


Self = TypeVar("Self", bound="TorqueConverterPumpPowerFlow")


class TorqueConverterPumpPowerFlow(_4093.CouplingHalfPowerFlow):
    """TorqueConverterPumpPowerFlow

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterPumpPowerFlow")

    class _Cast_TorqueConverterPumpPowerFlow:
        """Special nested class for casting TorqueConverterPumpPowerFlow to subclasses."""

        def __init__(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
            parent: "TorqueConverterPumpPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_power_flow(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_4093.CouplingHalfPowerFlow":
            return self._parent._cast(_4093.CouplingHalfPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_4135.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_4080.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def torque_converter_pump_power_flow(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "TorqueConverterPumpPowerFlow":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterPumpPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2631.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_7001.TorqueConverterPumpLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase

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
    ) -> "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow":
        return self._Cast_TorqueConverterPumpPowerFlow(self)
