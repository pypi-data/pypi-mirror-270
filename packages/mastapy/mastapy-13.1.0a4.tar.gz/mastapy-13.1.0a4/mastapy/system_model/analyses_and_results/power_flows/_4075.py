"""BoltPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4080
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "BoltPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.static_loads import _6858
    from mastapy.system_model.analyses_and_results.power_flows import _4137
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BoltPowerFlow",)


Self = TypeVar("Self", bound="BoltPowerFlow")


class BoltPowerFlow(_4080.ComponentPowerFlow):
    """BoltPowerFlow

    This is a mastapy class.
    """

    TYPE = _BOLT_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltPowerFlow")

    class _Cast_BoltPowerFlow:
        """Special nested class for casting BoltPowerFlow to subclasses."""

        def __init__(
            self: "BoltPowerFlow._Cast_BoltPowerFlow", parent: "BoltPowerFlow"
        ):
            self._parent = parent

        @property
        def component_power_flow(
            self: "BoltPowerFlow._Cast_BoltPowerFlow",
        ) -> "_4080.ComponentPowerFlow":
            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "BoltPowerFlow._Cast_BoltPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "BoltPowerFlow._Cast_BoltPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltPowerFlow._Cast_BoltPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltPowerFlow._Cast_BoltPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltPowerFlow._Cast_BoltPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltPowerFlow._Cast_BoltPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bolt_power_flow(
            self: "BoltPowerFlow._Cast_BoltPowerFlow",
        ) -> "BoltPowerFlow":
            return self._parent

        def __getattr__(self: "BoltPowerFlow._Cast_BoltPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2460.Bolt":
        """mastapy.system_model.part_model.Bolt

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6858.BoltLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BoltPowerFlow._Cast_BoltPowerFlow":
        return self._Cast_BoltPowerFlow(self)
