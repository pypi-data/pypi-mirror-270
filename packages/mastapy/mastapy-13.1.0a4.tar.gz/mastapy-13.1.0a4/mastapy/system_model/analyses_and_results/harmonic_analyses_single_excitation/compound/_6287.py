"""VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6242,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6158,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6240,
        _6241,
        _6251,
        _6252,
        _6286,
        _6190,
        _6244,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation"
)


class VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation(
    _6242.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
):
    """VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6242.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6242.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6190.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6190,
            )

            return self._parent._cast(
                _6190.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6244.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6244,
            )

            return self._parent._cast(
                _6244.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def mass_disc_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6240.MassDiscCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6240,
            )

            return self._parent._cast(
                _6240.MassDiscCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def measurement_component_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6241.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6241,
            )

            return self._parent._cast(
                _6241.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6251.PointLoadCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6251,
            )

            return self._parent._cast(
                _6251.PointLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def power_load_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6252.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6252,
            )

            return self._parent._cast(
                _6252.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6286.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6286,
            )

            return self._parent._cast(
                _6286.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6158.VirtualComponentHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.VirtualComponentHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6158.VirtualComponentHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.VirtualComponentHarmonicAnalysisOfSingleExcitation]

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
    ) -> "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
