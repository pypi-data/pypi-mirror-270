"""KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6733,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6638
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6770,
        _6773,
        _6759,
        _6778,
        _6726,
        _6780,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis"
)


class KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis(
    _6733.ConicalGearCompoundCriticalSpeedAnalysis
):
    """KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6733.ConicalGearCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6733.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6759.GearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6759,
            )

            return self._parent._cast(_6759.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6778.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6778,
            )

            return self._parent._cast(
                _6778.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6726.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6726,
            )

            return self._parent._cast(_6726.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6780.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(_6780.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6770.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6770,
            )

            return self._parent._cast(
                _6770.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
        ) -> (
            "_6773.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6638.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6638.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis(
                self
            )
        )
