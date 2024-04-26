"""ComponentHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5814
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ComponentHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.modal_analyses import _4620
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5891,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2738
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5706,
        _5707,
        _5709,
        _5713,
        _5716,
        _5719,
        _5720,
        _5721,
        _5725,
        _5727,
        _5733,
        _5735,
        _5738,
        _5742,
        _5744,
        _5748,
        _5751,
        _5753,
        _5756,
        _5757,
        _5772,
        _5773,
        _5776,
        _5779,
        _5786,
        _5797,
        _5801,
        _5804,
        _5807,
        _5810,
        _5811,
        _5812,
        _5813,
        _5816,
        _5821,
        _5822,
        _5823,
        _5824,
        _5826,
        _5830,
        _5832,
        _5833,
        _5838,
        _5842,
        _5845,
        _5848,
        _5851,
        _5852,
        _5853,
        _5855,
        _5856,
        _5859,
        _5860,
        _5862,
        _5863,
        _5864,
        _5867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ComponentHarmonicAnalysis",)


Self = TypeVar("Self", bound="ComponentHarmonicAnalysis")


class ComponentHarmonicAnalysis(_5814.PartHarmonicAnalysis):
    """ComponentHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentHarmonicAnalysis")

    class _Cast_ComponentHarmonicAnalysis:
        """Special nested class for casting ComponentHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
            parent: "ComponentHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def part_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5706.AbstractShaftHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5706,
            )

            return self._parent._cast(_5706.AbstractShaftHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5707.AbstractShaftOrHousingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5707,
            )

            return self._parent._cast(_5707.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5709.AGMAGleasonConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5709,
            )

            return self._parent._cast(_5709.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def bearing_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5713.BearingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.BearingHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5716.BevelDifferentialGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5716,
            )

            return self._parent._cast(_5716.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5719.BevelDifferentialPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5719,
            )

            return self._parent._cast(_5719.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5720.BevelDifferentialSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5720,
            )

            return self._parent._cast(_5720.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5721.BevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5721,
            )

            return self._parent._cast(_5721.BevelGearHarmonicAnalysis)

        @property
        def bolt_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5725.BoltHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5725,
            )

            return self._parent._cast(_5725.BoltHarmonicAnalysis)

        @property
        def clutch_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5727.ClutchHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5727,
            )

            return self._parent._cast(_5727.ClutchHalfHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5733.ConceptCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5733,
            )

            return self._parent._cast(_5733.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def concept_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5735.ConceptGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5735,
            )

            return self._parent._cast(_5735.ConceptGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5738.ConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5738,
            )

            return self._parent._cast(_5738.ConicalGearHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5742.ConnectorHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5742,
            )

            return self._parent._cast(_5742.ConnectorHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5744.CouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5744,
            )

            return self._parent._cast(_5744.CouplingHalfHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5748.CVTPulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5748,
            )

            return self._parent._cast(_5748.CVTPulleyHarmonicAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5751.CycloidalDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5751,
            )

            return self._parent._cast(_5751.CycloidalDiscHarmonicAnalysis)

        @property
        def cylindrical_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5753.CylindricalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5753,
            )

            return self._parent._cast(_5753.CylindricalGearHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5756.CylindricalPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5756,
            )

            return self._parent._cast(_5756.CylindricalPlanetGearHarmonicAnalysis)

        @property
        def datum_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5757.DatumHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5757,
            )

            return self._parent._cast(_5757.DatumHarmonicAnalysis)

        @property
        def external_cad_model_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5772.ExternalCADModelHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5772,
            )

            return self._parent._cast(_5772.ExternalCADModelHarmonicAnalysis)

        @property
        def face_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5773.FaceGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5773,
            )

            return self._parent._cast(_5773.FaceGearHarmonicAnalysis)

        @property
        def fe_part_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5776.FEPartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5776,
            )

            return self._parent._cast(_5776.FEPartHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5779.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5779,
            )

            return self._parent._cast(_5779.GearHarmonicAnalysis)

        @property
        def guide_dxf_model_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5786.GuideDxfModelHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5786,
            )

            return self._parent._cast(_5786.GuideDxfModelHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5797.HypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5797,
            )

            return self._parent._cast(_5797.HypoidGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5801.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5801,
            )

            return self._parent._cast(
                _5801.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5804.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5804,
            )

            return self._parent._cast(
                _5804.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5807.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5807,
            )

            return self._parent._cast(
                _5807.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
            )

        @property
        def mass_disc_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5810.MassDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5810,
            )

            return self._parent._cast(_5810.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5811.MeasurementComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5811,
            )

            return self._parent._cast(_5811.MeasurementComponentHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5812.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.MountableComponentHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5813.OilSealHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5813,
            )

            return self._parent._cast(_5813.OilSealHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5816.PartToPartShearCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5816,
            )

            return self._parent._cast(_5816.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def planet_carrier_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5821.PlanetCarrierHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5821,
            )

            return self._parent._cast(_5821.PlanetCarrierHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5822.PointLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5822,
            )

            return self._parent._cast(_5822.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5823.PowerLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5823,
            )

            return self._parent._cast(_5823.PowerLoadHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5824.PulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5824,
            )

            return self._parent._cast(_5824.PulleyHarmonicAnalysis)

        @property
        def ring_pins_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5826.RingPinsHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5826,
            )

            return self._parent._cast(_5826.RingPinsHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5830.RollingRingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5830,
            )

            return self._parent._cast(_5830.RollingRingHarmonicAnalysis)

        @property
        def shaft_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5832.ShaftHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5832,
            )

            return self._parent._cast(_5832.ShaftHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5833.ShaftHubConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5833,
            )

            return self._parent._cast(_5833.ShaftHubConnectionHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5838.SpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5838,
            )

            return self._parent._cast(_5838.SpiralBevelGearHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5842.SpringDamperHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5842,
            )

            return self._parent._cast(_5842.SpringDamperHalfHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5845.StraightBevelDiffGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5845,
            )

            return self._parent._cast(_5845.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5848.StraightBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5848,
            )

            return self._parent._cast(_5848.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5851.StraightBevelPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5851,
            )

            return self._parent._cast(_5851.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5852.StraightBevelSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5852,
            )

            return self._parent._cast(_5852.StraightBevelSunGearHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5853.SynchroniserHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5853,
            )

            return self._parent._cast(_5853.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5855.SynchroniserPartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5855,
            )

            return self._parent._cast(_5855.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5856.SynchroniserSleeveHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5856,
            )

            return self._parent._cast(_5856.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5859.TorqueConverterPumpHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5859,
            )

            return self._parent._cast(_5859.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5860.TorqueConverterTurbineHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5860,
            )

            return self._parent._cast(_5860.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5862.UnbalancedMassHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5862,
            )

            return self._parent._cast(_5862.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5863.VirtualComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5863,
            )

            return self._parent._cast(_5863.VirtualComponentHarmonicAnalysis)

        @property
        def worm_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5864.WormGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5864,
            )

            return self._parent._cast(_5864.WormGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "_5867.ZerolBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5867,
            )

            return self._parent._cast(_5867.ZerolBevelGearHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "ComponentHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

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
    def coupled_modal_analysis(self: Self) -> "_4620.ComponentModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ComponentModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results(self: Self) -> "_5891.HarmonicAnalysisResultsPropertyAccessor":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.HarmonicAnalysisResultsPropertyAccessor

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Results

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2738.ComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis":
        return self._Cast_ComponentHarmonicAnalysis(self)
