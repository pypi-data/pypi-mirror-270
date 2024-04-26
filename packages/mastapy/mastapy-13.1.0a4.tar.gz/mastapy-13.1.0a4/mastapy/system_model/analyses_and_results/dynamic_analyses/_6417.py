"""StraightBevelSunGearDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6410
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "StraightBevelSunGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2568
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6319,
        _6307,
        _6335,
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
__all__ = ("StraightBevelSunGearDynamicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelSunGearDynamicAnalysis")


class StraightBevelSunGearDynamicAnalysis(_6410.StraightBevelDiffGearDynamicAnalysis):
    """StraightBevelSunGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelSunGearDynamicAnalysis")

    class _Cast_StraightBevelSunGearDynamicAnalysis:
        """Special nested class for casting StraightBevelSunGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
            parent: "StraightBevelSunGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_6410.StraightBevelDiffGearDynamicAnalysis":
            return self._parent._cast(_6410.StraightBevelDiffGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_6319.BevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.BevelGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_6307.AGMAGleasonConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_6335.ConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.ConicalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_6363.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_6382.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_6328.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_6384.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "StraightBevelSunGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelSunGearDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2568.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

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
    ) -> (
        "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis"
    ):
        return self._Cast_StraightBevelSunGearDynamicAnalysis(self)
