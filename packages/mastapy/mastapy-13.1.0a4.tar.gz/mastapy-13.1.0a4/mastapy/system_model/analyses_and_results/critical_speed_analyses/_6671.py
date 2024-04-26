"""SpiralBevelGearCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6585
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "SpiralBevelGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2561
    from mastapy.system_model.analyses_and_results.static_loads import _6980
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6573,
        _6601,
        _6630,
        _6649,
        _6594,
        _6651,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearCriticalSpeedAnalysis")


class SpiralBevelGearCriticalSpeedAnalysis(_6585.BevelGearCriticalSpeedAnalysis):
    """SpiralBevelGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearCriticalSpeedAnalysis")

    class _Cast_SpiralBevelGearCriticalSpeedAnalysis:
        """Special nested class for casting SpiralBevelGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
            parent: "SpiralBevelGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_critical_speed_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_6585.BevelGearCriticalSpeedAnalysis":
            return self._parent._cast(_6585.BevelGearCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_6573.AGMAGleasonConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6573,
            )

            return self._parent._cast(_6573.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_6601.ConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6601,
            )

            return self._parent._cast(_6601.ConicalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_6630.GearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6630,
            )

            return self._parent._cast(_6630.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_6649.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6649,
            )

            return self._parent._cast(_6649.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_6594.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6594,
            )

            return self._parent._cast(_6594.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_6651.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "SpiralBevelGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2561.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6980.SpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis":
        return self._Cast_SpiralBevelGearCriticalSpeedAnalysis(self)
