"""CylindricalGearSetPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4118
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "CylindricalGearSetPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.static_loads import _6892
    from mastapy.gears.rating.cylindrical import _471
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4104,
        _4103,
        _4142,
        _4158,
        _4055,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetPowerFlow",)


Self = TypeVar("Self", bound="CylindricalGearSetPowerFlow")


class CylindricalGearSetPowerFlow(_4118.GearSetPowerFlow):
    """CylindricalGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSetPowerFlow")

    class _Cast_CylindricalGearSetPowerFlow:
        """Special nested class for casting CylindricalGearSetPowerFlow to subclasses."""

        def __init__(
            self: "CylindricalGearSetPowerFlow._Cast_CylindricalGearSetPowerFlow",
            parent: "CylindricalGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_set_power_flow(
            self: "CylindricalGearSetPowerFlow._Cast_CylindricalGearSetPowerFlow",
        ) -> "_4118.GearSetPowerFlow":
            return self._parent._cast(_4118.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "CylindricalGearSetPowerFlow._Cast_CylindricalGearSetPowerFlow",
        ) -> "_4158.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "CylindricalGearSetPowerFlow._Cast_CylindricalGearSetPowerFlow",
        ) -> "_4055.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "CylindricalGearSetPowerFlow._Cast_CylindricalGearSetPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSetPowerFlow._Cast_CylindricalGearSetPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSetPowerFlow._Cast_CylindricalGearSetPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSetPowerFlow._Cast_CylindricalGearSetPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSetPowerFlow._Cast_CylindricalGearSetPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetPowerFlow._Cast_CylindricalGearSetPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planetary_gear_set_power_flow(
            self: "CylindricalGearSetPowerFlow._Cast_CylindricalGearSetPowerFlow",
        ) -> "_4142.PlanetaryGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4142

            return self._parent._cast(_4142.PlanetaryGearSetPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(
            self: "CylindricalGearSetPowerFlow._Cast_CylindricalGearSetPowerFlow",
        ) -> "CylindricalGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetPowerFlow._Cast_CylindricalGearSetPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2544.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6892.CylindricalGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_471.CylindricalGearSetRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_471.CylindricalGearSetRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_power_flow(self: Self) -> "List[_4104.CylindricalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CylindricalGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gears_power_flow(
        self: Self,
    ) -> "List[_4104.CylindricalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CylindricalGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_power_flow(self: Self) -> "List[_4103.CylindricalGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CylindricalGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_power_flow(
        self: Self,
    ) -> "List[_4103.CylindricalGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CylindricalGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def ratings_for_all_designs(self: Self) -> "List[_471.CylindricalGearSetRating]":
        """List[mastapy.gears.rating.cylindrical.CylindricalGearSetRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingsForAllDesigns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetPowerFlow._Cast_CylindricalGearSetPowerFlow":
        return self._Cast_CylindricalGearSetPowerFlow(self)
