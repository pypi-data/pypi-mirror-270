"""MassDiscCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4312
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "MassDiscCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2480
    from mastapy.system_model.analyses_and_results.power_flows import _4133
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4267,
        _4215,
        _4269,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscCompoundPowerFlow",)


Self = TypeVar("Self", bound="MassDiscCompoundPowerFlow")


class MassDiscCompoundPowerFlow(_4312.VirtualComponentCompoundPowerFlow):
    """MassDiscCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MassDiscCompoundPowerFlow")

    class _Cast_MassDiscCompoundPowerFlow:
        """Special nested class for casting MassDiscCompoundPowerFlow to subclasses."""

        def __init__(
            self: "MassDiscCompoundPowerFlow._Cast_MassDiscCompoundPowerFlow",
            parent: "MassDiscCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_power_flow(
            self: "MassDiscCompoundPowerFlow._Cast_MassDiscCompoundPowerFlow",
        ) -> "_4312.VirtualComponentCompoundPowerFlow":
            return self._parent._cast(_4312.VirtualComponentCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "MassDiscCompoundPowerFlow._Cast_MassDiscCompoundPowerFlow",
        ) -> "_4267.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "MassDiscCompoundPowerFlow._Cast_MassDiscCompoundPowerFlow",
        ) -> "_4215.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4215,
            )

            return self._parent._cast(_4215.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "MassDiscCompoundPowerFlow._Cast_MassDiscCompoundPowerFlow",
        ) -> "_4269.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "MassDiscCompoundPowerFlow._Cast_MassDiscCompoundPowerFlow",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MassDiscCompoundPowerFlow._Cast_MassDiscCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscCompoundPowerFlow._Cast_MassDiscCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def mass_disc_compound_power_flow(
            self: "MassDiscCompoundPowerFlow._Cast_MassDiscCompoundPowerFlow",
        ) -> "MassDiscCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "MassDiscCompoundPowerFlow._Cast_MassDiscCompoundPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MassDiscCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2480.MassDisc":
        """mastapy.system_model.part_model.MassDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4133.MassDiscPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.MassDiscPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4133.MassDiscPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.MassDiscPowerFlow]

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
    ) -> "MassDiscCompoundPowerFlow._Cast_MassDiscCompoundPowerFlow":
        return self._Cast_MassDiscCompoundPowerFlow(self)
