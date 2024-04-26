"""GearCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6649
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "GearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6573,
        _6580,
        _6583,
        _6584,
        _6585,
        _6598,
        _6601,
        _6619,
        _6622,
        _6625,
        _6634,
        _6638,
        _6641,
        _6644,
        _6671,
        _6677,
        _6680,
        _6683,
        _6684,
        _6695,
        _6698,
        _6594,
        _6651,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="GearCriticalSpeedAnalysis")


class GearCriticalSpeedAnalysis(_6649.MountableComponentCriticalSpeedAnalysis):
    """GearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCriticalSpeedAnalysis")

    class _Cast_GearCriticalSpeedAnalysis:
        """Special nested class for casting GearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
            parent: "GearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6649.MountableComponentCriticalSpeedAnalysis":
            return self._parent._cast(_6649.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6594.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6594,
            )

            return self._parent._cast(_6594.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6651.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6573.AGMAGleasonConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6573,
            )

            return self._parent._cast(_6573.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6580.BevelDifferentialGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6580,
            )

            return self._parent._cast(_6580.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6583.BevelDifferentialPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6583,
            )

            return self._parent._cast(
                _6583.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6584.BevelDifferentialSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6584,
            )

            return self._parent._cast(
                _6584.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6585.BevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6585,
            )

            return self._parent._cast(_6585.BevelGearCriticalSpeedAnalysis)

        @property
        def concept_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6598.ConceptGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6598,
            )

            return self._parent._cast(_6598.ConceptGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6601.ConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6601,
            )

            return self._parent._cast(_6601.ConicalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6619.CylindricalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(_6619.CylindricalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6622.CylindricalPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.CylindricalPlanetGearCriticalSpeedAnalysis)

        @property
        def face_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6625.FaceGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.FaceGearCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6634.HypoidGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6634,
            )

            return self._parent._cast(_6634.HypoidGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6638.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6638,
            )

            return self._parent._cast(
                _6638.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6641.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6641,
            )

            return self._parent._cast(
                _6641.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6644.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(
                _6644.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6671.SpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6671,
            )

            return self._parent._cast(_6671.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6677.StraightBevelDiffGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6677,
            )

            return self._parent._cast(_6677.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6680.StraightBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6680,
            )

            return self._parent._cast(_6680.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6683.StraightBevelPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6683,
            )

            return self._parent._cast(
                _6683.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6684.StraightBevelSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6684,
            )

            return self._parent._cast(_6684.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def worm_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6695.WormGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6695,
            )

            return self._parent._cast(_6695.WormGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "_6698.ZerolBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6698,
            )

            return self._parent._cast(_6698.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "GearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearCriticalSpeedAnalysis.TYPE"):
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
    def cast_to(
        self: Self,
    ) -> "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis":
        return self._Cast_GearCriticalSpeedAnalysis(self)
