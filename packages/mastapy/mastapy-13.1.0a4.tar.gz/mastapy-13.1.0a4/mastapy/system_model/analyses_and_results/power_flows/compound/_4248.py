"""GearCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4267
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "GearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _365
    from mastapy.system_model.analyses_and_results.power_flows import _4117
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4194,
        _4201,
        _4204,
        _4205,
        _4206,
        _4219,
        _4222,
        _4237,
        _4240,
        _4243,
        _4252,
        _4256,
        _4259,
        _4262,
        _4289,
        _4295,
        _4298,
        _4301,
        _4302,
        _4313,
        _4316,
        _4215,
        _4269,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundPowerFlow",)


Self = TypeVar("Self", bound="GearCompoundPowerFlow")


class GearCompoundPowerFlow(_4267.MountableComponentCompoundPowerFlow):
    """GearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCompoundPowerFlow")

    class _Cast_GearCompoundPowerFlow:
        """Special nested class for casting GearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
            parent: "GearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4267.MountableComponentCompoundPowerFlow":
            return self._parent._cast(_4267.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4215.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4215,
            )

            return self._parent._cast(_4215.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4269.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4194.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4201.BevelDifferentialGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4204.BevelDifferentialPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4204,
            )

            return self._parent._cast(
                _4204.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4205.BevelDifferentialSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4205,
            )

            return self._parent._cast(_4205.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4206.BevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.BevelGearCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4219.ConceptGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4219,
            )

            return self._parent._cast(_4219.ConceptGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4222.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4222,
            )

            return self._parent._cast(_4222.ConicalGearCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4237.CylindricalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4237,
            )

            return self._parent._cast(_4237.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4240.CylindricalPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4240,
            )

            return self._parent._cast(_4240.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4243.FaceGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.FaceGearCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4252.HypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.HypoidGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4256.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4256,
            )

            return self._parent._cast(
                _4256.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4259.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4259,
            )

            return self._parent._cast(
                _4259.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4262.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(
                _4262.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4289.SpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.SpiralBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4295.StraightBevelDiffGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4295,
            )

            return self._parent._cast(_4295.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4298.StraightBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4298,
            )

            return self._parent._cast(_4298.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4301.StraightBevelPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4301,
            )

            return self._parent._cast(_4301.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4302.StraightBevelSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4302,
            )

            return self._parent._cast(_4302.StraightBevelSunGearCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4313.WormGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4313,
            )

            return self._parent._cast(_4313.WormGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "_4316.ZerolBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4316,
            )

            return self._parent._cast(_4316.ZerolBevelGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow",
        ) -> "GearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_rating(self: Self) -> "_365.GearDutyCycleRating":
        """mastapy.gears.rating.GearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases(self: Self) -> "List[_4117.GearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4117.GearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "GearCompoundPowerFlow._Cast_GearCompoundPowerFlow":
        return self._Cast_GearCompoundPowerFlow(self)
