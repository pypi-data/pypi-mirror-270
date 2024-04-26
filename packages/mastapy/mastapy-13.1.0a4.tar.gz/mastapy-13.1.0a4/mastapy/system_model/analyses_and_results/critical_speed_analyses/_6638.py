"""KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6641,
        _6644,
        _6630,
        _6649,
        _6594,
        _6651,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis")


class KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis(
    _6601.ConicalGearCriticalSpeedAnalysis
):
    """KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ) -> "_6601.ConicalGearCriticalSpeedAnalysis":
            return self._parent._cast(_6601.ConicalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ) -> "_6630.GearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6630,
            )

            return self._parent._cast(_6630.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ) -> "_6649.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6649,
            )

            return self._parent._cast(_6649.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ) -> "_6594.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6594,
            )

            return self._parent._cast(_6594.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ) -> "_6651.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ) -> "_6641.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6641,
            )

            return self._parent._cast(
                _6641.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ) -> "_6644.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(
                _6644.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2554.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

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
    ) -> "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis(self)
