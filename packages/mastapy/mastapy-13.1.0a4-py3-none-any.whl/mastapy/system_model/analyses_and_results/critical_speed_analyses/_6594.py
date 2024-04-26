"""ComponentCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6651
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ComponentCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6570,
        _6571,
        _6573,
        _6577,
        _6580,
        _6583,
        _6584,
        _6585,
        _6588,
        _6592,
        _6597,
        _6598,
        _6601,
        _6605,
        _6608,
        _6614,
        _6617,
        _6619,
        _6622,
        _6623,
        _6624,
        _6625,
        _6628,
        _6630,
        _6633,
        _6634,
        _6638,
        _6641,
        _6644,
        _6647,
        _6648,
        _6649,
        _6650,
        _6654,
        _6657,
        _6658,
        _6659,
        _6660,
        _6661,
        _6665,
        _6667,
        _6668,
        _6671,
        _6676,
        _6677,
        _6680,
        _6683,
        _6684,
        _6686,
        _6687,
        _6688,
        _6691,
        _6692,
        _6693,
        _6694,
        _6695,
        _6698,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ComponentCriticalSpeedAnalysis")


class ComponentCriticalSpeedAnalysis(_6651.PartCriticalSpeedAnalysis):
    """ComponentCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCriticalSpeedAnalysis")

    class _Cast_ComponentCriticalSpeedAnalysis:
        """Special nested class for casting ComponentCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
            parent: "ComponentCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def part_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6651.PartCriticalSpeedAnalysis":
            return self._parent._cast(_6651.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6570.AbstractShaftCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6570,
            )

            return self._parent._cast(_6570.AbstractShaftCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6571.AbstractShaftOrHousingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6571,
            )

            return self._parent._cast(_6571.AbstractShaftOrHousingCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6573.AGMAGleasonConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6573,
            )

            return self._parent._cast(_6573.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def bearing_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6577.BearingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(_6577.BearingCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6580.BevelDifferentialGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6580,
            )

            return self._parent._cast(_6580.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6583.BevelDifferentialPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6583,
            )

            return self._parent._cast(
                _6583.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6584.BevelDifferentialSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6584,
            )

            return self._parent._cast(
                _6584.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6585.BevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6585,
            )

            return self._parent._cast(_6585.BevelGearCriticalSpeedAnalysis)

        @property
        def bolt_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6588.BoltCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6588,
            )

            return self._parent._cast(_6588.BoltCriticalSpeedAnalysis)

        @property
        def clutch_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6592.ClutchHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6592,
            )

            return self._parent._cast(_6592.ClutchHalfCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6597.ConceptCouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6597,
            )

            return self._parent._cast(_6597.ConceptCouplingHalfCriticalSpeedAnalysis)

        @property
        def concept_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6598.ConceptGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6598,
            )

            return self._parent._cast(_6598.ConceptGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6601.ConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6601,
            )

            return self._parent._cast(_6601.ConicalGearCriticalSpeedAnalysis)

        @property
        def connector_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6605.ConnectorCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6605,
            )

            return self._parent._cast(_6605.ConnectorCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6608.CouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6608,
            )

            return self._parent._cast(_6608.CouplingHalfCriticalSpeedAnalysis)

        @property
        def cvt_pulley_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6614.CVTPulleyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6614,
            )

            return self._parent._cast(_6614.CVTPulleyCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6617.CycloidalDiscCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6617,
            )

            return self._parent._cast(_6617.CycloidalDiscCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6619.CylindricalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(_6619.CylindricalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6622.CylindricalPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.CylindricalPlanetGearCriticalSpeedAnalysis)

        @property
        def datum_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6623.DatumCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6623,
            )

            return self._parent._cast(_6623.DatumCriticalSpeedAnalysis)

        @property
        def external_cad_model_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6624.ExternalCADModelCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(_6624.ExternalCADModelCriticalSpeedAnalysis)

        @property
        def face_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6625.FaceGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.FaceGearCriticalSpeedAnalysis)

        @property
        def fe_part_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6628.FEPartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6628,
            )

            return self._parent._cast(_6628.FEPartCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6630.GearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6630,
            )

            return self._parent._cast(_6630.GearCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6633.GuideDxfModelCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.GuideDxfModelCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6634.HypoidGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6634,
            )

            return self._parent._cast(_6634.HypoidGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6638.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6638,
            )

            return self._parent._cast(
                _6638.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6641.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6641,
            )

            return self._parent._cast(
                _6641.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6644.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(
                _6644.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
            )

        @property
        def mass_disc_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6647.MassDiscCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6647,
            )

            return self._parent._cast(_6647.MassDiscCriticalSpeedAnalysis)

        @property
        def measurement_component_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6648.MeasurementComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6648,
            )

            return self._parent._cast(_6648.MeasurementComponentCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6649.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6649,
            )

            return self._parent._cast(_6649.MountableComponentCriticalSpeedAnalysis)

        @property
        def oil_seal_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6650.OilSealCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6650,
            )

            return self._parent._cast(_6650.OilSealCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6654.PartToPartShearCouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(
                _6654.PartToPartShearCouplingHalfCriticalSpeedAnalysis
            )

        @property
        def planet_carrier_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6657.PlanetCarrierCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6657,
            )

            return self._parent._cast(_6657.PlanetCarrierCriticalSpeedAnalysis)

        @property
        def point_load_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6658.PointLoadCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6658,
            )

            return self._parent._cast(_6658.PointLoadCriticalSpeedAnalysis)

        @property
        def power_load_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6659.PowerLoadCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6659,
            )

            return self._parent._cast(_6659.PowerLoadCriticalSpeedAnalysis)

        @property
        def pulley_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6660.PulleyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6660,
            )

            return self._parent._cast(_6660.PulleyCriticalSpeedAnalysis)

        @property
        def ring_pins_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6661.RingPinsCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6661,
            )

            return self._parent._cast(_6661.RingPinsCriticalSpeedAnalysis)

        @property
        def rolling_ring_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6665.RollingRingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6665,
            )

            return self._parent._cast(_6665.RollingRingCriticalSpeedAnalysis)

        @property
        def shaft_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6667.ShaftCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6667,
            )

            return self._parent._cast(_6667.ShaftCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6668.ShaftHubConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6668,
            )

            return self._parent._cast(_6668.ShaftHubConnectionCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6671.SpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6671,
            )

            return self._parent._cast(_6671.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def spring_damper_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6676.SpringDamperHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6676,
            )

            return self._parent._cast(_6676.SpringDamperHalfCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6677.StraightBevelDiffGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6677,
            )

            return self._parent._cast(_6677.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6680.StraightBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6680,
            )

            return self._parent._cast(_6680.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6683.StraightBevelPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6683,
            )

            return self._parent._cast(
                _6683.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6684.StraightBevelSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6684,
            )

            return self._parent._cast(_6684.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def synchroniser_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6686.SynchroniserHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6686,
            )

            return self._parent._cast(_6686.SynchroniserHalfCriticalSpeedAnalysis)

        @property
        def synchroniser_part_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6687.SynchroniserPartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6687,
            )

            return self._parent._cast(_6687.SynchroniserPartCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6688.SynchroniserSleeveCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6688,
            )

            return self._parent._cast(_6688.SynchroniserSleeveCriticalSpeedAnalysis)

        @property
        def torque_converter_pump_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6691.TorqueConverterPumpCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6691,
            )

            return self._parent._cast(_6691.TorqueConverterPumpCriticalSpeedAnalysis)

        @property
        def torque_converter_turbine_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6692.TorqueConverterTurbineCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6692,
            )

            return self._parent._cast(_6692.TorqueConverterTurbineCriticalSpeedAnalysis)

        @property
        def unbalanced_mass_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6693.UnbalancedMassCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6693,
            )

            return self._parent._cast(_6693.UnbalancedMassCriticalSpeedAnalysis)

        @property
        def virtual_component_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6694.VirtualComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6694,
            )

            return self._parent._cast(_6694.VirtualComponentCriticalSpeedAnalysis)

        @property
        def worm_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6695.WormGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6695,
            )

            return self._parent._cast(_6695.WormGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "_6698.ZerolBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6698,
            )

            return self._parent._cast(_6698.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "ComponentCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2462.Component":
        """mastapy.system_model.part_model.Component

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
    ) -> "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis":
        return self._Cast_ComponentCriticalSpeedAnalysis(self)
