"""BevelDifferentialPlanetGearCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5916
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5719
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5921,
        _5909,
        _5937,
        _5963,
        _5982,
        _5930,
        _5984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearCompoundHarmonicAnalysis")


class BevelDifferentialPlanetGearCompoundHarmonicAnalysis(
    _5916.BevelDifferentialGearCompoundHarmonicAnalysis
):
    """BevelDifferentialPlanetGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis"
    )

    class _Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
            parent: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ) -> "_5916.BevelDifferentialGearCompoundHarmonicAnalysis":
            return self._parent._cast(
                _5916.BevelDifferentialGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ) -> "_5921.BevelGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5921,
            )

            return self._parent._cast(_5921.BevelGearCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ) -> "_5909.AGMAGleasonConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5909,
            )

            return self._parent._cast(
                _5909.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ) -> "_5937.ConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5937,
            )

            return self._parent._cast(_5937.ConicalGearCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ) -> "_5963.GearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5963,
            )

            return self._parent._cast(_5963.GearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ) -> "_5982.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5982,
            )

            return self._parent._cast(_5982.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ) -> "_5930.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ) -> "_5984.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(_5984.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ) -> "BevelDifferentialPlanetGearCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
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
        instance_to_wrap: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5719.BevelDifferentialPlanetGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialPlanetGearHarmonicAnalysis]

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
    ) -> "List[_5719.BevelDifferentialPlanetGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialPlanetGearHarmonicAnalysis]

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
    ) -> "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis":
        return self._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis(self)
