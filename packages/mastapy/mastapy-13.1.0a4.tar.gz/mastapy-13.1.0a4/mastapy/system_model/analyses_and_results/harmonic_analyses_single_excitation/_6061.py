"""ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6072,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2600
    from mastapy.system_model.analyses_and_results.static_loads import _6866
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6113,
        _6059,
        _6115,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation")


class ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation(
    _6072.CouplingHalfHarmonicAnalysisOfSingleExcitation
):
    """ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
            parent: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6072.CouplingHalfHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6072.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6113.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6113,
            )

            return self._parent._cast(
                _6113.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6059.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6059,
            )

            return self._parent._cast(_6059.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(_6115.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
        ) -> "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2600.ConceptCouplingHalf":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6866.ConceptCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation(self)
