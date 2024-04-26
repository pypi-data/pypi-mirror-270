"""RingPinsCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6242,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "RingPinsCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2588
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6125,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6190,
        _6244,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="RingPinsCompoundHarmonicAnalysisOfSingleExcitation")


class RingPinsCompoundHarmonicAnalysisOfSingleExcitation(
    _6242.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
):
    """RingPinsCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _RING_PINS_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsCompoundHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_RingPinsCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting RingPinsCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "RingPinsCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "RingPinsCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "RingPinsCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6242.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6242.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "RingPinsCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6190.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6190,
            )

            return self._parent._cast(
                _6190.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "RingPinsCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6244.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6244,
            )

            return self._parent._cast(
                _6244.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "RingPinsCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def ring_pins_compound_harmonic_analysis_of_single_excitation(
            self: "RingPinsCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "RingPinsCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "RingPinsCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "RingPinsCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2588.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

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
    ) -> "List[_6125.RingPinsHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.RingPinsHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6125.RingPinsHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.RingPinsHarmonicAnalysisOfSingleExcitation]

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
    ) -> "RingPinsCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_RingPinsCompoundHarmonicAnalysisOfSingleExcitation(self)
