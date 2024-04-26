"""SynchroniserPartHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6072,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "SynchroniserPartHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2628
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6149,
        _6152,
        _6113,
        _6059,
        _6115,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="SynchroniserPartHarmonicAnalysisOfSingleExcitation")


class SynchroniserPartHarmonicAnalysisOfSingleExcitation(
    _6072.CouplingHalfHarmonicAnalysisOfSingleExcitation
):
    """SynchroniserPartHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting SynchroniserPartHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
            parent: "SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6072.CouplingHalfHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6072.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6113.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6113,
            )

            return self._parent._cast(
                _6113.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6059.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6059,
            )

            return self._parent._cast(_6059.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(_6115.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6149.SynchroniserHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6149,
            )

            return self._parent._cast(
                _6149.SynchroniserHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "_6152.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6152,
            )

            return self._parent._cast(
                _6152.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
        ) -> "SynchroniserPartHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "SynchroniserPartHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2628.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserPartHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation":
        return self._Cast_SynchroniserPartHarmonicAnalysisOfSingleExcitation(self)
