"""ComponentDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ComponentDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6304,
        _6305,
        _6307,
        _6311,
        _6314,
        _6317,
        _6318,
        _6319,
        _6322,
        _6326,
        _6331,
        _6332,
        _6335,
        _6339,
        _6342,
        _6345,
        _6348,
        _6350,
        _6353,
        _6354,
        _6357,
        _6358,
        _6361,
        _6363,
        _6366,
        _6367,
        _6371,
        _6374,
        _6377,
        _6380,
        _6381,
        _6382,
        _6383,
        _6387,
        _6390,
        _6391,
        _6392,
        _6393,
        _6394,
        _6398,
        _6400,
        _6401,
        _6404,
        _6409,
        _6410,
        _6413,
        _6416,
        _6417,
        _6419,
        _6420,
        _6421,
        _6424,
        _6425,
        _6426,
        _6427,
        _6428,
        _6431,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ComponentDynamicAnalysis",)


Self = TypeVar("Self", bound="ComponentDynamicAnalysis")


class ComponentDynamicAnalysis(_6384.PartDynamicAnalysis):
    """ComponentDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentDynamicAnalysis")

    class _Cast_ComponentDynamicAnalysis:
        """Special nested class for casting ComponentDynamicAnalysis to subclasses."""

        def __init__(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
            parent: "ComponentDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def part_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6384.PartDynamicAnalysis":
            return self._parent._cast(_6384.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6304.AbstractShaftDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.AbstractShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6305.AbstractShaftOrHousingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305

            return self._parent._cast(_6305.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6307.AGMAGleasonConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def bearing_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6311.BearingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.BearingDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6314.BevelDifferentialGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314

            return self._parent._cast(_6314.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6317.BevelDifferentialPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6317

            return self._parent._cast(_6317.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6318.BevelDifferentialSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318

            return self._parent._cast(_6318.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6319.BevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.BevelGearDynamicAnalysis)

        @property
        def bolt_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6322.BoltDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6322

            return self._parent._cast(_6322.BoltDynamicAnalysis)

        @property
        def clutch_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6326.ClutchHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326

            return self._parent._cast(_6326.ClutchHalfDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6331.ConceptCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6331

            return self._parent._cast(_6331.ConceptCouplingHalfDynamicAnalysis)

        @property
        def concept_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6332.ConceptGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332

            return self._parent._cast(_6332.ConceptGearDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6335.ConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.ConicalGearDynamicAnalysis)

        @property
        def connector_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6339.ConnectorDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.ConnectorDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6342.CouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342

            return self._parent._cast(_6342.CouplingHalfDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6345.CVTPulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345

            return self._parent._cast(_6345.CVTPulleyDynamicAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6348.CycloidalDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6348

            return self._parent._cast(_6348.CycloidalDiscDynamicAnalysis)

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6350.CylindricalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350

            return self._parent._cast(_6350.CylindricalGearDynamicAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6353.CylindricalPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(_6353.CylindricalPlanetGearDynamicAnalysis)

        @property
        def datum_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6354.DatumDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.DatumDynamicAnalysis)

        @property
        def external_cad_model_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6357.ExternalCADModelDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.ExternalCADModelDynamicAnalysis)

        @property
        def face_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6358.FaceGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.FaceGearDynamicAnalysis)

        @property
        def fe_part_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6361.FEPartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6361

            return self._parent._cast(_6361.FEPartDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6363.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.GearDynamicAnalysis)

        @property
        def guide_dxf_model_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6366.GuideDxfModelDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.GuideDxfModelDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6367.HypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6367

            return self._parent._cast(_6367.HypoidGearDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6371.KlingelnbergCycloPalloidConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6371

            return self._parent._cast(
                _6371.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6374.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(
                _6374.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6377.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(
                _6377.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
            )

        @property
        def mass_disc_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6380.MassDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380

            return self._parent._cast(_6380.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6381.MeasurementComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6381

            return self._parent._cast(_6381.MeasurementComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6382.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.MountableComponentDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6383.OilSealDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6383

            return self._parent._cast(_6383.OilSealDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6387.PartToPartShearCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def planet_carrier_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6390.PlanetCarrierDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.PlanetCarrierDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6391.PointLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6391

            return self._parent._cast(_6391.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6392.PowerLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6392

            return self._parent._cast(_6392.PowerLoadDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6393.PulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6393

            return self._parent._cast(_6393.PulleyDynamicAnalysis)

        @property
        def ring_pins_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6394.RingPinsDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6394

            return self._parent._cast(_6394.RingPinsDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6398.RollingRingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398

            return self._parent._cast(_6398.RollingRingDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6400.ShaftDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400

            return self._parent._cast(_6400.ShaftDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6401.ShaftHubConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6401

            return self._parent._cast(_6401.ShaftHubConnectionDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6404.SpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6404

            return self._parent._cast(_6404.SpiralBevelGearDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6409.SpringDamperHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6409

            return self._parent._cast(_6409.SpringDamperHalfDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6410.StraightBevelDiffGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6410

            return self._parent._cast(_6410.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6413.StraightBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6413

            return self._parent._cast(_6413.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6416.StraightBevelPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6416

            return self._parent._cast(_6416.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6417.StraightBevelSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6417

            return self._parent._cast(_6417.StraightBevelSunGearDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6419.SynchroniserHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6419

            return self._parent._cast(_6419.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6420.SynchroniserPartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6420

            return self._parent._cast(_6420.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6421.SynchroniserSleeveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6421

            return self._parent._cast(_6421.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6424.TorqueConverterPumpDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6424

            return self._parent._cast(_6424.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6425.TorqueConverterTurbineDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6425

            return self._parent._cast(_6425.TorqueConverterTurbineDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6426.UnbalancedMassDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6426

            return self._parent._cast(_6426.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6427.VirtualComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6427

            return self._parent._cast(_6427.VirtualComponentDynamicAnalysis)

        @property
        def worm_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6428.WormGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6428

            return self._parent._cast(_6428.WormGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "_6431.ZerolBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6431

            return self._parent._cast(_6431.ZerolBevelGearDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "ComponentDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentDynamicAnalysis.TYPE"):
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
    ) -> "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis":
        return self._Cast_ComponentDynamicAnalysis(self)
