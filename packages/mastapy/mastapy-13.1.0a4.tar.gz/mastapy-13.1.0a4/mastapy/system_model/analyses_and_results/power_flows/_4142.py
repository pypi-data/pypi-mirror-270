"""PlanetaryGearSetPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4105
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "PlanetaryGearSetPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2560
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4118,
        _4158,
        _4055,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetPowerFlow",)


Self = TypeVar("Self", bound="PlanetaryGearSetPowerFlow")


class PlanetaryGearSetPowerFlow(_4105.CylindricalGearSetPowerFlow):
    """PlanetaryGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSetPowerFlow")

    class _Cast_PlanetaryGearSetPowerFlow:
        """Special nested class for casting PlanetaryGearSetPowerFlow to subclasses."""

        def __init__(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
            parent: "PlanetaryGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_4105.CylindricalGearSetPowerFlow":
            return self._parent._cast(_4105.CylindricalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_4118.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4118

            return self._parent._cast(_4118.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_4158.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_4055.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planetary_gear_set_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "PlanetaryGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetaryGearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2560.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow":
        return self._Cast_PlanetaryGearSetPowerFlow(self)
