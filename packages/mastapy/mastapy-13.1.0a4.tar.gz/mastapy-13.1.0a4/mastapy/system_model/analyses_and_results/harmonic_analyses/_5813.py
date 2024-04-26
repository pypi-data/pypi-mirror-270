"""OilSealHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5742
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "OilSealHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2484
    from mastapy.system_model.analyses_and_results.static_loads import _6953
    from mastapy.system_model.analyses_and_results.system_deflections import _2807
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5812,
        _5731,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("OilSealHarmonicAnalysis",)


Self = TypeVar("Self", bound="OilSealHarmonicAnalysis")


class OilSealHarmonicAnalysis(_5742.ConnectorHarmonicAnalysis):
    """OilSealHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilSealHarmonicAnalysis")

    class _Cast_OilSealHarmonicAnalysis:
        """Special nested class for casting OilSealHarmonicAnalysis to subclasses."""

        def __init__(
            self: "OilSealHarmonicAnalysis._Cast_OilSealHarmonicAnalysis",
            parent: "OilSealHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def connector_harmonic_analysis(
            self: "OilSealHarmonicAnalysis._Cast_OilSealHarmonicAnalysis",
        ) -> "_5742.ConnectorHarmonicAnalysis":
            return self._parent._cast(_5742.ConnectorHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "OilSealHarmonicAnalysis._Cast_OilSealHarmonicAnalysis",
        ) -> "_5812.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "OilSealHarmonicAnalysis._Cast_OilSealHarmonicAnalysis",
        ) -> "_5731.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5731,
            )

            return self._parent._cast(_5731.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "OilSealHarmonicAnalysis._Cast_OilSealHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "OilSealHarmonicAnalysis._Cast_OilSealHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "OilSealHarmonicAnalysis._Cast_OilSealHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "OilSealHarmonicAnalysis._Cast_OilSealHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "OilSealHarmonicAnalysis._Cast_OilSealHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealHarmonicAnalysis._Cast_OilSealHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def oil_seal_harmonic_analysis(
            self: "OilSealHarmonicAnalysis._Cast_OilSealHarmonicAnalysis",
        ) -> "OilSealHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "OilSealHarmonicAnalysis._Cast_OilSealHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OilSealHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2484.OilSeal":
        """mastapy.system_model.part_model.OilSeal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6953.OilSealLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2807.OilSealSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.OilSealSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "OilSealHarmonicAnalysis._Cast_OilSealHarmonicAnalysis":
        return self._Cast_OilSealHarmonicAnalysis(self)
