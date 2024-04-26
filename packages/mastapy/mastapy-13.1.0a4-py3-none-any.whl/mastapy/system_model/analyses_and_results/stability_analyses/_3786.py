"""AbstractAssemblyStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3867
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "AbstractAssemblyStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3791,
        _3793,
        _3796,
        _3798,
        _3803,
        _3805,
        _3809,
        _3814,
        _3816,
        _3819,
        _3825,
        _3829,
        _3830,
        _3835,
        _3842,
        _3845,
        _3847,
        _3851,
        _3855,
        _3858,
        _3861,
        _3870,
        _3872,
        _3879,
        _3882,
        _3886,
        _3888,
        _3892,
        _3897,
        _3900,
        _3907,
        _3910,
        _3915,
        _3918,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyStabilityAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyStabilityAnalysis")


class AbstractAssemblyStabilityAnalysis(_3867.PartStabilityAnalysis):
    """AbstractAssemblyStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyStabilityAnalysis")

    class _Cast_AbstractAssemblyStabilityAnalysis:
        """Special nested class for casting AbstractAssemblyStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
            parent: "AbstractAssemblyStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def part_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3791.AGMAGleasonConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3791,
            )

            return self._parent._cast(_3791.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3793.AssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3793,
            )

            return self._parent._cast(_3793.AssemblyStabilityAnalysis)

        @property
        def belt_drive_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3796.BeltDriveStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.BeltDriveStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3798.BevelDifferentialGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(_3798.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3803.BevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3803,
            )

            return self._parent._cast(_3803.BevelGearSetStabilityAnalysis)

        @property
        def bolted_joint_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3805.BoltedJointStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3805,
            )

            return self._parent._cast(_3805.BoltedJointStabilityAnalysis)

        @property
        def clutch_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3809.ClutchStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.ClutchStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3814.ConceptCouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3814,
            )

            return self._parent._cast(_3814.ConceptCouplingStabilityAnalysis)

        @property
        def concept_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3816.ConceptGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3816,
            )

            return self._parent._cast(_3816.ConceptGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3819.ConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.ConicalGearSetStabilityAnalysis)

        @property
        def coupling_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3825.CouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.CouplingStabilityAnalysis)

        @property
        def cvt_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3829.CVTStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3829,
            )

            return self._parent._cast(_3829.CVTStabilityAnalysis)

        @property
        def cycloidal_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3830.CycloidalAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3830,
            )

            return self._parent._cast(_3830.CycloidalAssemblyStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3835.CylindricalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3835,
            )

            return self._parent._cast(_3835.CylindricalGearSetStabilityAnalysis)

        @property
        def face_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3842.FaceGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.FaceGearSetStabilityAnalysis)

        @property
        def flexible_pin_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3845.FlexiblePinAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3845,
            )

            return self._parent._cast(_3845.FlexiblePinAssemblyStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3847.GearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3847,
            )

            return self._parent._cast(_3847.GearSetStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3851.HypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3851,
            )

            return self._parent._cast(_3851.HypoidGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3855.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3855,
            )

            return self._parent._cast(
                _3855.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3858.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3858,
            )

            return self._parent._cast(
                _3858.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3861.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3861,
            )

            return self._parent._cast(
                _3861.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3870.PartToPartShearCouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3870,
            )

            return self._parent._cast(_3870.PartToPartShearCouplingStabilityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3872.PlanetaryGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3872,
            )

            return self._parent._cast(_3872.PlanetaryGearSetStabilityAnalysis)

        @property
        def rolling_ring_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3879.RollingRingAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3879,
            )

            return self._parent._cast(_3879.RollingRingAssemblyStabilityAnalysis)

        @property
        def root_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3882.RootAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3882,
            )

            return self._parent._cast(_3882.RootAssemblyStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3886.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3886,
            )

            return self._parent._cast(_3886.SpecialisedAssemblyStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3888.SpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3888,
            )

            return self._parent._cast(_3888.SpiralBevelGearSetStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3892.SpringDamperStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3892,
            )

            return self._parent._cast(_3892.SpringDamperStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3897.StraightBevelDiffGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3897,
            )

            return self._parent._cast(_3897.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3900.StraightBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3900,
            )

            return self._parent._cast(_3900.StraightBevelGearSetStabilityAnalysis)

        @property
        def synchroniser_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3907.SynchroniserStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3907,
            )

            return self._parent._cast(_3907.SynchroniserStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3910.TorqueConverterStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3910,
            )

            return self._parent._cast(_3910.TorqueConverterStabilityAnalysis)

        @property
        def worm_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3915.WormGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3915,
            )

            return self._parent._cast(_3915.WormGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "_3918.ZerolBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3918,
            )

            return self._parent._cast(_3918.ZerolBevelGearSetStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
        ) -> "AbstractAssemblyStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AbstractAssemblyStabilityAnalysis.TYPE"
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
    ) -> "AbstractAssemblyStabilityAnalysis._Cast_AbstractAssemblyStabilityAnalysis":
        return self._Cast_AbstractAssemblyStabilityAnalysis(self)
