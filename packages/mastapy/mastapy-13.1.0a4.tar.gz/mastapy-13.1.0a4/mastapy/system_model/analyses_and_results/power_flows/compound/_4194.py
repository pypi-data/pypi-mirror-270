"""AGMAGleasonConicalGearCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4222
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "AGMAGleasonConicalGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4060
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4201,
        _4204,
        _4205,
        _4206,
        _4252,
        _4289,
        _4295,
        _4298,
        _4301,
        _4302,
        _4316,
        _4248,
        _4267,
        _4215,
        _4269,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundPowerFlow")


class AGMAGleasonConicalGearCompoundPowerFlow(_4222.ConicalGearCompoundPowerFlow):
    """AGMAGleasonConicalGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCompoundPowerFlow"
    )

    class _Cast_AGMAGleasonConicalGearCompoundPowerFlow:
        """Special nested class for casting AGMAGleasonConicalGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
            parent: "AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_4222.ConicalGearCompoundPowerFlow":
            return self._parent._cast(_4222.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_4248.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_4267.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_4215.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4215,
            )

            return self._parent._cast(_4215.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_4269.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_4201.BevelDifferentialGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_4204.BevelDifferentialPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4204,
            )

            return self._parent._cast(
                _4204.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_4205.BevelDifferentialSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4205,
            )

            return self._parent._cast(_4205.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_4206.BevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.BevelGearCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_4252.HypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.HypoidGearCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_4289.SpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.SpiralBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_4295.StraightBevelDiffGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4295,
            )

            return self._parent._cast(_4295.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_4298.StraightBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4298,
            )

            return self._parent._cast(_4298.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_4301.StraightBevelPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4301,
            )

            return self._parent._cast(_4301.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_4302.StraightBevelSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4302,
            )

            return self._parent._cast(_4302.StraightBevelSunGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "_4316.ZerolBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4316,
            )

            return self._parent._cast(_4316.ZerolBevelGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "AGMAGleasonConicalGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4060.AGMAGleasonConicalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearPowerFlow]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4060.AGMAGleasonConicalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow":
        return self._Cast_AGMAGleasonConicalGearCompoundPowerFlow(self)
