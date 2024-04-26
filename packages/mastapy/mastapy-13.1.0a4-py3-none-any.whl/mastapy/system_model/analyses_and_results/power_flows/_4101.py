"""CycloidalDiscPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4057
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "CycloidalDiscPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2587
    from mastapy.system_model.analyses_and_results.static_loads import _6886
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4056,
        _4080,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPowerFlow",)


Self = TypeVar("Self", bound="CycloidalDiscPowerFlow")


class CycloidalDiscPowerFlow(_4057.AbstractShaftPowerFlow):
    """CycloidalDiscPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscPowerFlow")

    class _Cast_CycloidalDiscPowerFlow:
        """Special nested class for casting CycloidalDiscPowerFlow to subclasses."""

        def __init__(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
            parent: "CycloidalDiscPowerFlow",
        ):
            self._parent = parent

        @property
        def abstract_shaft_power_flow(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ) -> "_4057.AbstractShaftPowerFlow":
            return self._parent._cast(_4057.AbstractShaftPowerFlow)

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ) -> "_4056.AbstractShaftOrHousingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4056

            return self._parent._cast(_4056.AbstractShaftOrHousingPowerFlow)

        @property
        def component_power_flow(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ) -> "_4080.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_power_flow(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ) -> "CycloidalDiscPowerFlow":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2587.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6886.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow":
        return self._Cast_CycloidalDiscPowerFlow(self)
