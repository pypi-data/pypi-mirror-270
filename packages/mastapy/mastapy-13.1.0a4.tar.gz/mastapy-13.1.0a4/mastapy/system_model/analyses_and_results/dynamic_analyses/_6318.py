"""BevelDifferentialSunGearDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "BevelDifferentialSunGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
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
__all__ = ("BevelDifferentialSunGearDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearDynamicAnalysis")


class BevelDifferentialSunGearDynamicAnalysis(
    _6314.BevelDifferentialGearDynamicAnalysis
):
    """BevelDifferentialSunGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearDynamicAnalysis"
    )

    class _Cast_BevelDifferentialSunGearDynamicAnalysis:
        """Special nested class for casting BevelDifferentialSunGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis",
            parent: "BevelDifferentialSunGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis",
        ) -> "_6314.BevelDifferentialGearDynamicAnalysis":
            return self._parent._cast(_6314.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis",
        ) -> "_6319.BevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.BevelGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis",
        ) -> "_6307.AGMAGleasonConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis",
        ) -> "_6335.ConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.ConicalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis",
        ) -> "_6363.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis",
        ) -> "_6382.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis",
        ) -> "_6328.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis",
        ) -> "_6384.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis",
        ) -> "BevelDifferentialSunGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialSunGearDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2536.BevelDifferentialSunGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialSunGear

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
    ) -> "BevelDifferentialSunGearDynamicAnalysis._Cast_BevelDifferentialSunGearDynamicAnalysis":
        return self._Cast_BevelDifferentialSunGearDynamicAnalysis(self)
