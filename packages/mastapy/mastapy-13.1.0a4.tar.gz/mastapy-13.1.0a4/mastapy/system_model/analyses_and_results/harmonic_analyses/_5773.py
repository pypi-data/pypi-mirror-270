"""FaceGearHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5779
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "FaceGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.static_loads import _6911
    from mastapy.system_model.analyses_and_results.system_deflections import _2779
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5812,
        _5731,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="FaceGearHarmonicAnalysis")


class FaceGearHarmonicAnalysis(_5779.GearHarmonicAnalysis):
    """FaceGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearHarmonicAnalysis")

    class _Cast_FaceGearHarmonicAnalysis:
        """Special nested class for casting FaceGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "FaceGearHarmonicAnalysis._Cast_FaceGearHarmonicAnalysis",
            parent: "FaceGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_harmonic_analysis(
            self: "FaceGearHarmonicAnalysis._Cast_FaceGearHarmonicAnalysis",
        ) -> "_5779.GearHarmonicAnalysis":
            return self._parent._cast(_5779.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "FaceGearHarmonicAnalysis._Cast_FaceGearHarmonicAnalysis",
        ) -> "_5812.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "FaceGearHarmonicAnalysis._Cast_FaceGearHarmonicAnalysis",
        ) -> "_5731.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5731,
            )

            return self._parent._cast(_5731.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "FaceGearHarmonicAnalysis._Cast_FaceGearHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearHarmonicAnalysis._Cast_FaceGearHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearHarmonicAnalysis._Cast_FaceGearHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearHarmonicAnalysis._Cast_FaceGearHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearHarmonicAnalysis._Cast_FaceGearHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearHarmonicAnalysis._Cast_FaceGearHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def face_gear_harmonic_analysis(
            self: "FaceGearHarmonicAnalysis._Cast_FaceGearHarmonicAnalysis",
        ) -> "FaceGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearHarmonicAnalysis._Cast_FaceGearHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2546.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6911.FaceGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2779.FaceGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.FaceGearSystemDeflection

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
    ) -> "FaceGearHarmonicAnalysis._Cast_FaceGearHarmonicAnalysis":
        return self._Cast_FaceGearHarmonicAnalysis(self)
