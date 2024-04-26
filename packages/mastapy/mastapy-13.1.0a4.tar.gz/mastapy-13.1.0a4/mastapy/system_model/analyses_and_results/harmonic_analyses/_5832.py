"""ShaftHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5706
from mastapy.system_model.analyses_and_results import _2679
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ShaftHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2500
    from mastapy.system_model.analyses_and_results.static_loads import _6977
    from mastapy.system_model.analyses_and_results.modal_analyses import _4702
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5794,
        _5707,
        _5731,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2827
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHarmonicAnalysis",)


Self = TypeVar("Self", bound="ShaftHarmonicAnalysis")


class ShaftHarmonicAnalysis(
    _5706.AbstractShaftHarmonicAnalysis, _2679.IHaveShaftHarmonicResults
):
    """ShaftHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftHarmonicAnalysis")

    class _Cast_ShaftHarmonicAnalysis:
        """Special nested class for casting ShaftHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
            parent: "ShaftHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_harmonic_analysis(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_5706.AbstractShaftHarmonicAnalysis":
            return self._parent._cast(_5706.AbstractShaftHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_harmonic_analysis(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_5707.AbstractShaftOrHousingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5707,
            )

            return self._parent._cast(_5707.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_5731.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5731,
            )

            return self._parent._cast(_5731.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def shaft_harmonic_analysis(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis",
        ) -> "ShaftHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2500.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6977.ShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def coupled_modal_analysis(self: Self) -> "_4702.ShaftModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ShaftModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def export(self: Self) -> "_5794.HarmonicAnalysisShaftExportOptions":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisShaftExportOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Export

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2827.ShaftSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ShaftHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ShaftHarmonicAnalysis._Cast_ShaftHarmonicAnalysis":
        return self._Cast_ShaftHarmonicAnalysis(self)
