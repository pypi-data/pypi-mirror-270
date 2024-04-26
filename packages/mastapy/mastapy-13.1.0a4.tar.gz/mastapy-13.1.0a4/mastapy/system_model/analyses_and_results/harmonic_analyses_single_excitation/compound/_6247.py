"""PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6204,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6117,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6242,
        _6190,
        _6244,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self",
    bound="PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
)


class PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation(
    _6204.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
):
    """PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6204.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6204.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6242.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6242,
            )

            return self._parent._cast(
                _6242.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6190.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6190,
            )

            return self._parent._cast(
                _6190.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6244.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6244,
            )

            return self._parent._cast(
                _6244.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

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
    ) -> "List[_6117.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6117.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation]

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
    ) -> "PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
