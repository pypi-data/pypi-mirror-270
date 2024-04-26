"""BevelDifferentialGearCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6717,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "BevelDifferentialGearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6580
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6715,
        _6716,
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
__all__ = ("BevelDifferentialGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearCompoundCriticalSpeedAnalysis")


class BevelDifferentialGearCompoundCriticalSpeedAnalysis(
    _6717.BevelGearCompoundCriticalSpeedAnalysis
):
    """BevelDifferentialGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis"
    )

    class _Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting BevelDifferentialGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
            parent: "BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ) -> "_6717.BevelGearCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6717.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ) -> "_6705.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6705,
            )

            return self._parent._cast(
                _6705.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ) -> "_6733.ConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6733,
            )

            return self._parent._cast(_6733.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ) -> "_6759.GearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6759,
            )

            return self._parent._cast(_6759.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ) -> "_6778.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6778,
            )

            return self._parent._cast(
                _6778.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ) -> "_6726.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6726,
            )

            return self._parent._cast(_6726.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ) -> "_6780.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(_6780.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ) -> "_6715.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6715,
            )

            return self._parent._cast(
                _6715.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ) -> "_6716.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6716,
            )

            return self._parent._cast(
                _6716.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
        ) -> "BevelDifferentialGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "BevelDifferentialGearCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6580.BevelDifferentialGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelDifferentialGearCriticalSpeedAnalysis]

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
    ) -> "List[_6580.BevelDifferentialGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelDifferentialGearCriticalSpeedAnalysis]

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
    ) -> "BevelDifferentialGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis":
        return self._Cast_BevelDifferentialGearCompoundCriticalSpeedAnalysis(self)
