"""PlanetCarrierPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4135
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "PlanetCarrierPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2487
    from mastapy.system_model.analyses_and_results.static_loads import _6962
    from mastapy.system_model.analyses_and_results.power_flows import _4080, _4137
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierPowerFlow",)


Self = TypeVar("Self", bound="PlanetCarrierPowerFlow")


class PlanetCarrierPowerFlow(_4135.MountableComponentPowerFlow):
    """PlanetCarrierPowerFlow

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetCarrierPowerFlow")

    class _Cast_PlanetCarrierPowerFlow:
        """Special nested class for casting PlanetCarrierPowerFlow to subclasses."""

        def __init__(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
            parent: "PlanetCarrierPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_power_flow(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "_4135.MountableComponentPowerFlow":
            return self._parent._cast(_4135.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "_4080.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planet_carrier_power_flow(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow",
        ) -> "PlanetCarrierPowerFlow":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetCarrierPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2487.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6962.PlanetCarrierLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PlanetCarrierPowerFlow._Cast_PlanetCarrierPowerFlow":
        return self._Cast_PlanetCarrierPowerFlow(self)
