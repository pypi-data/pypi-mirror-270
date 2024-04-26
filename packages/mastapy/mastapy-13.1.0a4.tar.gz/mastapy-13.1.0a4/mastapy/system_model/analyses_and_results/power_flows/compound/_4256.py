"""KlingelnbergCycloPalloidConicalGearCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4222
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4125
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4259,
        _4262,
        _4248,
        _4267,
        _4215,
        _4269,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearCompoundPowerFlow")


class KlingelnbergCycloPalloidConicalGearCompoundPowerFlow(
    _4222.ConicalGearCompoundPowerFlow
):
    """KlingelnbergCycloPalloidConicalGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
            parent: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_4222.ConicalGearCompoundPowerFlow":
            return self._parent._cast(_4222.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_4248.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_4267.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_4215.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4215,
            )

            return self._parent._cast(_4215.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_4269.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_4259.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4259,
            )

            return self._parent._cast(
                _4259.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "_4262.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(
                _4262.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
        ) -> "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4125.KlingelnbergCycloPalloidConicalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearPowerFlow]

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
    ) -> "List[_4125.KlingelnbergCycloPalloidConicalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearPowerFlow]

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
    ) -> "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidConicalGearCompoundPowerFlow(self)
