"""SynchroniserSleeveCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _6020
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "SynchroniserSleeveCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2629
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5856
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5944,
        _5982,
        _5930,
        _5984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="SynchroniserSleeveCompoundHarmonicAnalysis")


class SynchroniserSleeveCompoundHarmonicAnalysis(
    _6020.SynchroniserPartCompoundHarmonicAnalysis
):
    """SynchroniserSleeveCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSleeveCompoundHarmonicAnalysis"
    )

    class _Cast_SynchroniserSleeveCompoundHarmonicAnalysis:
        """Special nested class for casting SynchroniserSleeveCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserSleeveCompoundHarmonicAnalysis._Cast_SynchroniserSleeveCompoundHarmonicAnalysis",
            parent: "SynchroniserSleeveCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_harmonic_analysis(
            self: "SynchroniserSleeveCompoundHarmonicAnalysis._Cast_SynchroniserSleeveCompoundHarmonicAnalysis",
        ) -> "_6020.SynchroniserPartCompoundHarmonicAnalysis":
            return self._parent._cast(_6020.SynchroniserPartCompoundHarmonicAnalysis)

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "SynchroniserSleeveCompoundHarmonicAnalysis._Cast_SynchroniserSleeveCompoundHarmonicAnalysis",
        ) -> "_5944.CouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5944,
            )

            return self._parent._cast(_5944.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "SynchroniserSleeveCompoundHarmonicAnalysis._Cast_SynchroniserSleeveCompoundHarmonicAnalysis",
        ) -> "_5982.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5982,
            )

            return self._parent._cast(_5982.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "SynchroniserSleeveCompoundHarmonicAnalysis._Cast_SynchroniserSleeveCompoundHarmonicAnalysis",
        ) -> "_5930.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "SynchroniserSleeveCompoundHarmonicAnalysis._Cast_SynchroniserSleeveCompoundHarmonicAnalysis",
        ) -> "_5984.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(_5984.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserSleeveCompoundHarmonicAnalysis._Cast_SynchroniserSleeveCompoundHarmonicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserSleeveCompoundHarmonicAnalysis._Cast_SynchroniserSleeveCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveCompoundHarmonicAnalysis._Cast_SynchroniserSleeveCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis(
            self: "SynchroniserSleeveCompoundHarmonicAnalysis._Cast_SynchroniserSleeveCompoundHarmonicAnalysis",
        ) -> "SynchroniserSleeveCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveCompoundHarmonicAnalysis._Cast_SynchroniserSleeveCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserSleeveCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2629.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

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
    ) -> "List[_5856.SynchroniserSleeveHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.SynchroniserSleeveHarmonicAnalysis]

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
    ) -> "List[_5856.SynchroniserSleeveHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.SynchroniserSleeveHarmonicAnalysis]

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
    ) -> "SynchroniserSleeveCompoundHarmonicAnalysis._Cast_SynchroniserSleeveCompoundHarmonicAnalysis":
        return self._Cast_SynchroniserSleeveCompoundHarmonicAnalysis(self)
