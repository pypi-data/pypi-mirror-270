"""BevelDifferentialSunGearCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6712,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6584
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6717,
        _6705,
        _6733,
        _6759,
        _6778,
        _6726,
        _6780,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearCompoundCriticalSpeedAnalysis")


class BevelDifferentialSunGearCompoundCriticalSpeedAnalysis(
    _6712.BevelDifferentialGearCompoundCriticalSpeedAnalysis
):
    """BevelDifferentialSunGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis"
    )

    class _Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting BevelDifferentialSunGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
            parent: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6712.BevelDifferentialGearCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6712.BevelDifferentialGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6717.BevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6717,
            )

            return self._parent._cast(_6717.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6705.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6705,
            )

            return self._parent._cast(
                _6705.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6733.ConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6733,
            )

            return self._parent._cast(_6733.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6759.GearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6759,
            )

            return self._parent._cast(_6759.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6778.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6778,
            )

            return self._parent._cast(
                _6778.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6726.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6726,
            )

            return self._parent._cast(_6726.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_6780.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(_6780.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
        ) -> "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6584.BevelDifferentialSunGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelDifferentialSunGearCriticalSpeedAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6584.BevelDifferentialSunGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelDifferentialSunGearCriticalSpeedAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis":
        return self._Cast_BevelDifferentialSunGearCompoundCriticalSpeedAnalysis(self)
