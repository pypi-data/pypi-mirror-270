"""FlexiblePinAssemblyPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4158
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "FlexiblePinAssemblyPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.static_loads import _6915
    from mastapy.system_model.analyses_and_results.power_flows import _4055, _4137
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyPowerFlow",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyPowerFlow")


class FlexiblePinAssemblyPowerFlow(_4158.SpecialisedAssemblyPowerFlow):
    """FlexiblePinAssemblyPowerFlow

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FlexiblePinAssemblyPowerFlow")

    class _Cast_FlexiblePinAssemblyPowerFlow:
        """Special nested class for casting FlexiblePinAssemblyPowerFlow to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
            parent: "FlexiblePinAssemblyPowerFlow",
        ):
            self._parent = parent

        @property
        def specialised_assembly_power_flow(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "_4158.SpecialisedAssemblyPowerFlow":
            return self._parent._cast(_4158.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "_4055.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_power_flow(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
        ) -> "FlexiblePinAssemblyPowerFlow":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FlexiblePinAssemblyPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2472.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6915.FlexiblePinAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAssemblyPowerFlow._Cast_FlexiblePinAssemblyPowerFlow":
        return self._Cast_FlexiblePinAssemblyPowerFlow(self)
