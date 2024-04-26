"""MountableComponentMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5428
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "MountableComponentMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2482
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5404,
        _5409,
        _5414,
        _5416,
        _5417,
        _5419,
        _5424,
        _5430,
        _5433,
        _5436,
        _5439,
        _5441,
        _5445,
        _5451,
        _5453,
        _5457,
        _5463,
        _5467,
        _5475,
        _5478,
        _5481,
        _5483,
        _5487,
        _5490,
        _5493,
        _5497,
        _5498,
        _5499,
        _5500,
        _5501,
        _5505,
        _5509,
        _5515,
        _5519,
        _5522,
        _5525,
        _5527,
        _5528,
        _5529,
        _5531,
        _5532,
        _5536,
        _5538,
        _5539,
        _5540,
        _5543,
        _5546,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="MountableComponentMultibodyDynamicsAnalysis")


class MountableComponentMultibodyDynamicsAnalysis(
    _5428.ComponentMultibodyDynamicsAnalysis
):
    """MountableComponentMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentMultibodyDynamicsAnalysis"
    )

    class _Cast_MountableComponentMultibodyDynamicsAnalysis:
        """Special nested class for casting MountableComponentMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
            parent: "MountableComponentMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def component_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5428.ComponentMultibodyDynamicsAnalysis":
            return self._parent._cast(_5428.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5404.AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(
                _5404.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def bearing_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5409.BearingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5409

            return self._parent._cast(_5409.BearingMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5414.BevelDifferentialGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(
                _5414.BevelDifferentialGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5416.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416

            return self._parent._cast(
                _5416.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5417.BevelDifferentialSunGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5417

            return self._parent._cast(
                _5417.BevelDifferentialSunGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5419.BevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5419

            return self._parent._cast(_5419.BevelGearMultibodyDynamicsAnalysis)

        @property
        def clutch_half_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5424.ClutchHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5424

            return self._parent._cast(_5424.ClutchHalfMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5430.ConceptCouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5430

            return self._parent._cast(
                _5430.ConceptCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5433.ConceptGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433

            return self._parent._cast(_5433.ConceptGearMultibodyDynamicsAnalysis)

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5436.ConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def connector_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5439.ConnectorMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.ConnectorMultibodyDynamicsAnalysis)

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5441.CouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5441

            return self._parent._cast(_5441.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5445.CVTPulleyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5445

            return self._parent._cast(_5445.CVTPulleyMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5451.CylindricalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(_5451.CylindricalGearMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5453.CylindricalPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5453

            return self._parent._cast(
                _5453.CylindricalPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5457.FaceGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5457

            return self._parent._cast(_5457.FaceGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5463.GearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.GearMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5467.HypoidGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.HypoidGearMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5475.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(
                _5475.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5478.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478

            return self._parent._cast(
                _5478.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5481.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5481

            return self._parent._cast(
                _5481.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5483.MassDiscMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5483

            return self._parent._cast(_5483.MassDiscMultibodyDynamicsAnalysis)

        @property
        def measurement_component_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5487.MeasurementComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487

            return self._parent._cast(
                _5487.MeasurementComponentMultibodyDynamicsAnalysis
            )

        @property
        def oil_seal_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5490.OilSealMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5490

            return self._parent._cast(_5490.OilSealMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5493.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5493

            return self._parent._cast(
                _5493.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def planet_carrier_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5497.PlanetCarrierMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5497

            return self._parent._cast(_5497.PlanetCarrierMultibodyDynamicsAnalysis)

        @property
        def point_load_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5498.PointLoadMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(_5498.PointLoadMultibodyDynamicsAnalysis)

        @property
        def power_load_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5499.PowerLoadMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5499

            return self._parent._cast(_5499.PowerLoadMultibodyDynamicsAnalysis)

        @property
        def pulley_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5500.PulleyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5500

            return self._parent._cast(_5500.PulleyMultibodyDynamicsAnalysis)

        @property
        def ring_pins_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5501.RingPinsMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5501

            return self._parent._cast(_5501.RingPinsMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5505.RollingRingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5505

            return self._parent._cast(_5505.RollingRingMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5509.ShaftHubConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5509

            return self._parent._cast(_5509.ShaftHubConnectionMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5515.SpiralBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5515

            return self._parent._cast(_5515.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5519.SpringDamperHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5519

            return self._parent._cast(_5519.SpringDamperHalfMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5522.StraightBevelDiffGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5522

            return self._parent._cast(
                _5522.StraightBevelDiffGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5525.StraightBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5525

            return self._parent._cast(_5525.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5527.StraightBevelPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5527

            return self._parent._cast(
                _5527.StraightBevelPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5528.StraightBevelSunGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5528

            return self._parent._cast(
                _5528.StraightBevelSunGearMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5529.SynchroniserHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5529

            return self._parent._cast(_5529.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5531.SynchroniserPartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5531

            return self._parent._cast(_5531.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5532.SynchroniserSleeveMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5532

            return self._parent._cast(_5532.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5536.TorqueConverterPumpMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5536

            return self._parent._cast(
                _5536.TorqueConverterPumpMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5538.TorqueConverterTurbineMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5538

            return self._parent._cast(
                _5538.TorqueConverterTurbineMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5539.UnbalancedMassMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5539

            return self._parent._cast(_5539.UnbalancedMassMultibodyDynamicsAnalysis)

        @property
        def virtual_component_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5540.VirtualComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5540

            return self._parent._cast(_5540.VirtualComponentMultibodyDynamicsAnalysis)

        @property
        def worm_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5543.WormGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5543

            return self._parent._cast(_5543.WormGearMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5546.ZerolBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5546

            return self._parent._cast(_5546.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "MountableComponentMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "MountableComponentMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def elastic_acceleration_force(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticAccelerationForce

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_acceleration_moment(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticAccelerationMoment

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_quadratic_velocity_force(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticQuadraticVelocityForce

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_quadratic_velocity_moment(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticQuadraticVelocityMoment

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def reference_acceleration_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceAccelerationTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_quadratic_velocity_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceQuadraticVelocityTorque

        if temp is None:
            return 0.0

        return temp

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
    ) -> "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis":
        return self._Cast_MountableComponentMultibodyDynamicsAnalysis(self)
