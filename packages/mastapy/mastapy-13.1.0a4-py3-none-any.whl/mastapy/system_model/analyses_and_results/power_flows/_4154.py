"""RootAssemblyPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4062
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "RootAssemblyPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2492
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4145,
        _4055,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyPowerFlow",)


Self = TypeVar("Self", bound="RootAssemblyPowerFlow")


class RootAssemblyPowerFlow(_4062.AssemblyPowerFlow):
    """RootAssemblyPowerFlow

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RootAssemblyPowerFlow")

    class _Cast_RootAssemblyPowerFlow:
        """Special nested class for casting RootAssemblyPowerFlow to subclasses."""

        def __init__(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
            parent: "RootAssemblyPowerFlow",
        ):
            self._parent = parent

        @property
        def assembly_power_flow(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "_4062.AssemblyPowerFlow":
            return self._parent._cast(_4062.AssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "_4055.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def root_assembly_power_flow(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "RootAssemblyPowerFlow":
            return self._parent

        def __getattr__(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RootAssemblyPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2492.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_inputs(self: Self) -> "_4145.PowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow":
        return self._Cast_RootAssemblyPowerFlow(self)
