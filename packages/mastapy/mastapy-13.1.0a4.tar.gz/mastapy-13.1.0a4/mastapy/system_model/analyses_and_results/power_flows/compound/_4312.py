"""VirtualComponentCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4267
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "VirtualComponentCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4183
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4265,
        _4266,
        _4276,
        _4277,
        _4311,
        _4215,
        _4269,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundPowerFlow",)


Self = TypeVar("Self", bound="VirtualComponentCompoundPowerFlow")


class VirtualComponentCompoundPowerFlow(_4267.MountableComponentCompoundPowerFlow):
    """VirtualComponentCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentCompoundPowerFlow")

    class _Cast_VirtualComponentCompoundPowerFlow:
        """Special nested class for casting VirtualComponentCompoundPowerFlow to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
            parent: "VirtualComponentCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ) -> "_4267.MountableComponentCompoundPowerFlow":
            return self._parent._cast(_4267.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ) -> "_4215.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4215,
            )

            return self._parent._cast(_4215.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ) -> "_4269.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def mass_disc_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ) -> "_4265.MassDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ) -> "_4266.MeasurementComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4266,
            )

            return self._parent._cast(_4266.MeasurementComponentCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ) -> "_4276.PointLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4276,
            )

            return self._parent._cast(_4276.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ) -> "_4277.PowerLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4277,
            )

            return self._parent._cast(_4277.PowerLoadCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ) -> "_4311.UnbalancedMassCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4311,
            )

            return self._parent._cast(_4311.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ) -> "VirtualComponentCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "VirtualComponentCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4183.VirtualComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.VirtualComponentPowerFlow]

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
    ) -> "List[_4183.VirtualComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.VirtualComponentPowerFlow]

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
    ) -> "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow":
        return self._Cast_VirtualComponentCompoundPowerFlow(self)
