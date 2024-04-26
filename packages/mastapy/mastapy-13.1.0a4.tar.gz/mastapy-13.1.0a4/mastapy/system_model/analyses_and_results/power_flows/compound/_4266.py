"""MeasurementComponentCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4312
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "MeasurementComponentCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2481
    from mastapy.system_model.analyses_and_results.power_flows import _4134
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4267,
        _4215,
        _4269,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentCompoundPowerFlow",)


Self = TypeVar("Self", bound="MeasurementComponentCompoundPowerFlow")


class MeasurementComponentCompoundPowerFlow(_4312.VirtualComponentCompoundPowerFlow):
    """MeasurementComponentCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentCompoundPowerFlow"
    )

    class _Cast_MeasurementComponentCompoundPowerFlow:
        """Special nested class for casting MeasurementComponentCompoundPowerFlow to subclasses."""

        def __init__(
            self: "MeasurementComponentCompoundPowerFlow._Cast_MeasurementComponentCompoundPowerFlow",
            parent: "MeasurementComponentCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_power_flow(
            self: "MeasurementComponentCompoundPowerFlow._Cast_MeasurementComponentCompoundPowerFlow",
        ) -> "_4312.VirtualComponentCompoundPowerFlow":
            return self._parent._cast(_4312.VirtualComponentCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "MeasurementComponentCompoundPowerFlow._Cast_MeasurementComponentCompoundPowerFlow",
        ) -> "_4267.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "MeasurementComponentCompoundPowerFlow._Cast_MeasurementComponentCompoundPowerFlow",
        ) -> "_4215.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4215,
            )

            return self._parent._cast(_4215.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "MeasurementComponentCompoundPowerFlow._Cast_MeasurementComponentCompoundPowerFlow",
        ) -> "_4269.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "MeasurementComponentCompoundPowerFlow._Cast_MeasurementComponentCompoundPowerFlow",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MeasurementComponentCompoundPowerFlow._Cast_MeasurementComponentCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentCompoundPowerFlow._Cast_MeasurementComponentCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def measurement_component_compound_power_flow(
            self: "MeasurementComponentCompoundPowerFlow._Cast_MeasurementComponentCompoundPowerFlow",
        ) -> "MeasurementComponentCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentCompoundPowerFlow._Cast_MeasurementComponentCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "MeasurementComponentCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2481.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4134.MeasurementComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.MeasurementComponentPowerFlow]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4134.MeasurementComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.MeasurementComponentPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "MeasurementComponentCompoundPowerFlow._Cast_MeasurementComponentCompoundPowerFlow":
        return self._Cast_MeasurementComponentCompoundPowerFlow(self)
