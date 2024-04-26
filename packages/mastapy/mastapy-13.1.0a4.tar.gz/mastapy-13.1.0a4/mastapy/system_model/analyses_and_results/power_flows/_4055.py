"""AbstractAssemblyPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4137
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "AbstractAssemblyPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4061,
        _4062,
        _4065,
        _4068,
        _4073,
        _4074,
        _4078,
        _4083,
        _4086,
        _4089,
        _4094,
        _4096,
        _4098,
        _4105,
        _4111,
        _4115,
        _4118,
        _4122,
        _4126,
        _4129,
        _4132,
        _4140,
        _4142,
        _4151,
        _4154,
        _4158,
        _4161,
        _4164,
        _4167,
        _4170,
        _4175,
        _4179,
        _4186,
        _4189,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyPowerFlow",)


Self = TypeVar("Self", bound="AbstractAssemblyPowerFlow")


class AbstractAssemblyPowerFlow(_4137.PartPowerFlow):
    """AbstractAssemblyPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyPowerFlow")

    class _Cast_AbstractAssemblyPowerFlow:
        """Special nested class for casting AbstractAssemblyPowerFlow to subclasses."""

        def __init__(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
            parent: "AbstractAssemblyPowerFlow",
        ):
            self._parent = parent

        @property
        def part_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4137.PartPowerFlow":
            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4061.AGMAGleasonConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4061

            return self._parent._cast(_4061.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4062.AssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.AssemblyPowerFlow)

        @property
        def belt_drive_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4065.BeltDrivePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4068.BevelDifferentialGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4073.BevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4073

            return self._parent._cast(_4073.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4074.BoltedJointPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4074

            return self._parent._cast(_4074.BoltedJointPowerFlow)

        @property
        def clutch_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4078.ClutchPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.ClutchPowerFlow)

        @property
        def concept_coupling_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4083.ConceptCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4083

            return self._parent._cast(_4083.ConceptCouplingPowerFlow)

        @property
        def concept_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4086.ConceptGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4086

            return self._parent._cast(_4086.ConceptGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4089.ConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4089

            return self._parent._cast(_4089.ConicalGearSetPowerFlow)

        @property
        def coupling_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4094.CouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.CouplingPowerFlow)

        @property
        def cvt_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4096.CVTPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.CVTPowerFlow)

        @property
        def cycloidal_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4098.CycloidalAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4098

            return self._parent._cast(_4098.CycloidalAssemblyPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4105.CylindricalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4105

            return self._parent._cast(_4105.CylindricalGearSetPowerFlow)

        @property
        def face_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4111.FaceGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.FaceGearSetPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4115.FlexiblePinAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4115

            return self._parent._cast(_4115.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4118.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4118

            return self._parent._cast(_4118.GearSetPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4122.HypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4126.KlingelnbergCycloPalloidConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4126

            return self._parent._cast(
                _4126.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4129.KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(
                _4129.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4132.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(
                _4132.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def part_to_part_shear_coupling_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4140.PartToPartShearCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4142.PlanetaryGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4142

            return self._parent._cast(_4142.PlanetaryGearSetPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4151.RollingRingAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4151

            return self._parent._cast(_4151.RollingRingAssemblyPowerFlow)

        @property
        def root_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4154.RootAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4154

            return self._parent._cast(_4154.RootAssemblyPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4158.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.SpecialisedAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4161.SpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4164.SpringDamperPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4164

            return self._parent._cast(_4164.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4167.StraightBevelDiffGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4167

            return self._parent._cast(_4167.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4170.StraightBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4170

            return self._parent._cast(_4170.StraightBevelGearSetPowerFlow)

        @property
        def synchroniser_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4175.SynchroniserPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4175

            return self._parent._cast(_4175.SynchroniserPowerFlow)

        @property
        def torque_converter_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4179.TorqueConverterPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4179

            return self._parent._cast(_4179.TorqueConverterPowerFlow)

        @property
        def worm_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4186.WormGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4186

            return self._parent._cast(_4186.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "_4189.ZerolBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4189

            return self._parent._cast(_4189.ZerolBevelGearSetPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "AbstractAssemblyPowerFlow":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssemblyPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2452.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2452.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

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
    ) -> "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow":
        return self._Cast_AbstractAssemblyPowerFlow(self)
