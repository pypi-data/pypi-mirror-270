"""ConceptGearHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6092,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "ConceptGearHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.static_loads import _6868
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6113,
        _6059,
        _6115,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="ConceptGearHarmonicAnalysisOfSingleExcitation")


class ConceptGearHarmonicAnalysisOfSingleExcitation(
    _6092.GearHarmonicAnalysisOfSingleExcitation
):
    """ConceptGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_ConceptGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConceptGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
            parent: "ConceptGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6092.GearHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6092.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6113.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6113,
            )

            return self._parent._cast(
                _6113.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6059.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6059,
            )

            return self._parent._cast(_6059.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(_6115.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ) -> "ConceptGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ConceptGearHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2539.ConceptGear":
        """mastapy.system_model.part_model.gears.ConceptGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6868.ConceptGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase

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
    ) -> "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation(self)
