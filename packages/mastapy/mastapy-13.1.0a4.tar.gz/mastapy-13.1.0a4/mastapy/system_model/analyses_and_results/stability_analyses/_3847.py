"""GearSetStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3886
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "GearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3848,
        _3846,
        _3791,
        _3798,
        _3803,
        _3816,
        _3819,
        _3835,
        _3842,
        _3851,
        _3855,
        _3858,
        _3861,
        _3872,
        _3888,
        _3897,
        _3900,
        _3915,
        _3918,
        _3786,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="GearSetStabilityAnalysis")


class GearSetStabilityAnalysis(_3886.SpecialisedAssemblyStabilityAnalysis):
    """GearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetStabilityAnalysis")

    class _Cast_GearSetStabilityAnalysis:
        """Special nested class for casting GearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
            parent: "GearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3886.SpecialisedAssemblyStabilityAnalysis":
            return self._parent._cast(_3886.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3786.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3791.AGMAGleasonConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3791,
            )

            return self._parent._cast(_3791.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3798.BevelDifferentialGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(_3798.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3803.BevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3803,
            )

            return self._parent._cast(_3803.BevelGearSetStabilityAnalysis)

        @property
        def concept_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3816.ConceptGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3816,
            )

            return self._parent._cast(_3816.ConceptGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3819.ConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.ConicalGearSetStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3835.CylindricalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3835,
            )

            return self._parent._cast(_3835.CylindricalGearSetStabilityAnalysis)

        @property
        def face_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3842.FaceGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.FaceGearSetStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3851.HypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3851,
            )

            return self._parent._cast(_3851.HypoidGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3855.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3855,
            )

            return self._parent._cast(
                _3855.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3858.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3858,
            )

            return self._parent._cast(
                _3858.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3861.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3861,
            )

            return self._parent._cast(
                _3861.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
            )

        @property
        def planetary_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3872.PlanetaryGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3872,
            )

            return self._parent._cast(_3872.PlanetaryGearSetStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3888.SpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3888,
            )

            return self._parent._cast(_3888.SpiralBevelGearSetStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3897.StraightBevelDiffGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3897,
            )

            return self._parent._cast(_3897.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3900.StraightBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3900,
            )

            return self._parent._cast(_3900.StraightBevelGearSetStabilityAnalysis)

        @property
        def worm_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3915.WormGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3915,
            )

            return self._parent._cast(_3915.WormGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "_3918.ZerolBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3918,
            )

            return self._parent._cast(_3918.ZerolBevelGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis",
        ) -> "GearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2550.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_stability_analysis(self: Self) -> "List[_3848.GearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.GearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_stability_analysis(
        self: Self,
    ) -> "List[_3846.GearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.GearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetStabilityAnalysis._Cast_GearSetStabilityAnalysis":
        return self._Cast_GearSetStabilityAnalysis(self)
