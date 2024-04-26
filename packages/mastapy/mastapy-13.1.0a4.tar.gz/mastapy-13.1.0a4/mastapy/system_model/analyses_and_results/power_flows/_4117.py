"""GearPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4135
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "GearPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4060,
        _4067,
        _4069,
        _4070,
        _4072,
        _4085,
        _4088,
        _4104,
        _4106,
        _4110,
        _4121,
        _4125,
        _4128,
        _4131,
        _4160,
        _4166,
        _4169,
        _4171,
        _4172,
        _4185,
        _4188,
        _4080,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearPowerFlow",)


Self = TypeVar("Self", bound="GearPowerFlow")


class GearPowerFlow(_4135.MountableComponentPowerFlow):
    """GearPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearPowerFlow")

    class _Cast_GearPowerFlow:
        """Special nested class for casting GearPowerFlow to subclasses."""

        def __init__(
            self: "GearPowerFlow._Cast_GearPowerFlow", parent: "GearPowerFlow"
        ):
            self._parent = parent

        @property
        def mountable_component_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4135.MountableComponentPowerFlow":
            return self._parent._cast(_4135.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4080.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4060.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.AGMAGleasonConicalGearPowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4067.BevelDifferentialGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4069.BevelDifferentialPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4069

            return self._parent._cast(_4069.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4070.BevelDifferentialSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4072.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4072

            return self._parent._cast(_4072.BevelGearPowerFlow)

        @property
        def concept_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4085.ConceptGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4085

            return self._parent._cast(_4085.ConceptGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4088.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.ConicalGearPowerFlow)

        @property
        def cylindrical_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4104.CylindricalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(_4104.CylindricalGearPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4106.CylindricalPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4106

            return self._parent._cast(_4106.CylindricalPlanetGearPowerFlow)

        @property
        def face_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4110.FaceGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.FaceGearPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4121.HypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.HypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4125.KlingelnbergCycloPalloidConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4125

            return self._parent._cast(
                _4125.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4128.KlingelnbergCycloPalloidHypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4128

            return self._parent._cast(_4128.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4131.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(
                _4131.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def spiral_bevel_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4160.SpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4160

            return self._parent._cast(_4160.SpiralBevelGearPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4166.StraightBevelDiffGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4166

            return self._parent._cast(_4166.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4169.StraightBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4169

            return self._parent._cast(_4169.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4171.StraightBevelPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4171

            return self._parent._cast(_4171.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4172.StraightBevelSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4172

            return self._parent._cast(_4172.StraightBevelSunGearPowerFlow)

        @property
        def worm_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4185.WormGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4185

            return self._parent._cast(_4185.WormGearPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "_4188.ZerolBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4188

            return self._parent._cast(_4188.ZerolBevelGearPowerFlow)

        @property
        def gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "GearPowerFlow":
            return self._parent

        def __getattr__(self: "GearPowerFlow._Cast_GearPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_loaded(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLoaded

        if temp is None:
            return False

        return temp

    @property
    def component_design(self: Self) -> "_2548.Gear":
        """mastapy.system_model.part_model.gears.Gear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearPowerFlow._Cast_GearPowerFlow":
        return self._Cast_GearPowerFlow(self)
