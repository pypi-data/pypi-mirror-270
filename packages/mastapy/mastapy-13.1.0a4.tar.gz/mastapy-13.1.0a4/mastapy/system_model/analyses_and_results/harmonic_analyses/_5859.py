"""TorqueConverterPumpHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5744
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "TorqueConverterPumpHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2631
    from mastapy.system_model.analyses_and_results.static_loads import _7001
    from mastapy.system_model.analyses_and_results.system_deflections import _2852
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5812,
        _5731,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpHarmonicAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterPumpHarmonicAnalysis")


class TorqueConverterPumpHarmonicAnalysis(_5744.CouplingHalfHarmonicAnalysis):
    """TorqueConverterPumpHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterPumpHarmonicAnalysis")

    class _Cast_TorqueConverterPumpHarmonicAnalysis:
        """Special nested class for casting TorqueConverterPumpHarmonicAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterPumpHarmonicAnalysis._Cast_TorqueConverterPumpHarmonicAnalysis",
            parent: "TorqueConverterPumpHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_harmonic_analysis(
            self: "TorqueConverterPumpHarmonicAnalysis._Cast_TorqueConverterPumpHarmonicAnalysis",
        ) -> "_5744.CouplingHalfHarmonicAnalysis":
            return self._parent._cast(_5744.CouplingHalfHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "TorqueConverterPumpHarmonicAnalysis._Cast_TorqueConverterPumpHarmonicAnalysis",
        ) -> "_5812.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "TorqueConverterPumpHarmonicAnalysis._Cast_TorqueConverterPumpHarmonicAnalysis",
        ) -> "_5731.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5731,
            )

            return self._parent._cast(_5731.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "TorqueConverterPumpHarmonicAnalysis._Cast_TorqueConverterPumpHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterPumpHarmonicAnalysis._Cast_TorqueConverterPumpHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterPumpHarmonicAnalysis._Cast_TorqueConverterPumpHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterPumpHarmonicAnalysis._Cast_TorqueConverterPumpHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterPumpHarmonicAnalysis._Cast_TorqueConverterPumpHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpHarmonicAnalysis._Cast_TorqueConverterPumpHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(
            self: "TorqueConverterPumpHarmonicAnalysis._Cast_TorqueConverterPumpHarmonicAnalysis",
        ) -> "TorqueConverterPumpHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpHarmonicAnalysis._Cast_TorqueConverterPumpHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "TorqueConverterPumpHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2631.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_7001.TorqueConverterPumpLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2852.TorqueConverterPumpSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterPumpSystemDeflection

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
    ) -> (
        "TorqueConverterPumpHarmonicAnalysis._Cast_TorqueConverterPumpHarmonicAnalysis"
    ):
        return self._Cast_TorqueConverterPumpHarmonicAnalysis(self)
