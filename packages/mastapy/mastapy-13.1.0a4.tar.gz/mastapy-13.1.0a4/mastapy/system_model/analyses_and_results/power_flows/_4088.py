"""ConicalGearPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4117
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ConicalGearPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4060,
        _4067,
        _4069,
        _4070,
        _4072,
        _4121,
        _4125,
        _4128,
        _4131,
        _4160,
        _4166,
        _4169,
        _4171,
        _4172,
        _4188,
        _4135,
        _4080,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearPowerFlow",)


Self = TypeVar("Self", bound="ConicalGearPowerFlow")


class ConicalGearPowerFlow(_4117.GearPowerFlow):
    """ConicalGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearPowerFlow")

    class _Cast_ConicalGearPowerFlow:
        """Special nested class for casting ConicalGearPowerFlow to subclasses."""

        def __init__(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
            parent: "ConicalGearPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4117.GearPowerFlow":
            return self._parent._cast(_4117.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4135.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4080.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4060.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.AGMAGleasonConicalGearPowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4067.BevelDifferentialGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4069.BevelDifferentialPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4069

            return self._parent._cast(_4069.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4070.BevelDifferentialSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4072.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4072

            return self._parent._cast(_4072.BevelGearPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4121.HypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.HypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4125.KlingelnbergCycloPalloidConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4125

            return self._parent._cast(
                _4125.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4128.KlingelnbergCycloPalloidHypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4128

            return self._parent._cast(_4128.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4131.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(
                _4131.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def spiral_bevel_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4160.SpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4160

            return self._parent._cast(_4160.SpiralBevelGearPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4166.StraightBevelDiffGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4166

            return self._parent._cast(_4166.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4169.StraightBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4169

            return self._parent._cast(_4169.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4171.StraightBevelPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4171

            return self._parent._cast(_4171.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4172.StraightBevelSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4172

            return self._parent._cast(_4172.StraightBevelSunGearPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "_4188.ZerolBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4188

            return self._parent._cast(_4188.ZerolBevelGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "ConicalGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2541.ConicalGear":
        """mastapy.system_model.part_model.gears.ConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow":
        return self._Cast_ConicalGearPowerFlow(self)
