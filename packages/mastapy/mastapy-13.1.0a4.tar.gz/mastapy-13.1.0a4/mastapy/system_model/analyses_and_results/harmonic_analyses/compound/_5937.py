"""ConicalGearCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5963
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "ConicalGearCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5738
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5909,
        _5916,
        _5919,
        _5920,
        _5921,
        _5967,
        _5971,
        _5974,
        _5977,
        _6004,
        _6010,
        _6013,
        _6016,
        _6017,
        _6031,
        _5982,
        _5930,
        _5984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearCompoundHarmonicAnalysis")


class ConicalGearCompoundHarmonicAnalysis(_5963.GearCompoundHarmonicAnalysis):
    """ConicalGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearCompoundHarmonicAnalysis")

    class _Cast_ConicalGearCompoundHarmonicAnalysis:
        """Special nested class for casting ConicalGearCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
            parent: "ConicalGearCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5963.GearCompoundHarmonicAnalysis":
            return self._parent._cast(_5963.GearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5982.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5982,
            )

            return self._parent._cast(_5982.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5930.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5984.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(_5984.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5909.AGMAGleasonConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5909,
            )

            return self._parent._cast(
                _5909.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5916.BevelDifferentialGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5916,
            )

            return self._parent._cast(
                _5916.BevelDifferentialGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5919.BevelDifferentialPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5919,
            )

            return self._parent._cast(
                _5919.BevelDifferentialPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5920.BevelDifferentialSunGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5920,
            )

            return self._parent._cast(
                _5920.BevelDifferentialSunGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5921.BevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5921,
            )

            return self._parent._cast(_5921.BevelGearCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5967.HypoidGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5967,
            )

            return self._parent._cast(_5967.HypoidGearCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5971.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5971,
            )

            return self._parent._cast(
                _5971.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5974.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5974,
            )

            return self._parent._cast(
                _5974.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_5977.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(
                _5977.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_6004.SpiralBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6004,
            )

            return self._parent._cast(_6004.SpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_6010.StraightBevelDiffGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6010,
            )

            return self._parent._cast(
                _6010.StraightBevelDiffGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_6013.StraightBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6013,
            )

            return self._parent._cast(_6013.StraightBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_6016.StraightBevelPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6016,
            )

            return self._parent._cast(
                _6016.StraightBevelPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_6017.StraightBevelSunGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6017,
            )

            return self._parent._cast(
                _6017.StraightBevelSunGearCompoundHarmonicAnalysis
            )

        @property
        def zerol_bevel_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "_6031.ZerolBevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6031,
            )

            return self._parent._cast(_6031.ZerolBevelGearCompoundHarmonicAnalysis)

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
        ) -> "ConicalGearCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self: Self) -> "List[ConicalGearCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.ConicalGearCompoundHarmonicAnalysis]

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
    ) -> "List[_5738.ConicalGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearHarmonicAnalysis]

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
    ) -> "List[_5738.ConicalGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearHarmonicAnalysis]

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
    ) -> (
        "ConicalGearCompoundHarmonicAnalysis._Cast_ConicalGearCompoundHarmonicAnalysis"
    ):
        return self._Cast_ConicalGearCompoundHarmonicAnalysis(self)
