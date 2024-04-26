"""GearSetPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4158
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "GearSetPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.gears.rating import _370
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4117,
        _4116,
        _4061,
        _4068,
        _4073,
        _4086,
        _4089,
        _4105,
        _4111,
        _4122,
        _4126,
        _4129,
        _4132,
        _4142,
        _4161,
        _4167,
        _4170,
        _4186,
        _4189,
        _4055,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearSetPowerFlow",)


Self = TypeVar("Self", bound="GearSetPowerFlow")


class GearSetPowerFlow(_4158.SpecialisedAssemblyPowerFlow):
    """GearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetPowerFlow")

    class _Cast_GearSetPowerFlow:
        """Special nested class for casting GearSetPowerFlow to subclasses."""

        def __init__(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow", parent: "GearSetPowerFlow"
        ):
            self._parent = parent

        @property
        def specialised_assembly_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4158.SpecialisedAssemblyPowerFlow":
            return self._parent._cast(_4158.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4055.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4061.AGMAGleasonConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4061

            return self._parent._cast(_4061.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4068.BevelDifferentialGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4073.BevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4073

            return self._parent._cast(_4073.BevelGearSetPowerFlow)

        @property
        def concept_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4086.ConceptGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4086

            return self._parent._cast(_4086.ConceptGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4089.ConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4089

            return self._parent._cast(_4089.ConicalGearSetPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4105.CylindricalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4105

            return self._parent._cast(_4105.CylindricalGearSetPowerFlow)

        @property
        def face_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4111.FaceGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.FaceGearSetPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4122.HypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4126.KlingelnbergCycloPalloidConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4126

            return self._parent._cast(
                _4126.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4129.KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(
                _4129.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4132.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(
                _4132.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def planetary_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4142.PlanetaryGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4142

            return self._parent._cast(_4142.PlanetaryGearSetPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4161.SpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.SpiralBevelGearSetPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4167.StraightBevelDiffGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4167

            return self._parent._cast(_4167.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4170.StraightBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4170

            return self._parent._cast(_4170.StraightBevelGearSetPowerFlow)

        @property
        def worm_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4186.WormGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4186

            return self._parent._cast(_4186.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "_4189.ZerolBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4189

            return self._parent._cast(_4189.ZerolBevelGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "GearSetPowerFlow._Cast_GearSetPowerFlow",
        ) -> "GearSetPowerFlow":
            return self._parent

        def __getattr__(self: "GearSetPowerFlow._Cast_GearSetPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2550.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_370.GearSetRating":
        """mastapy.gears.rating.GearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_power_flow(self: Self) -> "List[_4117.GearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearPowerFlow]

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
    def meshes_power_flow(self: Self) -> "List[_4116.GearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearMeshPowerFlow]

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

    def set_face_widths_for_specified_safety_factors(self: Self):
        """Method does not return."""
        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactors()

    @property
    def cast_to(self: Self) -> "GearSetPowerFlow._Cast_GearSetPowerFlow":
        return self._Cast_GearSetPowerFlow(self)
