"""GearStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3865
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "GearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3792,
        _3799,
        _3800,
        _3801,
        _3804,
        _3817,
        _3820,
        _3836,
        _3837,
        _3843,
        _3852,
        _3856,
        _3859,
        _3862,
        _3889,
        _3898,
        _3901,
        _3902,
        _3903,
        _3916,
        _3919,
        _3811,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearStabilityAnalysis",)


Self = TypeVar("Self", bound="GearStabilityAnalysis")


class GearStabilityAnalysis(_3865.MountableComponentStabilityAnalysis):
    """GearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearStabilityAnalysis")

    class _Cast_GearStabilityAnalysis:
        """Special nested class for casting GearStabilityAnalysis to subclasses."""

        def __init__(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
            parent: "GearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3865.MountableComponentStabilityAnalysis":
            return self._parent._cast(_3865.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3811.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3792.AGMAGleasonConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3792,
            )

            return self._parent._cast(_3792.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3799.BevelDifferentialGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3799,
            )

            return self._parent._cast(_3799.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3800.BevelDifferentialPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3800,
            )

            return self._parent._cast(
                _3800.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3801.BevelDifferentialSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3801,
            )

            return self._parent._cast(_3801.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3804.BevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3804,
            )

            return self._parent._cast(_3804.BevelGearStabilityAnalysis)

        @property
        def concept_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3817.ConceptGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3817,
            )

            return self._parent._cast(_3817.ConceptGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3820.ConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3820,
            )

            return self._parent._cast(_3820.ConicalGearStabilityAnalysis)

        @property
        def cylindrical_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3836.CylindricalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3836,
            )

            return self._parent._cast(_3836.CylindricalGearStabilityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3837.CylindricalPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3837,
            )

            return self._parent._cast(_3837.CylindricalPlanetGearStabilityAnalysis)

        @property
        def face_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3843.FaceGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3843,
            )

            return self._parent._cast(_3843.FaceGearStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3852.HypoidGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.HypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3856.KlingelnbergCycloPalloidConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3856,
            )

            return self._parent._cast(
                _3856.KlingelnbergCycloPalloidConicalGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3859.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3859,
            )

            return self._parent._cast(
                _3859.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3862.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3862,
            )

            return self._parent._cast(
                _3862.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3889.SpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3889,
            )

            return self._parent._cast(_3889.SpiralBevelGearStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3898.StraightBevelDiffGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3898,
            )

            return self._parent._cast(_3898.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3901.StraightBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3901,
            )

            return self._parent._cast(_3901.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3902.StraightBevelPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3902,
            )

            return self._parent._cast(_3902.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3903.StraightBevelSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3903,
            )

            return self._parent._cast(_3903.StraightBevelSunGearStabilityAnalysis)

        @property
        def worm_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3916.WormGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3916,
            )

            return self._parent._cast(_3916.WormGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "_3919.ZerolBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3919,
            )

            return self._parent._cast(_3919.ZerolBevelGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis",
        ) -> "GearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "GearStabilityAnalysis._Cast_GearStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(self: Self) -> "GearStabilityAnalysis._Cast_GearStabilityAnalysis":
        return self._Cast_GearStabilityAnalysis(self)
