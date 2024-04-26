"""MountableComponentPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4080
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "MountableComponentPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2482
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4060,
        _4063,
        _4067,
        _4069,
        _4070,
        _4072,
        _4077,
        _4082,
        _4085,
        _4088,
        _4091,
        _4093,
        _4097,
        _4104,
        _4106,
        _4110,
        _4117,
        _4121,
        _4125,
        _4128,
        _4131,
        _4133,
        _4134,
        _4136,
        _4139,
        _4143,
        _4144,
        _4147,
        _4148,
        _4149,
        _4153,
        _4155,
        _4160,
        _4163,
        _4166,
        _4169,
        _4171,
        _4172,
        _4173,
        _4174,
        _4176,
        _4180,
        _4181,
        _4182,
        _4183,
        _4185,
        _4188,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentPowerFlow",)


Self = TypeVar("Self", bound="MountableComponentPowerFlow")


class MountableComponentPowerFlow(_4080.ComponentPowerFlow):
    """MountableComponentPowerFlow

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentPowerFlow")

    class _Cast_MountableComponentPowerFlow:
        """Special nested class for casting MountableComponentPowerFlow to subclasses."""

        def __init__(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
            parent: "MountableComponentPowerFlow",
        ):
            self._parent = parent

        @property
        def component_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4080.ComponentPowerFlow":
            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4060.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.AGMAGleasonConicalGearPowerFlow)

        @property
        def bearing_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4063.BearingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.BearingPowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4067.BevelDifferentialGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4069.BevelDifferentialPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4069

            return self._parent._cast(_4069.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4070.BevelDifferentialSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4072.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4072

            return self._parent._cast(_4072.BevelGearPowerFlow)

        @property
        def clutch_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4077.ClutchHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4077

            return self._parent._cast(_4077.ClutchHalfPowerFlow)

        @property
        def concept_coupling_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4082.ConceptCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4082

            return self._parent._cast(_4082.ConceptCouplingHalfPowerFlow)

        @property
        def concept_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4085.ConceptGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4085

            return self._parent._cast(_4085.ConceptGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4088.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.ConicalGearPowerFlow)

        @property
        def connector_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4091.ConnectorPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4093.CouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4093

            return self._parent._cast(_4093.CouplingHalfPowerFlow)

        @property
        def cvt_pulley_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4097.CVTPulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4097

            return self._parent._cast(_4097.CVTPulleyPowerFlow)

        @property
        def cylindrical_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4104.CylindricalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(_4104.CylindricalGearPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4106.CylindricalPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4106

            return self._parent._cast(_4106.CylindricalPlanetGearPowerFlow)

        @property
        def face_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4110.FaceGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.FaceGearPowerFlow)

        @property
        def gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4117.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(_4117.GearPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4121.HypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.HypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4125.KlingelnbergCycloPalloidConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4125

            return self._parent._cast(
                _4125.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4128.KlingelnbergCycloPalloidHypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4128

            return self._parent._cast(_4128.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4131.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(
                _4131.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def mass_disc_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4133.MassDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4134.MeasurementComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.MeasurementComponentPowerFlow)

        @property
        def oil_seal_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4136.OilSealPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4136

            return self._parent._cast(_4136.OilSealPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4139.PartToPartShearCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4139

            return self._parent._cast(_4139.PartToPartShearCouplingHalfPowerFlow)

        @property
        def planet_carrier_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4143.PlanetCarrierPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4144.PointLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4144

            return self._parent._cast(_4144.PointLoadPowerFlow)

        @property
        def power_load_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4147.PowerLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4147

            return self._parent._cast(_4147.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4148.PulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4148

            return self._parent._cast(_4148.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4149.RingPinsPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.RingPinsPowerFlow)

        @property
        def rolling_ring_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4153.RollingRingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4153

            return self._parent._cast(_4153.RollingRingPowerFlow)

        @property
        def shaft_hub_connection_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4155.ShaftHubConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4155

            return self._parent._cast(_4155.ShaftHubConnectionPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4160.SpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4160

            return self._parent._cast(_4160.SpiralBevelGearPowerFlow)

        @property
        def spring_damper_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4163.SpringDamperHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4163

            return self._parent._cast(_4163.SpringDamperHalfPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4166.StraightBevelDiffGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4166

            return self._parent._cast(_4166.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4169.StraightBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4169

            return self._parent._cast(_4169.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4171.StraightBevelPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4171

            return self._parent._cast(_4171.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4172.StraightBevelSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4172

            return self._parent._cast(_4172.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4173.SynchroniserHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4173

            return self._parent._cast(_4173.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4174.SynchroniserPartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4174

            return self._parent._cast(_4174.SynchroniserPartPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4176.SynchroniserSleevePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4176

            return self._parent._cast(_4176.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_pump_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4180.TorqueConverterPumpPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4180

            return self._parent._cast(_4180.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4181.TorqueConverterTurbinePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4181

            return self._parent._cast(_4181.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4182.UnbalancedMassPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4182

            return self._parent._cast(_4182.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4183.VirtualComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4183

            return self._parent._cast(_4183.VirtualComponentPowerFlow)

        @property
        def worm_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4185.WormGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4185

            return self._parent._cast(_4185.WormGearPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "_4188.ZerolBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4188

            return self._parent._cast(_4188.ZerolBevelGearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
        ) -> "MountableComponentPowerFlow":
            return self._parent

        def __getattr__(
            self: "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponentPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2482.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentPowerFlow._Cast_MountableComponentPowerFlow":
        return self._Cast_MountableComponentPowerFlow(self)
