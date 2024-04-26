"""RollingRingAssemblyHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6134,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "RollingRingAssemblyHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2617
    from mastapy.system_model.analyses_and_results.static_loads import _6972
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6034,
        _6115,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="RollingRingAssemblyHarmonicAnalysisOfSingleExcitation")


class RollingRingAssemblyHarmonicAnalysisOfSingleExcitation(
    _6134.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
):
    """RollingRingAssemblyHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingAssemblyHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_RollingRingAssemblyHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting RollingRingAssemblyHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "RollingRingAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RollingRingAssemblyHarmonicAnalysisOfSingleExcitation",
            parent: "RollingRingAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "RollingRingAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RollingRingAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6134.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6134.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "RollingRingAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RollingRingAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6034.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6034,
            )

            return self._parent._cast(
                _6034.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "RollingRingAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RollingRingAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(_6115.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RollingRingAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RollingRingAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RollingRingAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RollingRingAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RollingRingAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_harmonic_analysis_of_single_excitation(
            self: "RollingRingAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RollingRingAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "RollingRingAssemblyHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RollingRingAssemblyHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "RollingRingAssemblyHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2617.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6972.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

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
    ) -> "RollingRingAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RollingRingAssemblyHarmonicAnalysisOfSingleExcitation":
        return self._Cast_RollingRingAssemblyHarmonicAnalysisOfSingleExcitation(self)
