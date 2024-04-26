"""FEPartPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4056
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "FEPartPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.static_loads import _6914
    from mastapy.system_model.analyses_and_results.power_flows import _4080, _4137
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("FEPartPowerFlow",)


Self = TypeVar("Self", bound="FEPartPowerFlow")


class FEPartPowerFlow(_4056.AbstractShaftOrHousingPowerFlow):
    """FEPartPowerFlow

    This is a mastapy class.
    """

    TYPE = _FE_PART_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartPowerFlow")

    class _Cast_FEPartPowerFlow:
        """Special nested class for casting FEPartPowerFlow to subclasses."""

        def __init__(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow", parent: "FEPartPowerFlow"
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "_4056.AbstractShaftOrHousingPowerFlow":
            return self._parent._cast(_4056.AbstractShaftOrHousingPowerFlow)

        @property
        def component_power_flow(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "_4080.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def fe_part_power_flow(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "FEPartPowerFlow":
            return self._parent

        def __getattr__(self: "FEPartPowerFlow._Cast_FEPartPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fe_parts_are_not_used_in_power_flow(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEPartsAreNotUsedInPowerFlow

        if temp is None:
            return ""

        return temp

    @property
    def fe_parts_are_not_used_in_power_flow_select_component_replaced_by_this_fe(
        self: Self,
    ) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEPartsAreNotUsedInPowerFlowSelectComponentReplacedByThisFE

        if temp is None:
            return ""

        return temp

    @property
    def speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2471.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6914.FEPartLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "FEPartPowerFlow._Cast_FEPartPowerFlow":
        return self._Cast_FEPartPowerFlow(self)
