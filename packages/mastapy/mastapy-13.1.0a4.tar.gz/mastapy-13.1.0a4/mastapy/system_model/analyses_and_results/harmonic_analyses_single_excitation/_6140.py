"""SpringDamperHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6073,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "SpringDamperHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2623
    from mastapy.system_model.analyses_and_results.static_loads import _6985
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6134,
        _6034,
        _6115,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="SpringDamperHarmonicAnalysisOfSingleExcitation")


class SpringDamperHarmonicAnalysisOfSingleExcitation(
    _6073.CouplingHarmonicAnalysisOfSingleExcitation
):
    """SpringDamperHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_SpringDamperHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting SpringDamperHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "SpringDamperHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperHarmonicAnalysisOfSingleExcitation",
            parent: "SpringDamperHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_harmonic_analysis_of_single_excitation(
            self: "SpringDamperHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperHarmonicAnalysisOfSingleExcitation",
        ) -> "_6073.CouplingHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6073.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "SpringDamperHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperHarmonicAnalysisOfSingleExcitation",
        ) -> "_6134.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6134,
            )

            return self._parent._cast(
                _6134.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "SpringDamperHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperHarmonicAnalysisOfSingleExcitation",
        ) -> "_6034.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6034,
            )

            return self._parent._cast(
                _6034.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "SpringDamperHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(_6115.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperHarmonicAnalysisOfSingleExcitation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperHarmonicAnalysisOfSingleExcitation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperHarmonicAnalysisOfSingleExcitation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(
            self: "SpringDamperHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperHarmonicAnalysisOfSingleExcitation",
        ) -> "SpringDamperHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "SpringDamperHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "SpringDamperHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2623.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6985.SpringDamperLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperHarmonicAnalysisOfSingleExcitation._Cast_SpringDamperHarmonicAnalysisOfSingleExcitation":
        return self._Cast_SpringDamperHarmonicAnalysisOfSingleExcitation(self)
