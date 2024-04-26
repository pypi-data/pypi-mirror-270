"""TorqueConverterHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5745
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "TorqueConverterHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2630
    from mastapy.system_model.analyses_and_results.static_loads import _7000
    from mastapy.system_model.analyses_and_results.system_deflections import _2853
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5836,
        _5704,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterHarmonicAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterHarmonicAnalysis")


class TorqueConverterHarmonicAnalysis(_5745.CouplingHarmonicAnalysis):
    """TorqueConverterHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterHarmonicAnalysis")

    class _Cast_TorqueConverterHarmonicAnalysis:
        """Special nested class for casting TorqueConverterHarmonicAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterHarmonicAnalysis._Cast_TorqueConverterHarmonicAnalysis",
            parent: "TorqueConverterHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_harmonic_analysis(
            self: "TorqueConverterHarmonicAnalysis._Cast_TorqueConverterHarmonicAnalysis",
        ) -> "_5745.CouplingHarmonicAnalysis":
            return self._parent._cast(_5745.CouplingHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "TorqueConverterHarmonicAnalysis._Cast_TorqueConverterHarmonicAnalysis",
        ) -> "_5836.SpecialisedAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5836,
            )

            return self._parent._cast(_5836.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "TorqueConverterHarmonicAnalysis._Cast_TorqueConverterHarmonicAnalysis",
        ) -> "_5704.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "TorqueConverterHarmonicAnalysis._Cast_TorqueConverterHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterHarmonicAnalysis._Cast_TorqueConverterHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterHarmonicAnalysis._Cast_TorqueConverterHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterHarmonicAnalysis._Cast_TorqueConverterHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterHarmonicAnalysis._Cast_TorqueConverterHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterHarmonicAnalysis._Cast_TorqueConverterHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def torque_converter_harmonic_analysis(
            self: "TorqueConverterHarmonicAnalysis._Cast_TorqueConverterHarmonicAnalysis",
        ) -> "TorqueConverterHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterHarmonicAnalysis._Cast_TorqueConverterHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2630.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_7000.TorqueConverterLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2853.TorqueConverterSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterSystemDeflection

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
    ) -> "TorqueConverterHarmonicAnalysis._Cast_TorqueConverterHarmonicAnalysis":
        return self._Cast_TorqueConverterHarmonicAnalysis(self)
