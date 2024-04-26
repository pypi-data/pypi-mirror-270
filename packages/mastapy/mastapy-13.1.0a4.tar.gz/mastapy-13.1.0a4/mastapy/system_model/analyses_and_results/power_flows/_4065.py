"""BeltDrivePowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4158
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "BeltDrivePowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.static_loads import _6848
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4096,
        _4055,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BeltDrivePowerFlow",)


Self = TypeVar("Self", bound="BeltDrivePowerFlow")


class BeltDrivePowerFlow(_4158.SpecialisedAssemblyPowerFlow):
    """BeltDrivePowerFlow

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltDrivePowerFlow")

    class _Cast_BeltDrivePowerFlow:
        """Special nested class for casting BeltDrivePowerFlow to subclasses."""

        def __init__(
            self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow",
            parent: "BeltDrivePowerFlow",
        ):
            self._parent = parent

        @property
        def specialised_assembly_power_flow(
            self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow",
        ) -> "_4158.SpecialisedAssemblyPowerFlow":
            return self._parent._cast(_4158.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow",
        ) -> "_4055.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_power_flow(
            self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow",
        ) -> "_4096.CVTPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.CVTPowerFlow)

        @property
        def belt_drive_power_flow(
            self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow",
        ) -> "BeltDrivePowerFlow":
            return self._parent

        def __getattr__(self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BeltDrivePowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2594.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6848.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow":
        return self._Cast_BeltDrivePowerFlow(self)
