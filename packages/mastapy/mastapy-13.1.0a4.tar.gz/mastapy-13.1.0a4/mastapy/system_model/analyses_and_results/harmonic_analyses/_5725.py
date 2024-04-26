"""BoltHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5731
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "BoltHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.static_loads import _6858
    from mastapy.system_model.analyses_and_results.system_deflections import _2733
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5814
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BoltHarmonicAnalysis",)


Self = TypeVar("Self", bound="BoltHarmonicAnalysis")


class BoltHarmonicAnalysis(_5731.ComponentHarmonicAnalysis):
    """BoltHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltHarmonicAnalysis")

    class _Cast_BoltHarmonicAnalysis:
        """Special nested class for casting BoltHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis",
            parent: "BoltHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def component_harmonic_analysis(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis",
        ) -> "_5731.ComponentHarmonicAnalysis":
            return self._parent._cast(_5731.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bolt_harmonic_analysis(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis",
        ) -> "BoltHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2460.Bolt":
        """mastapy.system_model.part_model.Bolt

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6858.BoltLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2733.BoltSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BoltSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis":
        return self._Cast_BoltHarmonicAnalysis(self)
