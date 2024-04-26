"""PartMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7575
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "PartMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2486
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5489,
        _5399,
        _5400,
        _5401,
        _5404,
        _5405,
        _5407,
        _5409,
        _5412,
        _5414,
        _5415,
        _5416,
        _5417,
        _5419,
        _5420,
        _5421,
        _5422,
        _5424,
        _5425,
        _5428,
        _5430,
        _5431,
        _5433,
        _5434,
        _5436,
        _5437,
        _5439,
        _5441,
        _5442,
        _5444,
        _5445,
        _5446,
        _5448,
        _5451,
        _5452,
        _5453,
        _5454,
        _5455,
        _5457,
        _5458,
        _5459,
        _5460,
        _5463,
        _5464,
        _5465,
        _5467,
        _5468,
        _5475,
        _5476,
        _5478,
        _5479,
        _5481,
        _5482,
        _5483,
        _5487,
        _5488,
        _5490,
        _5493,
        _5494,
        _5496,
        _5497,
        _5498,
        _5499,
        _5500,
        _5501,
        _5503,
        _5505,
        _5506,
        _5509,
        _5510,
        _5513,
        _5515,
        _5516,
        _5519,
        _5520,
        _5522,
        _5523,
        _5525,
        _5526,
        _5527,
        _5528,
        _5529,
        _5530,
        _5531,
        _5532,
        _5535,
        _5536,
        _5538,
        _5539,
        _5540,
        _5543,
        _5544,
        _5546,
        _5547,
    )
    from mastapy.math_utility.convergence import _1588
    from mastapy.system_model.drawing import _2268
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PartMultibodyDynamicsAnalysis")


class PartMultibodyDynamicsAnalysis(_7575.PartTimeSeriesLoadAnalysisCase):
    """PartMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartMultibodyDynamicsAnalysis")

    class _Cast_PartMultibodyDynamicsAnalysis:
        """Special nested class for casting PartMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
            parent: "PartMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def part_time_series_load_analysis_case(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5399.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5399

            return self._parent._cast(_5399.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5400.AbstractShaftMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(_5400.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5401.AbstractShaftOrHousingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(
                _5401.AbstractShaftOrHousingMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5404.AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(
                _5404.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5405.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5405

            return self._parent._cast(
                _5405.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5407.AssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5407

            return self._parent._cast(_5407.AssemblyMultibodyDynamicsAnalysis)

        @property
        def bearing_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5409.BearingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5409

            return self._parent._cast(_5409.BearingMultibodyDynamicsAnalysis)

        @property
        def belt_drive_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5412.BeltDriveMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.BeltDriveMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5414.BevelDifferentialGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(
                _5414.BevelDifferentialGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5415.BevelDifferentialGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5415

            return self._parent._cast(
                _5415.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5416.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416

            return self._parent._cast(
                _5416.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5417.BevelDifferentialSunGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5417

            return self._parent._cast(
                _5417.BevelDifferentialSunGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5419.BevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5419

            return self._parent._cast(_5419.BevelGearMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5420.BevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5420

            return self._parent._cast(_5420.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5421.BoltedJointMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421

            return self._parent._cast(_5421.BoltedJointMultibodyDynamicsAnalysis)

        @property
        def bolt_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5422.BoltMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422

            return self._parent._cast(_5422.BoltMultibodyDynamicsAnalysis)

        @property
        def clutch_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5424.ClutchHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5424

            return self._parent._cast(_5424.ClutchHalfMultibodyDynamicsAnalysis)

        @property
        def clutch_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5425.ClutchMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(_5425.ClutchMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5428.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.ComponentMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5430.ConceptCouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5430

            return self._parent._cast(
                _5430.ConceptCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5431.ConceptCouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5431

            return self._parent._cast(_5431.ConceptCouplingMultibodyDynamicsAnalysis)

        @property
        def concept_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5433.ConceptGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433

            return self._parent._cast(_5433.ConceptGearMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5434.ConceptGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5434

            return self._parent._cast(_5434.ConceptGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5436.ConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5437.ConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(_5437.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def connector_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5439.ConnectorMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.ConnectorMultibodyDynamicsAnalysis)

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5441.CouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5441

            return self._parent._cast(_5441.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def coupling_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5442.CouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5442

            return self._parent._cast(_5442.CouplingMultibodyDynamicsAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5444.CVTMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5444

            return self._parent._cast(_5444.CVTMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5445.CVTPulleyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5445

            return self._parent._cast(_5445.CVTPulleyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5446.CycloidalAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5446

            return self._parent._cast(_5446.CycloidalAssemblyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5448.CycloidalDiscMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5448

            return self._parent._cast(_5448.CycloidalDiscMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5451.CylindricalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(_5451.CylindricalGearMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5452.CylindricalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452

            return self._parent._cast(_5452.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5453.CylindricalPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5453

            return self._parent._cast(
                _5453.CylindricalPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def datum_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5454.DatumMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5454

            return self._parent._cast(_5454.DatumMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5455.ExternalCADModelMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5455

            return self._parent._cast(_5455.ExternalCADModelMultibodyDynamicsAnalysis)

        @property
        def face_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5457.FaceGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5457

            return self._parent._cast(_5457.FaceGearMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5458.FaceGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5458

            return self._parent._cast(_5458.FaceGearSetMultibodyDynamicsAnalysis)

        @property
        def fe_part_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5459.FEPartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5459

            return self._parent._cast(_5459.FEPartMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5460.FlexiblePinAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460

            return self._parent._cast(
                _5460.FlexiblePinAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5463.GearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.GearMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5464.GearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.GearSetMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5465.GuideDxfModelMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5465

            return self._parent._cast(_5465.GuideDxfModelMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5467.HypoidGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.HypoidGearMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5468.HypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5468

            return self._parent._cast(_5468.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5475.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(
                _5475.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5476.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5476

            return self._parent._cast(
                _5476.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5478.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478

            return self._parent._cast(
                _5478.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5479.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5479

            return self._parent._cast(
                _5479.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5481.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5481

            return self._parent._cast(
                _5481.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> (
            "_5482.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5482

            return self._parent._cast(
                _5482.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5483.MassDiscMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5483

            return self._parent._cast(_5483.MassDiscMultibodyDynamicsAnalysis)

        @property
        def measurement_component_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5487.MeasurementComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487

            return self._parent._cast(
                _5487.MeasurementComponentMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5488.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def oil_seal_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5490.OilSealMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5490

            return self._parent._cast(_5490.OilSealMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5493.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5493

            return self._parent._cast(
                _5493.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5494.PartToPartShearCouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5494

            return self._parent._cast(
                _5494.PartToPartShearCouplingMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5496.PlanetaryGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5496

            return self._parent._cast(_5496.PlanetaryGearSetMultibodyDynamicsAnalysis)

        @property
        def planet_carrier_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5497.PlanetCarrierMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5497

            return self._parent._cast(_5497.PlanetCarrierMultibodyDynamicsAnalysis)

        @property
        def point_load_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5498.PointLoadMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(_5498.PointLoadMultibodyDynamicsAnalysis)

        @property
        def power_load_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5499.PowerLoadMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5499

            return self._parent._cast(_5499.PowerLoadMultibodyDynamicsAnalysis)

        @property
        def pulley_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5500.PulleyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5500

            return self._parent._cast(_5500.PulleyMultibodyDynamicsAnalysis)

        @property
        def ring_pins_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5501.RingPinsMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5501

            return self._parent._cast(_5501.RingPinsMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5503.RollingRingAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5503

            return self._parent._cast(
                _5503.RollingRingAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5505.RollingRingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5505

            return self._parent._cast(_5505.RollingRingMultibodyDynamicsAnalysis)

        @property
        def root_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5506.RootAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5506

            return self._parent._cast(_5506.RootAssemblyMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5509.ShaftHubConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5509

            return self._parent._cast(_5509.ShaftHubConnectionMultibodyDynamicsAnalysis)

        @property
        def shaft_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5510.ShaftMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(_5510.ShaftMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5513.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5513

            return self._parent._cast(
                _5513.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5515.SpiralBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5515

            return self._parent._cast(_5515.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5516.SpiralBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5516

            return self._parent._cast(_5516.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5519.SpringDamperHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5519

            return self._parent._cast(_5519.SpringDamperHalfMultibodyDynamicsAnalysis)

        @property
        def spring_damper_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5520.SpringDamperMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5520

            return self._parent._cast(_5520.SpringDamperMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5522.StraightBevelDiffGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5522

            return self._parent._cast(
                _5522.StraightBevelDiffGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5523.StraightBevelDiffGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5523

            return self._parent._cast(
                _5523.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5525.StraightBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5525

            return self._parent._cast(_5525.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5526.StraightBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5526

            return self._parent._cast(
                _5526.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5527.StraightBevelPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5527

            return self._parent._cast(
                _5527.StraightBevelPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5528.StraightBevelSunGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5528

            return self._parent._cast(
                _5528.StraightBevelSunGearMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5529.SynchroniserHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5529

            return self._parent._cast(_5529.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5530.SynchroniserMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5530

            return self._parent._cast(_5530.SynchroniserMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5531.SynchroniserPartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5531

            return self._parent._cast(_5531.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5532.SynchroniserSleeveMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5532

            return self._parent._cast(_5532.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def torque_converter_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5535.TorqueConverterMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5535

            return self._parent._cast(_5535.TorqueConverterMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5536.TorqueConverterPumpMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5536

            return self._parent._cast(
                _5536.TorqueConverterPumpMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5538.TorqueConverterTurbineMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5538

            return self._parent._cast(
                _5538.TorqueConverterTurbineMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5539.UnbalancedMassMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5539

            return self._parent._cast(_5539.UnbalancedMassMultibodyDynamicsAnalysis)

        @property
        def virtual_component_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5540.VirtualComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5540

            return self._parent._cast(_5540.VirtualComponentMultibodyDynamicsAnalysis)

        @property
        def worm_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5543.WormGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5543

            return self._parent._cast(_5543.WormGearMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5544.WormGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5544

            return self._parent._cast(_5544.WormGearSetMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5546.ZerolBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5546

            return self._parent._cast(_5546.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5547.ZerolBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5547

            return self._parent._cast(_5547.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "PartMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartMultibodyDynamicsAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def multibody_dynamics_analysis(self: Self) -> "_5489.MultibodyDynamicsAnalysis":
        """mastapy.system_model.analyses_and_results.mbd_analyses.MultibodyDynamicsAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MultibodyDynamicsAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def data_logger(self: Self) -> "_1588.DataLogger":
        """mastapy.math_utility.convergence.DataLogger

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DataLogger

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2268.MBDAnalysisViewable":
        """mastapy.system_model.drawing.MBDAnalysisViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(
        self: Self,
    ) -> "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis":
        return self._Cast_PartMultibodyDynamicsAnalysis(self)
