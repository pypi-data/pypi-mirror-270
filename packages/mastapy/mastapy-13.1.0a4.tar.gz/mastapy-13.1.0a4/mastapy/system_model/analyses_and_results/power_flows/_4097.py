"""CVTPulleyPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4148
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "CVTPulleyPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4093,
        _4135,
        _4080,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyPowerFlow",)


Self = TypeVar("Self", bound="CVTPulleyPowerFlow")


class CVTPulleyPowerFlow(_4148.PulleyPowerFlow):
    """CVTPulleyPowerFlow

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyPowerFlow")

    class _Cast_CVTPulleyPowerFlow:
        """Special nested class for casting CVTPulleyPowerFlow to subclasses."""

        def __init__(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
            parent: "CVTPulleyPowerFlow",
        ):
            self._parent = parent

        @property
        def pulley_power_flow(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_4148.PulleyPowerFlow":
            return self._parent._cast(_4148.PulleyPowerFlow)

        @property
        def coupling_half_power_flow(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_4093.CouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4093

            return self._parent._cast(_4093.CouplingHalfPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_4135.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_4080.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_pulley_power_flow(
            self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow",
        ) -> "CVTPulleyPowerFlow":
            return self._parent

        def __getattr__(self: "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CVTPulleyPowerFlow._Cast_CVTPulleyPowerFlow":
        return self._Cast_CVTPulleyPowerFlow(self)
