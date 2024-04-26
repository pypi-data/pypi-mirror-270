"""CouplingHalfCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4267
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "CouplingHalfCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4093
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4213,
        _4218,
        _4232,
        _4272,
        _4278,
        _4282,
        _4294,
        _4304,
        _4305,
        _4306,
        _4309,
        _4310,
        _4215,
        _4269,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundPowerFlow",)


Self = TypeVar("Self", bound="CouplingHalfCompoundPowerFlow")


class CouplingHalfCompoundPowerFlow(_4267.MountableComponentCompoundPowerFlow):
    """CouplingHalfCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfCompoundPowerFlow")

    class _Cast_CouplingHalfCompoundPowerFlow:
        """Special nested class for casting CouplingHalfCompoundPowerFlow to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
            parent: "CouplingHalfCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4267.MountableComponentCompoundPowerFlow":
            return self._parent._cast(_4267.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4215.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4215,
            )

            return self._parent._cast(_4215.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4269.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4213.ClutchHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4213,
            )

            return self._parent._cast(_4213.ClutchHalfCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4218.ConceptCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4218,
            )

            return self._parent._cast(_4218.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4232.CVTPulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4232,
            )

            return self._parent._cast(_4232.CVTPulleyCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4272.PartToPartShearCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4272,
            )

            return self._parent._cast(
                _4272.PartToPartShearCouplingHalfCompoundPowerFlow
            )

        @property
        def pulley_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4278.PulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4278,
            )

            return self._parent._cast(_4278.PulleyCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4282.RollingRingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4282,
            )

            return self._parent._cast(_4282.RollingRingCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4294.SpringDamperHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4294,
            )

            return self._parent._cast(_4294.SpringDamperHalfCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4304.SynchroniserHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4304,
            )

            return self._parent._cast(_4304.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4305.SynchroniserPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4305,
            )

            return self._parent._cast(_4305.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4306.SynchroniserSleeveCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4306,
            )

            return self._parent._cast(_4306.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4309.TorqueConverterPumpCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4309,
            )

            return self._parent._cast(_4309.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "_4310.TorqueConverterTurbineCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4310,
            )

            return self._parent._cast(_4310.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "CouplingHalfCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4093.CouplingHalfPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CouplingHalfPowerFlow]

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
    ) -> "List[_4093.CouplingHalfPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CouplingHalfPowerFlow]

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
    ) -> "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow":
        return self._Cast_CouplingHalfCompoundPowerFlow(self)
