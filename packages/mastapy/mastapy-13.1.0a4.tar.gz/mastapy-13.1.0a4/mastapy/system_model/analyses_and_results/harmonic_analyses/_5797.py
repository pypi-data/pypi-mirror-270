"""HypoidGearHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5709
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "HypoidGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2552
    from mastapy.system_model.analyses_and_results.static_loads import _6932
    from mastapy.system_model.analyses_and_results.system_deflections import _2788
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5738,
        _5779,
        _5812,
        _5731,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="HypoidGearHarmonicAnalysis")


class HypoidGearHarmonicAnalysis(_5709.AGMAGleasonConicalGearHarmonicAnalysis):
    """HypoidGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearHarmonicAnalysis")

    class _Cast_HypoidGearHarmonicAnalysis:
        """Special nested class for casting HypoidGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
            parent: "HypoidGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_5709.AGMAGleasonConicalGearHarmonicAnalysis":
            return self._parent._cast(_5709.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_5738.ConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5738,
            )

            return self._parent._cast(_5738.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_5779.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5779,
            )

            return self._parent._cast(_5779.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_5812.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_5731.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5731,
            )

            return self._parent._cast(_5731.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
        ) -> "HypoidGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2552.HypoidGear":
        """mastapy.system_model.part_model.gears.HypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6932.HypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2788.HypoidGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSystemDeflection

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
    ) -> "HypoidGearHarmonicAnalysis._Cast_HypoidGearHarmonicAnalysis":
        return self._Cast_HypoidGearHarmonicAnalysis(self)
