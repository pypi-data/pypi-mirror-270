"""ConicalGearSetCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4250
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ConicalGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.conical import _548
    from mastapy.system_model.analyses_and_results.power_flows import _4089
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4196,
        _4203,
        _4208,
        _4254,
        _4258,
        _4261,
        _4264,
        _4291,
        _4297,
        _4300,
        _4318,
        _4288,
        _4190,
        _4269,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="ConicalGearSetCompoundPowerFlow")


class ConicalGearSetCompoundPowerFlow(_4250.GearSetCompoundPowerFlow):
    """ConicalGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetCompoundPowerFlow")

    class _Cast_ConicalGearSetCompoundPowerFlow:
        """Special nested class for casting ConicalGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
            parent: "ConicalGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_4250.GearSetCompoundPowerFlow":
            return self._parent._cast(_4250.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_4288.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_4190.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4190,
            )

            return self._parent._cast(_4190.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_4269.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_4196.AGMAGleasonConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4196,
            )

            return self._parent._cast(_4196.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_4203.BevelDifferentialGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4203,
            )

            return self._parent._cast(_4203.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_4208.BevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4208,
            )

            return self._parent._cast(_4208.BevelGearSetCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_4254.HypoidGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.HypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_4258.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4258,
            )

            return self._parent._cast(
                _4258.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_4261.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4261,
            )

            return self._parent._cast(
                _4261.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_4264.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4264,
            )

            return self._parent._cast(
                _4264.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
            )

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_4291.SpiralBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4291,
            )

            return self._parent._cast(_4291.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_4297.StraightBevelDiffGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4297,
            )

            return self._parent._cast(_4297.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_4300.StraightBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4300,
            )

            return self._parent._cast(_4300.StraightBevelGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "_4318.ZerolBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4318,
            )

            return self._parent._cast(_4318.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "ConicalGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set_duty_cycle_rating(self: Self) -> "_548.ConicalGearSetDutyCycleRating":
        """mastapy.gears.rating.conical.ConicalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_set_duty_cycle_rating(
        self: Self,
    ) -> "_548.ConicalGearSetDutyCycleRating":
        """mastapy.gears.rating.conical.ConicalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4089.ConicalGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConicalGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4089.ConicalGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConicalGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow":
        return self._Cast_ConicalGearSetCompoundPowerFlow(self)
