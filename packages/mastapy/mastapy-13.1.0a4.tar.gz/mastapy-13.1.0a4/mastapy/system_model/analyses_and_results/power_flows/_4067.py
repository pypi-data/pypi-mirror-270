"""BevelDifferentialGearPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4072
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "BevelDifferentialGearPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.gears.rating.bevel import _562
    from mastapy.system_model.analyses_and_results.static_loads import _6849
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4069,
        _4070,
        _4060,
        _4088,
        _4117,
        _4135,
        _4080,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearPowerFlow",)


Self = TypeVar("Self", bound="BevelDifferentialGearPowerFlow")


class BevelDifferentialGearPowerFlow(_4072.BevelGearPowerFlow):
    """BevelDifferentialGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialGearPowerFlow")

    class _Cast_BevelDifferentialGearPowerFlow:
        """Special nested class for casting BevelDifferentialGearPowerFlow to subclasses."""

        def __init__(
            self: "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow",
            parent: "BevelDifferentialGearPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_power_flow(
            self: "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow",
        ) -> "_4072.BevelGearPowerFlow":
            return self._parent._cast(_4072.BevelGearPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow",
        ) -> "_4060.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.AGMAGleasonConicalGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow",
        ) -> "_4088.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.ConicalGearPowerFlow)

        @property
        def gear_power_flow(
            self: "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow",
        ) -> "_4117.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(_4117.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow",
        ) -> "_4135.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow",
        ) -> "_4080.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow",
        ) -> "_4069.BevelDifferentialPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4069

            return self._parent._cast(_4069.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow",
        ) -> "_4070.BevelDifferentialSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow",
        ) -> "BevelDifferentialGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelDifferentialGearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_562.BevelGearRating":
        """mastapy.gears.rating.bevel.BevelGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6849.BevelDifferentialGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase

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
    ) -> "BevelDifferentialGearPowerFlow._Cast_BevelDifferentialGearPowerFlow":
        return self._Cast_BevelDifferentialGearPowerFlow(self)
