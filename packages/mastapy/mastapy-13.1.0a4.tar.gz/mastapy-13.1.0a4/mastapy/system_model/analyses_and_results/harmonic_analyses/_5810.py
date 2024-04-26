"""MassDiscHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5863
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "MassDiscHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2480
    from mastapy.system_model.analyses_and_results.static_loads import _6948
    from mastapy.system_model.analyses_and_results.system_deflections import _2802
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5812,
        _5731,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscHarmonicAnalysis",)


Self = TypeVar("Self", bound="MassDiscHarmonicAnalysis")


class MassDiscHarmonicAnalysis(_5863.VirtualComponentHarmonicAnalysis):
    """MassDiscHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MassDiscHarmonicAnalysis")

    class _Cast_MassDiscHarmonicAnalysis:
        """Special nested class for casting MassDiscHarmonicAnalysis to subclasses."""

        def __init__(
            self: "MassDiscHarmonicAnalysis._Cast_MassDiscHarmonicAnalysis",
            parent: "MassDiscHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_harmonic_analysis(
            self: "MassDiscHarmonicAnalysis._Cast_MassDiscHarmonicAnalysis",
        ) -> "_5863.VirtualComponentHarmonicAnalysis":
            return self._parent._cast(_5863.VirtualComponentHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "MassDiscHarmonicAnalysis._Cast_MassDiscHarmonicAnalysis",
        ) -> "_5812.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "MassDiscHarmonicAnalysis._Cast_MassDiscHarmonicAnalysis",
        ) -> "_5731.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5731,
            )

            return self._parent._cast(_5731.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "MassDiscHarmonicAnalysis._Cast_MassDiscHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MassDiscHarmonicAnalysis._Cast_MassDiscHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MassDiscHarmonicAnalysis._Cast_MassDiscHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MassDiscHarmonicAnalysis._Cast_MassDiscHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MassDiscHarmonicAnalysis._Cast_MassDiscHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscHarmonicAnalysis._Cast_MassDiscHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def mass_disc_harmonic_analysis(
            self: "MassDiscHarmonicAnalysis._Cast_MassDiscHarmonicAnalysis",
        ) -> "MassDiscHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "MassDiscHarmonicAnalysis._Cast_MassDiscHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MassDiscHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2480.MassDisc":
        """mastapy.system_model.part_model.MassDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6948.MassDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2802.MassDiscSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.MassDiscSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[MassDiscHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.MassDiscHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "MassDiscHarmonicAnalysis._Cast_MassDiscHarmonicAnalysis":
        return self._Cast_MassDiscHarmonicAnalysis(self)
