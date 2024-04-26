"""AbstractShaftHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6036,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "AbstractShaftHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6079,
        _6131,
        _6059,
        _6115,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="AbstractShaftHarmonicAnalysisOfSingleExcitation")


class AbstractShaftHarmonicAnalysisOfSingleExcitation(
    _6036.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
):
    """AbstractShaftHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting AbstractShaftHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
            parent: "AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6036.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6036.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6059.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6059,
            )

            return self._parent._cast(_6059.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(_6115.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6079.CycloidalDiscHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6079,
            )

            return self._parent._cast(
                _6079.CycloidalDiscHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6131.ShaftHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6131,
            )

            return self._parent._cast(_6131.ShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "AbstractShaftHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "AbstractShaftHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2453.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

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
    ) -> "AbstractShaftHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation":
        return self._Cast_AbstractShaftHarmonicAnalysisOfSingleExcitation(self)
