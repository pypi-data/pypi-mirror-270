"""AbstractShaftPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4056
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "AbstractShaftPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4101,
        _4156,
        _4080,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftPowerFlow",)


Self = TypeVar("Self", bound="AbstractShaftPowerFlow")


class AbstractShaftPowerFlow(_4056.AbstractShaftOrHousingPowerFlow):
    """AbstractShaftPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftPowerFlow")

    class _Cast_AbstractShaftPowerFlow:
        """Special nested class for casting AbstractShaftPowerFlow to subclasses."""

        def __init__(
            self: "AbstractShaftPowerFlow._Cast_AbstractShaftPowerFlow",
            parent: "AbstractShaftPowerFlow",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "AbstractShaftPowerFlow._Cast_AbstractShaftPowerFlow",
        ) -> "_4056.AbstractShaftOrHousingPowerFlow":
            return self._parent._cast(_4056.AbstractShaftOrHousingPowerFlow)

        @property
        def component_power_flow(
            self: "AbstractShaftPowerFlow._Cast_AbstractShaftPowerFlow",
        ) -> "_4080.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "AbstractShaftPowerFlow._Cast_AbstractShaftPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftPowerFlow._Cast_AbstractShaftPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftPowerFlow._Cast_AbstractShaftPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftPowerFlow._Cast_AbstractShaftPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftPowerFlow._Cast_AbstractShaftPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftPowerFlow._Cast_AbstractShaftPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_power_flow(
            self: "AbstractShaftPowerFlow._Cast_AbstractShaftPowerFlow",
        ) -> "_4101.CycloidalDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4101

            return self._parent._cast(_4101.CycloidalDiscPowerFlow)

        @property
        def shaft_power_flow(
            self: "AbstractShaftPowerFlow._Cast_AbstractShaftPowerFlow",
        ) -> "_4156.ShaftPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4156

            return self._parent._cast(_4156.ShaftPowerFlow)

        @property
        def abstract_shaft_power_flow(
            self: "AbstractShaftPowerFlow._Cast_AbstractShaftPowerFlow",
        ) -> "AbstractShaftPowerFlow":
            return self._parent

        def __getattr__(
            self: "AbstractShaftPowerFlow._Cast_AbstractShaftPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2453.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "AbstractShaftPowerFlow._Cast_AbstractShaftPowerFlow":
        return self._Cast_AbstractShaftPowerFlow(self)
