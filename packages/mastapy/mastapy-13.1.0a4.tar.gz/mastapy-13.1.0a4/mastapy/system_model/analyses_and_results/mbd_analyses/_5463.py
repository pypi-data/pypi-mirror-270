"""GearMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5488
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "GearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import _5551
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5404,
        _5414,
        _5416,
        _5417,
        _5419,
        _5433,
        _5436,
        _5451,
        _5453,
        _5457,
        _5467,
        _5475,
        _5478,
        _5481,
        _5515,
        _5522,
        _5525,
        _5527,
        _5528,
        _5543,
        _5546,
        _5428,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="GearMultibodyDynamicsAnalysis")


class GearMultibodyDynamicsAnalysis(_5488.MountableComponentMultibodyDynamicsAnalysis):
    """GearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMultibodyDynamicsAnalysis")

    class _Cast_GearMultibodyDynamicsAnalysis:
        """Special nested class for casting GearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
            parent: "GearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5488.MountableComponentMultibodyDynamicsAnalysis":
            return self._parent._cast(_5488.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5428.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5404.AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(
                _5404.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5414.BevelDifferentialGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(
                _5414.BevelDifferentialGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5416.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416

            return self._parent._cast(
                _5416.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5417.BevelDifferentialSunGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5417

            return self._parent._cast(
                _5417.BevelDifferentialSunGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5419.BevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5419

            return self._parent._cast(_5419.BevelGearMultibodyDynamicsAnalysis)

        @property
        def concept_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5433.ConceptGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433

            return self._parent._cast(_5433.ConceptGearMultibodyDynamicsAnalysis)

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5436.ConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5451.CylindricalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(_5451.CylindricalGearMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5453.CylindricalPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5453

            return self._parent._cast(
                _5453.CylindricalPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5457.FaceGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5457

            return self._parent._cast(_5457.FaceGearMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5467.HypoidGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.HypoidGearMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5475.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(
                _5475.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5478.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478

            return self._parent._cast(
                _5478.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5481.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5481

            return self._parent._cast(
                _5481.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5515.SpiralBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5515

            return self._parent._cast(_5515.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5522.StraightBevelDiffGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5522

            return self._parent._cast(
                _5522.StraightBevelDiffGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5525.StraightBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5525

            return self._parent._cast(_5525.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5527.StraightBevelPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5527

            return self._parent._cast(
                _5527.StraightBevelPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5528.StraightBevelSunGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5528

            return self._parent._cast(
                _5528.StraightBevelSunGearMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5543.WormGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5543

            return self._parent._cast(_5543.WormGearMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "_5546.ZerolBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5546

            return self._parent._cast(_5546.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
        ) -> "GearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMultibodyDynamicsAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_mesh_forces_on_shaft(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshForcesOnShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def gear_mesh_moments_on_shaft(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshMomentsOnShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def gear_mesh_torque(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshTorque

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def component_design(self: Self) -> "_2548.Gear":
        """mastapy.system_model.part_model.gears.Gear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def peak_gear_torque(self: Self) -> "List[_5551.DynamicTorqueResultAtTime]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.reporting.DynamicTorqueResultAtTime]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakGearTorque

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis":
        return self._Cast_GearMultibodyDynamicsAnalysis(self)
