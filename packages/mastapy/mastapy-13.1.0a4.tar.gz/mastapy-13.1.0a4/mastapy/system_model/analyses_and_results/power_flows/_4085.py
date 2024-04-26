"""ConceptGearPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4117
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ConceptGearPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.gears.rating.concept import _558
    from mastapy.system_model.analyses_and_results.static_loads import _6868
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4135,
        _4080,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearPowerFlow",)


Self = TypeVar("Self", bound="ConceptGearPowerFlow")


class ConceptGearPowerFlow(_4117.GearPowerFlow):
    """ConceptGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearPowerFlow")

    class _Cast_ConceptGearPowerFlow:
        """Special nested class for casting ConceptGearPowerFlow to subclasses."""

        def __init__(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
            parent: "ConceptGearPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_power_flow(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_4117.GearPowerFlow":
            return self._parent._cast(_4117.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_4135.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_4080.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_gear_power_flow(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow",
        ) -> "ConceptGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2539.ConceptGear":
        """mastapy.system_model.part_model.gears.ConceptGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_558.ConceptGearRating":
        """mastapy.gears.rating.concept.ConceptGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6868.ConceptGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConceptGearPowerFlow._Cast_ConceptGearPowerFlow":
        return self._Cast_ConceptGearPowerFlow(self)
