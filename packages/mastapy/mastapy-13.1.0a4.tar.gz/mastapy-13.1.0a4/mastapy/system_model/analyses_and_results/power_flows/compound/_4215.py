"""ComponentCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4269
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ComponentCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4080
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4191,
        _4192,
        _4194,
        _4198,
        _4201,
        _4204,
        _4205,
        _4206,
        _4209,
        _4213,
        _4218,
        _4219,
        _4222,
        _4226,
        _4229,
        _4232,
        _4235,
        _4237,
        _4240,
        _4241,
        _4242,
        _4243,
        _4246,
        _4248,
        _4251,
        _4252,
        _4256,
        _4259,
        _4262,
        _4265,
        _4266,
        _4267,
        _4268,
        _4272,
        _4275,
        _4276,
        _4277,
        _4278,
        _4279,
        _4282,
        _4285,
        _4286,
        _4289,
        _4294,
        _4295,
        _4298,
        _4301,
        _4302,
        _4304,
        _4305,
        _4306,
        _4309,
        _4310,
        _4311,
        _4312,
        _4313,
        _4316,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundPowerFlow",)


Self = TypeVar("Self", bound="ComponentCompoundPowerFlow")


class ComponentCompoundPowerFlow(_4269.PartCompoundPowerFlow):
    """ComponentCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundPowerFlow")

    class _Cast_ComponentCompoundPowerFlow:
        """Special nested class for casting ComponentCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
            parent: "ComponentCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def part_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4269.PartCompoundPowerFlow":
            return self._parent._cast(_4269.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4191.AbstractShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4191,
            )

            return self._parent._cast(_4191.AbstractShaftCompoundPowerFlow)

        @property
        def abstract_shaft_or_housing_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4192.AbstractShaftOrHousingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.AbstractShaftOrHousingCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4194.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def bearing_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4198.BearingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.BearingCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4201.BevelDifferentialGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4204.BevelDifferentialPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4204,
            )

            return self._parent._cast(
                _4204.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4205.BevelDifferentialSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4205,
            )

            return self._parent._cast(_4205.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4206.BevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.BevelGearCompoundPowerFlow)

        @property
        def bolt_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4209.BoltCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4209,
            )

            return self._parent._cast(_4209.BoltCompoundPowerFlow)

        @property
        def clutch_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4213.ClutchHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4213,
            )

            return self._parent._cast(_4213.ClutchHalfCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4218.ConceptCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4218,
            )

            return self._parent._cast(_4218.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4219.ConceptGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4219,
            )

            return self._parent._cast(_4219.ConceptGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4222.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4222,
            )

            return self._parent._cast(_4222.ConicalGearCompoundPowerFlow)

        @property
        def connector_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4226.ConnectorCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4226,
            )

            return self._parent._cast(_4226.ConnectorCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4229.CouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4229,
            )

            return self._parent._cast(_4229.CouplingHalfCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4232.CVTPulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4232,
            )

            return self._parent._cast(_4232.CVTPulleyCompoundPowerFlow)

        @property
        def cycloidal_disc_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4235.CycloidalDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(_4235.CycloidalDiscCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4237.CylindricalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4237,
            )

            return self._parent._cast(_4237.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4240.CylindricalPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4240,
            )

            return self._parent._cast(_4240.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def datum_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4241.DatumCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(_4241.DatumCompoundPowerFlow)

        @property
        def external_cad_model_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4242.ExternalCADModelCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.ExternalCADModelCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4243.FaceGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.FaceGearCompoundPowerFlow)

        @property
        def fe_part_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4246.FEPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.FEPartCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4248.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.GearCompoundPowerFlow)

        @property
        def guide_dxf_model_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4251.GuideDxfModelCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4251,
            )

            return self._parent._cast(_4251.GuideDxfModelCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4252.HypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.HypoidGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4256.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4256,
            )

            return self._parent._cast(
                _4256.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4259.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4259,
            )

            return self._parent._cast(
                _4259.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4262.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(
                _4262.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def mass_disc_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4265.MassDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4266.MeasurementComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4266,
            )

            return self._parent._cast(_4266.MeasurementComponentCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4267.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.MountableComponentCompoundPowerFlow)

        @property
        def oil_seal_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4268.OilSealCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4268,
            )

            return self._parent._cast(_4268.OilSealCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4272.PartToPartShearCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4272,
            )

            return self._parent._cast(
                _4272.PartToPartShearCouplingHalfCompoundPowerFlow
            )

        @property
        def planet_carrier_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4275.PlanetCarrierCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4275,
            )

            return self._parent._cast(_4275.PlanetCarrierCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4276.PointLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4276,
            )

            return self._parent._cast(_4276.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4277.PowerLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4277,
            )

            return self._parent._cast(_4277.PowerLoadCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4278.PulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4278,
            )

            return self._parent._cast(_4278.PulleyCompoundPowerFlow)

        @property
        def ring_pins_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4279.RingPinsCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4279,
            )

            return self._parent._cast(_4279.RingPinsCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4282.RollingRingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4282,
            )

            return self._parent._cast(_4282.RollingRingCompoundPowerFlow)

        @property
        def shaft_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4285.ShaftCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4285,
            )

            return self._parent._cast(_4285.ShaftCompoundPowerFlow)

        @property
        def shaft_hub_connection_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4286.ShaftHubConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4286,
            )

            return self._parent._cast(_4286.ShaftHubConnectionCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4289.SpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.SpiralBevelGearCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4294.SpringDamperHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4294,
            )

            return self._parent._cast(_4294.SpringDamperHalfCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4295.StraightBevelDiffGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4295,
            )

            return self._parent._cast(_4295.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4298.StraightBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4298,
            )

            return self._parent._cast(_4298.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4301.StraightBevelPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4301,
            )

            return self._parent._cast(_4301.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4302.StraightBevelSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4302,
            )

            return self._parent._cast(_4302.StraightBevelSunGearCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4304.SynchroniserHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4304,
            )

            return self._parent._cast(_4304.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4305.SynchroniserPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4305,
            )

            return self._parent._cast(_4305.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4306.SynchroniserSleeveCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4306,
            )

            return self._parent._cast(_4306.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4309.TorqueConverterPumpCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4309,
            )

            return self._parent._cast(_4309.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4310.TorqueConverterTurbineCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4310,
            )

            return self._parent._cast(_4310.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4311.UnbalancedMassCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4311,
            )

            return self._parent._cast(_4311.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4312.VirtualComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4312,
            )

            return self._parent._cast(_4312.VirtualComponentCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4313.WormGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4313,
            )

            return self._parent._cast(_4313.WormGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "_4316.ZerolBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4316,
            )

            return self._parent._cast(_4316.ZerolBevelGearCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
        ) -> "ComponentCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4080.ComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ComponentPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4080.ComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ComponentPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentCompoundPowerFlow._Cast_ComponentCompoundPowerFlow":
        return self._Cast_ComponentCompoundPowerFlow(self)
