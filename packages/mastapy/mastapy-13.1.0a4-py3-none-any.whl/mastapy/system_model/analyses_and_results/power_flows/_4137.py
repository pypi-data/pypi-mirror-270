"""PartPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7574
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "PartPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2486
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4145,
        _4055,
        _4056,
        _4057,
        _4060,
        _4061,
        _4062,
        _4063,
        _4065,
        _4067,
        _4068,
        _4069,
        _4070,
        _4072,
        _4073,
        _4074,
        _4075,
        _4077,
        _4078,
        _4080,
        _4082,
        _4083,
        _4085,
        _4086,
        _4088,
        _4089,
        _4091,
        _4093,
        _4094,
        _4096,
        _4097,
        _4098,
        _4101,
        _4104,
        _4105,
        _4106,
        _4107,
        _4108,
        _4110,
        _4111,
        _4114,
        _4115,
        _4117,
        _4118,
        _4119,
        _4121,
        _4122,
        _4125,
        _4126,
        _4128,
        _4129,
        _4131,
        _4132,
        _4133,
        _4134,
        _4135,
        _4136,
        _4139,
        _4140,
        _4142,
        _4143,
        _4144,
        _4147,
        _4148,
        _4149,
        _4151,
        _4153,
        _4154,
        _4155,
        _4156,
        _4158,
        _4160,
        _4161,
        _4163,
        _4164,
        _4166,
        _4167,
        _4169,
        _4170,
        _4171,
        _4172,
        _4173,
        _4174,
        _4175,
        _4176,
        _4179,
        _4180,
        _4181,
        _4182,
        _4183,
        _4185,
        _4186,
        _4188,
        _4189,
    )
    from mastapy.system_model.drawing import _2272
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartPowerFlow",)


Self = TypeVar("Self", bound="PartPowerFlow")


class PartPowerFlow(_7574.PartStaticLoadAnalysisCase):
    """PartPowerFlow

    This is a mastapy class.
    """

    TYPE = _PART_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartPowerFlow")

    class _Cast_PartPowerFlow:
        """Special nested class for casting PartPowerFlow to subclasses."""

        def __init__(
            self: "PartPowerFlow._Cast_PartPowerFlow", parent: "PartPowerFlow"
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4055.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.AbstractAssemblyPowerFlow)

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4056.AbstractShaftOrHousingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4056

            return self._parent._cast(_4056.AbstractShaftOrHousingPowerFlow)

        @property
        def abstract_shaft_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4057.AbstractShaftPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.AbstractShaftPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4060.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.AGMAGleasonConicalGearPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4061.AGMAGleasonConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4061

            return self._parent._cast(_4061.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4062.AssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.AssemblyPowerFlow)

        @property
        def bearing_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4063.BearingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.BearingPowerFlow)

        @property
        def belt_drive_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4065.BeltDrivePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4067.BevelDifferentialGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4068.BevelDifferentialGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4069.BevelDifferentialPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4069

            return self._parent._cast(_4069.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4070.BevelDifferentialSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4072.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4072

            return self._parent._cast(_4072.BevelGearPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4073.BevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4073

            return self._parent._cast(_4073.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4074.BoltedJointPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4074

            return self._parent._cast(_4074.BoltedJointPowerFlow)

        @property
        def bolt_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4075.BoltPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4075

            return self._parent._cast(_4075.BoltPowerFlow)

        @property
        def clutch_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4077.ClutchHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4077

            return self._parent._cast(_4077.ClutchHalfPowerFlow)

        @property
        def clutch_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4078.ClutchPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.ClutchPowerFlow)

        @property
        def component_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4080.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def concept_coupling_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4082.ConceptCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4082

            return self._parent._cast(_4082.ConceptCouplingHalfPowerFlow)

        @property
        def concept_coupling_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4083.ConceptCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4083

            return self._parent._cast(_4083.ConceptCouplingPowerFlow)

        @property
        def concept_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4085.ConceptGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4085

            return self._parent._cast(_4085.ConceptGearPowerFlow)

        @property
        def concept_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4086.ConceptGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4086

            return self._parent._cast(_4086.ConceptGearSetPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4088.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.ConicalGearPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4089.ConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4089

            return self._parent._cast(_4089.ConicalGearSetPowerFlow)

        @property
        def connector_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4091.ConnectorPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4093.CouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4093

            return self._parent._cast(_4093.CouplingHalfPowerFlow)

        @property
        def coupling_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4094.CouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.CouplingPowerFlow)

        @property
        def cvt_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4096.CVTPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.CVTPowerFlow)

        @property
        def cvt_pulley_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4097.CVTPulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4097

            return self._parent._cast(_4097.CVTPulleyPowerFlow)

        @property
        def cycloidal_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4098.CycloidalAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4098

            return self._parent._cast(_4098.CycloidalAssemblyPowerFlow)

        @property
        def cycloidal_disc_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4101.CycloidalDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4101

            return self._parent._cast(_4101.CycloidalDiscPowerFlow)

        @property
        def cylindrical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4104.CylindricalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(_4104.CylindricalGearPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4105.CylindricalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4105

            return self._parent._cast(_4105.CylindricalGearSetPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4106.CylindricalPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4106

            return self._parent._cast(_4106.CylindricalPlanetGearPowerFlow)

        @property
        def datum_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4107.DatumPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4107

            return self._parent._cast(_4107.DatumPowerFlow)

        @property
        def external_cad_model_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4108.ExternalCADModelPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(_4108.ExternalCADModelPowerFlow)

        @property
        def face_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4110.FaceGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.FaceGearPowerFlow)

        @property
        def face_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4111.FaceGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.FaceGearSetPowerFlow)

        @property
        def fe_part_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4114.FEPartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.FEPartPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4115.FlexiblePinAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4115

            return self._parent._cast(_4115.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4117.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(_4117.GearPowerFlow)

        @property
        def gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4118.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4118

            return self._parent._cast(_4118.GearSetPowerFlow)

        @property
        def guide_dxf_model_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4119.GuideDxfModelPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4119

            return self._parent._cast(_4119.GuideDxfModelPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4121.HypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.HypoidGearPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4122.HypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4125.KlingelnbergCycloPalloidConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4125

            return self._parent._cast(
                _4125.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4126.KlingelnbergCycloPalloidConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4126

            return self._parent._cast(
                _4126.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4128.KlingelnbergCycloPalloidHypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4128

            return self._parent._cast(_4128.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4129.KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(
                _4129.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4131.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(
                _4131.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4132.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(
                _4132.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def mass_disc_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4133.MassDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4134.MeasurementComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.MeasurementComponentPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4135.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.MountableComponentPowerFlow)

        @property
        def oil_seal_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4136.OilSealPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4136

            return self._parent._cast(_4136.OilSealPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4139.PartToPartShearCouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4139

            return self._parent._cast(_4139.PartToPartShearCouplingHalfPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4140.PartToPartShearCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4142.PlanetaryGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4142

            return self._parent._cast(_4142.PlanetaryGearSetPowerFlow)

        @property
        def planet_carrier_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4143.PlanetCarrierPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4144.PointLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4144

            return self._parent._cast(_4144.PointLoadPowerFlow)

        @property
        def power_load_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4147.PowerLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4147

            return self._parent._cast(_4147.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4148.PulleyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4148

            return self._parent._cast(_4148.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4149.RingPinsPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.RingPinsPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4151.RollingRingAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4151

            return self._parent._cast(_4151.RollingRingAssemblyPowerFlow)

        @property
        def rolling_ring_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4153.RollingRingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4153

            return self._parent._cast(_4153.RollingRingPowerFlow)

        @property
        def root_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4154.RootAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4154

            return self._parent._cast(_4154.RootAssemblyPowerFlow)

        @property
        def shaft_hub_connection_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4155.ShaftHubConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4155

            return self._parent._cast(_4155.ShaftHubConnectionPowerFlow)

        @property
        def shaft_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4156.ShaftPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4156

            return self._parent._cast(_4156.ShaftPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4158.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.SpecialisedAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4160.SpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4160

            return self._parent._cast(_4160.SpiralBevelGearPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4161.SpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4163.SpringDamperHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4163

            return self._parent._cast(_4163.SpringDamperHalfPowerFlow)

        @property
        def spring_damper_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4164.SpringDamperPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4164

            return self._parent._cast(_4164.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4166.StraightBevelDiffGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4166

            return self._parent._cast(_4166.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4167.StraightBevelDiffGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4167

            return self._parent._cast(_4167.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4169.StraightBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4169

            return self._parent._cast(_4169.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4170.StraightBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4170

            return self._parent._cast(_4170.StraightBevelGearSetPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4171.StraightBevelPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4171

            return self._parent._cast(_4171.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4172.StraightBevelSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4172

            return self._parent._cast(_4172.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4173.SynchroniserHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4173

            return self._parent._cast(_4173.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4174.SynchroniserPartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4174

            return self._parent._cast(_4174.SynchroniserPartPowerFlow)

        @property
        def synchroniser_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4175.SynchroniserPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4175

            return self._parent._cast(_4175.SynchroniserPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4176.SynchroniserSleevePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4176

            return self._parent._cast(_4176.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4179.TorqueConverterPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4179

            return self._parent._cast(_4179.TorqueConverterPowerFlow)

        @property
        def torque_converter_pump_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4180.TorqueConverterPumpPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4180

            return self._parent._cast(_4180.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4181.TorqueConverterTurbinePowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4181

            return self._parent._cast(_4181.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4182.UnbalancedMassPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4182

            return self._parent._cast(_4182.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4183.VirtualComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4183

            return self._parent._cast(_4183.VirtualComponentPowerFlow)

        @property
        def worm_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4185.WormGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4185

            return self._parent._cast(_4185.WormGearPowerFlow)

        @property
        def worm_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4186.WormGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4186

            return self._parent._cast(_4186.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4188.ZerolBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4188

            return self._parent._cast(_4188.ZerolBevelGearPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "_4189.ZerolBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4189

            return self._parent._cast(_4189.ZerolBevelGearSetPowerFlow)

        @property
        def part_power_flow(
            self: "PartPowerFlow._Cast_PartPowerFlow",
        ) -> "PartPowerFlow":
            return self._parent

        def __getattr__(self: "PartPowerFlow._Cast_PartPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing_showing_power_flow(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingShowingPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def component_design(self: Self) -> "_2486.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow(self: Self) -> "_4145.PowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlow

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2272.PowerFlowViewable":
        """mastapy.system_model.drawing.PowerFlowViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartPowerFlow._Cast_PartPowerFlow":
        return self._Cast_PartPowerFlow(self)
