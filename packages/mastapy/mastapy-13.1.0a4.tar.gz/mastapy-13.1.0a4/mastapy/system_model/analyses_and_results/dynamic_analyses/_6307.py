"""AGMAGleasonConicalGearDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "AGMAGleasonConicalGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6314,
        _6317,
        _6318,
        _6319,
        _6367,
        _6404,
        _6410,
        _6413,
        _6416,
        _6417,
        _6431,
        _6363,
        _6382,
        _6328,
        _6384,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearDynamicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearDynamicAnalysis")


class AGMAGleasonConicalGearDynamicAnalysis(_6335.ConicalGearDynamicAnalysis):
    """AGMAGleasonConicalGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearDynamicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearDynamicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
            parent: "AGMAGleasonConicalGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_6335.ConicalGearDynamicAnalysis":
            return self._parent._cast(_6335.ConicalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_6363.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_6382.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_6328.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_6384.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_6314.BevelDifferentialGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314

            return self._parent._cast(_6314.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_6317.BevelDifferentialPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6317

            return self._parent._cast(_6317.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_6318.BevelDifferentialSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318

            return self._parent._cast(_6318.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_6319.BevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.BevelGearDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_6367.HypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6367

            return self._parent._cast(_6367.HypoidGearDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_6404.SpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6404

            return self._parent._cast(_6404.SpiralBevelGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_6410.StraightBevelDiffGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6410

            return self._parent._cast(_6410.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_6413.StraightBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6413

            return self._parent._cast(_6413.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_6416.StraightBevelPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6416

            return self._parent._cast(_6416.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_6417.StraightBevelSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6417

            return self._parent._cast(_6417.StraightBevelSunGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "_6431.ZerolBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6431

            return self._parent._cast(_6431.ZerolBevelGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "AGMAGleasonConicalGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2531.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis":
        return self._Cast_AGMAGleasonConicalGearDynamicAnalysis(self)
