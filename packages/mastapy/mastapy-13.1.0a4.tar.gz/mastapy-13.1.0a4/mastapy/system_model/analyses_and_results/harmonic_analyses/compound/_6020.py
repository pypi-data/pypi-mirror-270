"""SynchroniserPartCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5944
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "SynchroniserPartCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5855
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _6019,
        _6021,
        _5982,
        _5930,
        _5984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartCompoundHarmonicAnalysis")


class SynchroniserPartCompoundHarmonicAnalysis(
    _5944.CouplingHalfCompoundHarmonicAnalysis
):
    """SynchroniserPartCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartCompoundHarmonicAnalysis"
    )

    class _Cast_SynchroniserPartCompoundHarmonicAnalysis:
        """Special nested class for casting SynchroniserPartCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
            parent: "SynchroniserPartCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_5944.CouplingHalfCompoundHarmonicAnalysis":
            return self._parent._cast(_5944.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_5982.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5982,
            )

            return self._parent._cast(_5982.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_5930.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_5984.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(_5984.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_harmonic_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_6019.SynchroniserHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6019,
            )

            return self._parent._cast(_6019.SynchroniserHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "_6021.SynchroniserSleeveCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6021,
            )

            return self._parent._cast(_6021.SynchroniserSleeveCompoundHarmonicAnalysis)

        @property
        def synchroniser_part_compound_harmonic_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
        ) -> "SynchroniserPartCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserPartCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5855.SynchroniserPartHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.SynchroniserPartHarmonicAnalysis]

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
    ) -> "List[_5855.SynchroniserPartHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.SynchroniserPartHarmonicAnalysis]

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
    ) -> "SynchroniserPartCompoundHarmonicAnalysis._Cast_SynchroniserPartCompoundHarmonicAnalysis":
        return self._Cast_SynchroniserPartCompoundHarmonicAnalysis(self)
