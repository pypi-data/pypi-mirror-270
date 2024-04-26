"""KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4126
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4261,
        _4264,
        _4250,
        _4288,
        _4190,
        _4269,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow")


class KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow(
    _4224.ConicalGearSetCompoundPowerFlow
):
    """KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
            parent: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ) -> "_4224.ConicalGearSetCompoundPowerFlow":
            return self._parent._cast(_4224.ConicalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ) -> "_4250.GearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4250,
            )

            return self._parent._cast(_4250.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ) -> "_4288.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ) -> "_4190.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4190,
            )

            return self._parent._cast(_4190.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ) -> "_4269.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ) -> "_4261.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4261,
            )

            return self._parent._cast(
                _4261.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ) -> "_4264.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4264,
            )

            return self._parent._cast(
                _4264.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4126.KlingelnbergCycloPalloidConicalGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearSetPowerFlow]

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
    ) -> "List[_4126.KlingelnbergCycloPalloidConicalGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearSetPowerFlow]

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
    ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow(self)
