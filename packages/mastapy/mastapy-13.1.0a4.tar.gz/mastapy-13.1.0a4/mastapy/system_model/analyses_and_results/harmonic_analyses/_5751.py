"""CycloidalDiscHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5706
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CycloidalDiscHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2587
    from mastapy.system_model.analyses_and_results.static_loads import _6886
    from mastapy.system_model.analyses_and_results.system_deflections import _2761
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5707,
        _5731,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscHarmonicAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscHarmonicAnalysis")


class CycloidalDiscHarmonicAnalysis(_5706.AbstractShaftHarmonicAnalysis):
    """CycloidalDiscHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscHarmonicAnalysis")

    class _Cast_CycloidalDiscHarmonicAnalysis:
        """Special nested class for casting CycloidalDiscHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscHarmonicAnalysis._Cast_CycloidalDiscHarmonicAnalysis",
            parent: "CycloidalDiscHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_harmonic_analysis(
            self: "CycloidalDiscHarmonicAnalysis._Cast_CycloidalDiscHarmonicAnalysis",
        ) -> "_5706.AbstractShaftHarmonicAnalysis":
            return self._parent._cast(_5706.AbstractShaftHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_harmonic_analysis(
            self: "CycloidalDiscHarmonicAnalysis._Cast_CycloidalDiscHarmonicAnalysis",
        ) -> "_5707.AbstractShaftOrHousingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5707,
            )

            return self._parent._cast(_5707.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "CycloidalDiscHarmonicAnalysis._Cast_CycloidalDiscHarmonicAnalysis",
        ) -> "_5731.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5731,
            )

            return self._parent._cast(_5731.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "CycloidalDiscHarmonicAnalysis._Cast_CycloidalDiscHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscHarmonicAnalysis._Cast_CycloidalDiscHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscHarmonicAnalysis._Cast_CycloidalDiscHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscHarmonicAnalysis._Cast_CycloidalDiscHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscHarmonicAnalysis._Cast_CycloidalDiscHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscHarmonicAnalysis._Cast_CycloidalDiscHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis(
            self: "CycloidalDiscHarmonicAnalysis._Cast_CycloidalDiscHarmonicAnalysis",
        ) -> "CycloidalDiscHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscHarmonicAnalysis._Cast_CycloidalDiscHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2587.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6886.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2761.CycloidalDiscSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscHarmonicAnalysis._Cast_CycloidalDiscHarmonicAnalysis":
        return self._Cast_CycloidalDiscHarmonicAnalysis(self)
