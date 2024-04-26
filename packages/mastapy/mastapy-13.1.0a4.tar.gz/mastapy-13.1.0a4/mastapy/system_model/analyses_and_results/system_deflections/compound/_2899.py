"""ComponentCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2954
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ComponentCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2738
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2875,
        _2876,
        _2878,
        _2882,
        _2885,
        _2888,
        _2889,
        _2890,
        _2893,
        _2897,
        _2902,
        _2903,
        _2906,
        _2910,
        _2913,
        _2916,
        _2919,
        _2921,
        _2924,
        _2925,
        _2927,
        _2928,
        _2931,
        _2933,
        _2936,
        _2937,
        _2941,
        _2944,
        _2947,
        _2950,
        _2951,
        _2952,
        _2953,
        _2957,
        _2960,
        _2961,
        _2962,
        _2963,
        _2964,
        _2967,
        _2970,
        _2972,
        _2975,
        _2980,
        _2981,
        _2984,
        _2987,
        _2988,
        _2990,
        _2991,
        _2992,
        _2995,
        _2996,
        _2997,
        _2998,
        _2999,
        _3002,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ComponentCompoundSystemDeflection")


class ComponentCompoundSystemDeflection(_2954.PartCompoundSystemDeflection):
    """ComponentCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundSystemDeflection")

    class _Cast_ComponentCompoundSystemDeflection:
        """Special nested class for casting ComponentCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
            parent: "ComponentCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2954.PartCompoundSystemDeflection":
            return self._parent._cast(_2954.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2875.AbstractShaftCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2875,
            )

            return self._parent._cast(_2875.AbstractShaftCompoundSystemDeflection)

        @property
        def abstract_shaft_or_housing_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2876.AbstractShaftOrHousingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2876,
            )

            return self._parent._cast(
                _2876.AbstractShaftOrHousingCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2878.AGMAGleasonConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2878,
            )

            return self._parent._cast(
                _2878.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def bearing_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2882.BearingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2882,
            )

            return self._parent._cast(_2882.BearingCompoundSystemDeflection)

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2885.BevelDifferentialGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2885,
            )

            return self._parent._cast(
                _2885.BevelDifferentialGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2888.BevelDifferentialPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2888,
            )

            return self._parent._cast(
                _2888.BevelDifferentialPlanetGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2889.BevelDifferentialSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2889,
            )

            return self._parent._cast(
                _2889.BevelDifferentialSunGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2890.BevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2890,
            )

            return self._parent._cast(_2890.BevelGearCompoundSystemDeflection)

        @property
        def bolt_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2893.BoltCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2893,
            )

            return self._parent._cast(_2893.BoltCompoundSystemDeflection)

        @property
        def clutch_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2897.ClutchHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.ClutchHalfCompoundSystemDeflection)

        @property
        def concept_coupling_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2902.ConceptCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2902,
            )

            return self._parent._cast(_2902.ConceptCouplingHalfCompoundSystemDeflection)

        @property
        def concept_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2903.ConceptGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2903,
            )

            return self._parent._cast(_2903.ConceptGearCompoundSystemDeflection)

        @property
        def conical_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2906.ConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2906,
            )

            return self._parent._cast(_2906.ConicalGearCompoundSystemDeflection)

        @property
        def connector_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2910.ConnectorCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2910,
            )

            return self._parent._cast(_2910.ConnectorCompoundSystemDeflection)

        @property
        def coupling_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2913.CouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2913,
            )

            return self._parent._cast(_2913.CouplingHalfCompoundSystemDeflection)

        @property
        def cvt_pulley_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2916.CVTPulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2916,
            )

            return self._parent._cast(_2916.CVTPulleyCompoundSystemDeflection)

        @property
        def cycloidal_disc_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2919.CycloidalDiscCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2919,
            )

            return self._parent._cast(_2919.CycloidalDiscCompoundSystemDeflection)

        @property
        def cylindrical_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2921.CylindricalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2921,
            )

            return self._parent._cast(_2921.CylindricalGearCompoundSystemDeflection)

        @property
        def cylindrical_planet_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2924.CylindricalPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2924,
            )

            return self._parent._cast(
                _2924.CylindricalPlanetGearCompoundSystemDeflection
            )

        @property
        def datum_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2925.DatumCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2925,
            )

            return self._parent._cast(_2925.DatumCompoundSystemDeflection)

        @property
        def external_cad_model_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2927.ExternalCADModelCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2927,
            )

            return self._parent._cast(_2927.ExternalCADModelCompoundSystemDeflection)

        @property
        def face_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2928.FaceGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2928,
            )

            return self._parent._cast(_2928.FaceGearCompoundSystemDeflection)

        @property
        def fe_part_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2931.FEPartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(_2931.FEPartCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2933.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2933,
            )

            return self._parent._cast(_2933.GearCompoundSystemDeflection)

        @property
        def guide_dxf_model_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2936.GuideDxfModelCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2936,
            )

            return self._parent._cast(_2936.GuideDxfModelCompoundSystemDeflection)

        @property
        def hypoid_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2937.HypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2937,
            )

            return self._parent._cast(_2937.HypoidGearCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2941.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2941,
            )

            return self._parent._cast(
                _2941.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2944.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2944,
            )

            return self._parent._cast(
                _2944.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2947.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2947,
            )

            return self._parent._cast(
                _2947.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
            )

        @property
        def mass_disc_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2950.MassDiscCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2950,
            )

            return self._parent._cast(_2950.MassDiscCompoundSystemDeflection)

        @property
        def measurement_component_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2951.MeasurementComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2951,
            )

            return self._parent._cast(
                _2951.MeasurementComponentCompoundSystemDeflection
            )

        @property
        def mountable_component_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2952.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.MountableComponentCompoundSystemDeflection)

        @property
        def oil_seal_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2953.OilSealCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2953,
            )

            return self._parent._cast(_2953.OilSealCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2957.PartToPartShearCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2957,
            )

            return self._parent._cast(
                _2957.PartToPartShearCouplingHalfCompoundSystemDeflection
            )

        @property
        def planet_carrier_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2960.PlanetCarrierCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2960,
            )

            return self._parent._cast(_2960.PlanetCarrierCompoundSystemDeflection)

        @property
        def point_load_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2961.PointLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2961,
            )

            return self._parent._cast(_2961.PointLoadCompoundSystemDeflection)

        @property
        def power_load_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2962.PowerLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2962,
            )

            return self._parent._cast(_2962.PowerLoadCompoundSystemDeflection)

        @property
        def pulley_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2963.PulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2963,
            )

            return self._parent._cast(_2963.PulleyCompoundSystemDeflection)

        @property
        def ring_pins_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2964.RingPinsCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2964,
            )

            return self._parent._cast(_2964.RingPinsCompoundSystemDeflection)

        @property
        def rolling_ring_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2967.RollingRingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2967,
            )

            return self._parent._cast(_2967.RollingRingCompoundSystemDeflection)

        @property
        def shaft_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2970.ShaftCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2970,
            )

            return self._parent._cast(_2970.ShaftCompoundSystemDeflection)

        @property
        def shaft_hub_connection_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2972.ShaftHubConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2972,
            )

            return self._parent._cast(_2972.ShaftHubConnectionCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2975.SpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2975,
            )

            return self._parent._cast(_2975.SpiralBevelGearCompoundSystemDeflection)

        @property
        def spring_damper_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2980.SpringDamperHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2980,
            )

            return self._parent._cast(_2980.SpringDamperHalfCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2981.StraightBevelDiffGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2981,
            )

            return self._parent._cast(
                _2981.StraightBevelDiffGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2984.StraightBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2984,
            )

            return self._parent._cast(_2984.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_planet_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2987.StraightBevelPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2987,
            )

            return self._parent._cast(
                _2987.StraightBevelPlanetGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2988.StraightBevelSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2988,
            )

            return self._parent._cast(
                _2988.StraightBevelSunGearCompoundSystemDeflection
            )

        @property
        def synchroniser_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2990.SynchroniserHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2990,
            )

            return self._parent._cast(_2990.SynchroniserHalfCompoundSystemDeflection)

        @property
        def synchroniser_part_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2991.SynchroniserPartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2991,
            )

            return self._parent._cast(_2991.SynchroniserPartCompoundSystemDeflection)

        @property
        def synchroniser_sleeve_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2992.SynchroniserSleeveCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2992,
            )

            return self._parent._cast(_2992.SynchroniserSleeveCompoundSystemDeflection)

        @property
        def torque_converter_pump_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2995.TorqueConverterPumpCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2995,
            )

            return self._parent._cast(_2995.TorqueConverterPumpCompoundSystemDeflection)

        @property
        def torque_converter_turbine_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2996.TorqueConverterTurbineCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2996,
            )

            return self._parent._cast(
                _2996.TorqueConverterTurbineCompoundSystemDeflection
            )

        @property
        def unbalanced_mass_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2997.UnbalancedMassCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2997,
            )

            return self._parent._cast(_2997.UnbalancedMassCompoundSystemDeflection)

        @property
        def virtual_component_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2998.VirtualComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2998,
            )

            return self._parent._cast(_2998.VirtualComponentCompoundSystemDeflection)

        @property
        def worm_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2999.WormGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2999,
            )

            return self._parent._cast(_2999.WormGearCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_3002.ZerolBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _3002,
            )

            return self._parent._cast(_3002.ZerolBevelGearCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "ComponentCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "ComponentCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_2738.ComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2738.ComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection]

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
    ) -> "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection":
        return self._Cast_ComponentCompoundSystemDeflection(self)
