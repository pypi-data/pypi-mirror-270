"""CVTPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4065
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "CVTPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4158,
        _4055,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CVTPowerFlow",)


Self = TypeVar("Self", bound="CVTPowerFlow")


class CVTPowerFlow(_4065.BeltDrivePowerFlow):
    """CVTPowerFlow

    This is a mastapy class.
    """

    TYPE = _CVT_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPowerFlow")

    class _Cast_CVTPowerFlow:
        """Special nested class for casting CVTPowerFlow to subclasses."""

        def __init__(self: "CVTPowerFlow._Cast_CVTPowerFlow", parent: "CVTPowerFlow"):
            self._parent = parent

        @property
        def belt_drive_power_flow(
            self: "CVTPowerFlow._Cast_CVTPowerFlow",
        ) -> "_4065.BeltDrivePowerFlow":
            return self._parent._cast(_4065.BeltDrivePowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "CVTPowerFlow._Cast_CVTPowerFlow",
        ) -> "_4158.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "CVTPowerFlow._Cast_CVTPowerFlow",
        ) -> "_4055.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "CVTPowerFlow._Cast_CVTPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "CVTPowerFlow._Cast_CVTPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPowerFlow._Cast_CVTPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPowerFlow._Cast_CVTPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPowerFlow._Cast_CVTPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPowerFlow._Cast_CVTPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_power_flow(self: "CVTPowerFlow._Cast_CVTPowerFlow") -> "CVTPowerFlow":
            return self._parent

        def __getattr__(self: "CVTPowerFlow._Cast_CVTPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2605.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CVTPowerFlow._Cast_CVTPowerFlow":
        return self._Cast_CVTPowerFlow(self)
