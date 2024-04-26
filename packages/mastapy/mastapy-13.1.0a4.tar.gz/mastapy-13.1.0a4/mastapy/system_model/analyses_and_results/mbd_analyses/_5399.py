"""AbstractAssemblyMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5491
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "AbstractAssemblyMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5405,
        _5407,
        _5412,
        _5415,
        _5420,
        _5421,
        _5425,
        _5431,
        _5434,
        _5437,
        _5442,
        _5444,
        _5446,
        _5452,
        _5458,
        _5460,
        _5464,
        _5468,
        _5476,
        _5479,
        _5482,
        _5494,
        _5496,
        _5503,
        _5506,
        _5513,
        _5516,
        _5520,
        _5523,
        _5526,
        _5530,
        _5535,
        _5544,
        _5547,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyMultibodyDynamicsAnalysis")


class AbstractAssemblyMultibodyDynamicsAnalysis(_5491.PartMultibodyDynamicsAnalysis):
    """AbstractAssemblyMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyMultibodyDynamicsAnalysis"
    )

    class _Cast_AbstractAssemblyMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractAssemblyMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
            parent: "AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def part_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5405.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5405

            return self._parent._cast(
                _5405.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def assembly_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5407.AssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5407

            return self._parent._cast(_5407.AssemblyMultibodyDynamicsAnalysis)

        @property
        def belt_drive_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5412.BeltDriveMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.BeltDriveMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5415.BevelDifferentialGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5415

            return self._parent._cast(
                _5415.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5420.BevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5420

            return self._parent._cast(_5420.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5421.BoltedJointMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421

            return self._parent._cast(_5421.BoltedJointMultibodyDynamicsAnalysis)

        @property
        def clutch_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5425.ClutchMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(_5425.ClutchMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5431.ConceptCouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5431

            return self._parent._cast(_5431.ConceptCouplingMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5434.ConceptGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5434

            return self._parent._cast(_5434.ConceptGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5437.ConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(_5437.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def coupling_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5442.CouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5442

            return self._parent._cast(_5442.CouplingMultibodyDynamicsAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5444.CVTMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5444

            return self._parent._cast(_5444.CVTMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5446.CycloidalAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5446

            return self._parent._cast(_5446.CycloidalAssemblyMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5452.CylindricalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452

            return self._parent._cast(_5452.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5458.FaceGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5458

            return self._parent._cast(_5458.FaceGearSetMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5460.FlexiblePinAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460

            return self._parent._cast(
                _5460.FlexiblePinAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5464.GearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.GearSetMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5468.HypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5468

            return self._parent._cast(_5468.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5476.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5476

            return self._parent._cast(
                _5476.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5479.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5479

            return self._parent._cast(
                _5479.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> (
            "_5482.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5482

            return self._parent._cast(
                _5482.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5494.PartToPartShearCouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5494

            return self._parent._cast(
                _5494.PartToPartShearCouplingMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5496.PlanetaryGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5496

            return self._parent._cast(_5496.PlanetaryGearSetMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5503.RollingRingAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5503

            return self._parent._cast(
                _5503.RollingRingAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def root_assembly_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5506.RootAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5506

            return self._parent._cast(_5506.RootAssemblyMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5513.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5513

            return self._parent._cast(
                _5513.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5516.SpiralBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5516

            return self._parent._cast(_5516.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def spring_damper_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5520.SpringDamperMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5520

            return self._parent._cast(_5520.SpringDamperMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5523.StraightBevelDiffGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5523

            return self._parent._cast(
                _5523.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5526.StraightBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5526

            return self._parent._cast(
                _5526.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5530.SynchroniserMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5530

            return self._parent._cast(_5530.SynchroniserMultibodyDynamicsAnalysis)

        @property
        def torque_converter_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5535.TorqueConverterMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5535

            return self._parent._cast(_5535.TorqueConverterMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5544.WormGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5544

            return self._parent._cast(_5544.WormGearSetMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5547.ZerolBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5547

            return self._parent._cast(_5547.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "AbstractAssemblyMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "AbstractAssemblyMultibodyDynamicsAnalysis.TYPE"
    ):
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
    ) -> "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis":
        return self._Cast_AbstractAssemblyMultibodyDynamicsAnalysis(self)
