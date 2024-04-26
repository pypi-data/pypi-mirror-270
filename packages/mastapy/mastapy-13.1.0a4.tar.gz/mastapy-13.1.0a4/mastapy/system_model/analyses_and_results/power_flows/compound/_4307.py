"""TorqueConverterCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4227
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "TorqueConverterCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2630
    from mastapy.system_model.analyses_and_results.power_flows import _4179
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4288,
        _4190,
        _4269,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterCompoundPowerFlow",)


Self = TypeVar("Self", bound="TorqueConverterCompoundPowerFlow")


class TorqueConverterCompoundPowerFlow(_4227.CouplingCompoundPowerFlow):
    """TorqueConverterCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterCompoundPowerFlow")

    class _Cast_TorqueConverterCompoundPowerFlow:
        """Special nested class for casting TorqueConverterCompoundPowerFlow to subclasses."""

        def __init__(
            self: "TorqueConverterCompoundPowerFlow._Cast_TorqueConverterCompoundPowerFlow",
            parent: "TorqueConverterCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_compound_power_flow(
            self: "TorqueConverterCompoundPowerFlow._Cast_TorqueConverterCompoundPowerFlow",
        ) -> "_4227.CouplingCompoundPowerFlow":
            return self._parent._cast(_4227.CouplingCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "TorqueConverterCompoundPowerFlow._Cast_TorqueConverterCompoundPowerFlow",
        ) -> "_4288.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "TorqueConverterCompoundPowerFlow._Cast_TorqueConverterCompoundPowerFlow",
        ) -> "_4190.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4190,
            )

            return self._parent._cast(_4190.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "TorqueConverterCompoundPowerFlow._Cast_TorqueConverterCompoundPowerFlow",
        ) -> "_4269.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "TorqueConverterCompoundPowerFlow._Cast_TorqueConverterCompoundPowerFlow",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterCompoundPowerFlow._Cast_TorqueConverterCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterCompoundPowerFlow._Cast_TorqueConverterCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def torque_converter_compound_power_flow(
            self: "TorqueConverterCompoundPowerFlow._Cast_TorqueConverterCompoundPowerFlow",
        ) -> "TorqueConverterCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "TorqueConverterCompoundPowerFlow._Cast_TorqueConverterCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2630.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2630.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4179.TorqueConverterPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.TorqueConverterPowerFlow]

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
    def assembly_analysis_cases(self: Self) -> "List[_4179.TorqueConverterPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.TorqueConverterPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "TorqueConverterCompoundPowerFlow._Cast_TorqueConverterCompoundPowerFlow":
        return self._Cast_TorqueConverterCompoundPowerFlow(self)
