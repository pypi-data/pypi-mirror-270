"""ConicalGearCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6492
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ConicalGearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6438,
        _6445,
        _6448,
        _6449,
        _6450,
        _6496,
        _6500,
        _6503,
        _6506,
        _6533,
        _6539,
        _6542,
        _6545,
        _6546,
        _6560,
        _6511,
        _6459,
        _6513,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearCompoundDynamicAnalysis")


class ConicalGearCompoundDynamicAnalysis(_6492.GearCompoundDynamicAnalysis):
    """ConicalGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearCompoundDynamicAnalysis")

    class _Cast_ConicalGearCompoundDynamicAnalysis:
        """Special nested class for casting ConicalGearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
            parent: "ConicalGearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6492.GearCompoundDynamicAnalysis":
            return self._parent._cast(_6492.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6511.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6511,
            )

            return self._parent._cast(_6511.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6459.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6459,
            )

            return self._parent._cast(_6459.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6513.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6513,
            )

            return self._parent._cast(_6513.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6438.AGMAGleasonConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6438,
            )

            return self._parent._cast(
                _6438.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6445.BevelDifferentialGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6445,
            )

            return self._parent._cast(
                _6445.BevelDifferentialGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6448.BevelDifferentialPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6448,
            )

            return self._parent._cast(
                _6448.BevelDifferentialPlanetGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6449.BevelDifferentialSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6449,
            )

            return self._parent._cast(
                _6449.BevelDifferentialSunGearCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6450.BevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6450,
            )

            return self._parent._cast(_6450.BevelGearCompoundDynamicAnalysis)

        @property
        def hypoid_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6496.HypoidGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6496,
            )

            return self._parent._cast(_6496.HypoidGearCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6500.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6500,
            )

            return self._parent._cast(
                _6500.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6503.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6503,
            )

            return self._parent._cast(
                _6503.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6506.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(
                _6506.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6533.SpiralBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6533,
            )

            return self._parent._cast(_6533.SpiralBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6539.StraightBevelDiffGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6539,
            )

            return self._parent._cast(
                _6539.StraightBevelDiffGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6542.StraightBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6542,
            )

            return self._parent._cast(_6542.StraightBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6545.StraightBevelPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6545,
            )

            return self._parent._cast(
                _6545.StraightBevelPlanetGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6546.StraightBevelSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6546,
            )

            return self._parent._cast(_6546.StraightBevelSunGearCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6560.ZerolBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6560,
            )

            return self._parent._cast(_6560.ZerolBevelGearCompoundDynamicAnalysis)

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "ConicalGearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self: Self) -> "List[ConicalGearCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConicalGearCompoundDynamicAnalysis]

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
    ) -> "List[_6335.ConicalGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearDynamicAnalysis]

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
    ) -> "List[_6335.ConicalGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearDynamicAnalysis]

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
    ) -> "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis":
        return self._Cast_ConicalGearCompoundDynamicAnalysis(self)
