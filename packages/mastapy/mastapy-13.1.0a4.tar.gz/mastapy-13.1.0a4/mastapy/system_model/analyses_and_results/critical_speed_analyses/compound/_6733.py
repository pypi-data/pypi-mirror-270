"""ConicalGearCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6759,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "ConicalGearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6601
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6705,
        _6712,
        _6715,
        _6716,
        _6717,
        _6763,
        _6767,
        _6770,
        _6773,
        _6800,
        _6806,
        _6809,
        _6812,
        _6813,
        _6827,
        _6778,
        _6726,
        _6780,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConicalGearCompoundCriticalSpeedAnalysis")


class ConicalGearCompoundCriticalSpeedAnalysis(_6759.GearCompoundCriticalSpeedAnalysis):
    """ConicalGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearCompoundCriticalSpeedAnalysis"
    )

    class _Cast_ConicalGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ConicalGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
            parent: "ConicalGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6759.GearCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6759.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6778.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6778,
            )

            return self._parent._cast(
                _6778.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6726.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6726,
            )

            return self._parent._cast(_6726.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6780.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(_6780.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6705.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6705,
            )

            return self._parent._cast(
                _6705.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6712.BevelDifferentialGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6712,
            )

            return self._parent._cast(
                _6712.BevelDifferentialGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6715.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6715,
            )

            return self._parent._cast(
                _6715.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6716.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6716,
            )

            return self._parent._cast(
                _6716.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6717.BevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6717,
            )

            return self._parent._cast(_6717.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6763.HypoidGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6763,
            )

            return self._parent._cast(_6763.HypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6767.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6767,
            )

            return self._parent._cast(
                _6767.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6770.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6770,
            )

            return self._parent._cast(
                _6770.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
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
        def spiral_bevel_gear_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6800.SpiralBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6800,
            )

            return self._parent._cast(
                _6800.SpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6806.StraightBevelDiffGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6806,
            )

            return self._parent._cast(
                _6806.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6809.StraightBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6809,
            )

            return self._parent._cast(
                _6809.StraightBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6812.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6812,
            )

            return self._parent._cast(
                _6812.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6813.StraightBevelSunGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6813,
            )

            return self._parent._cast(
                _6813.StraightBevelSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def zerol_bevel_gear_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "_6827.ZerolBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6827,
            )

            return self._parent._cast(_6827.ZerolBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "ConicalGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self: Self) -> "List[ConicalGearCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.ConicalGearCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6601.ConicalGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConicalGearCriticalSpeedAnalysis]

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
    ) -> "List[_6601.ConicalGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConicalGearCriticalSpeedAnalysis]

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
    ) -> "ConicalGearCompoundCriticalSpeedAnalysis._Cast_ConicalGearCompoundCriticalSpeedAnalysis":
        return self._Cast_ConicalGearCompoundCriticalSpeedAnalysis(self)
