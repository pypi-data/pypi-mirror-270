"""CVTPulleyHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5824
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CVTPulleyHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.system_deflections import _2756
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5744,
        _5812,
        _5731,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyHarmonicAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyHarmonicAnalysis")


class CVTPulleyHarmonicAnalysis(_5824.PulleyHarmonicAnalysis):
    """CVTPulleyHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyHarmonicAnalysis")

    class _Cast_CVTPulleyHarmonicAnalysis:
        """Special nested class for casting CVTPulleyHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
            parent: "CVTPulleyHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_harmonic_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_5824.PulleyHarmonicAnalysis":
            return self._parent._cast(_5824.PulleyHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_5744.CouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5744,
            )

            return self._parent._cast(_5744.CouplingHalfHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_5812.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_5731.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5731,
            )

            return self._parent._cast(_5731.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis",
        ) -> "CVTPulleyHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2756.CVTPulleySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CVTPulleySystemDeflection

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
    ) -> "CVTPulleyHarmonicAnalysis._Cast_CVTPulleyHarmonicAnalysis":
        return self._Cast_CVTPulleyHarmonicAnalysis(self)
