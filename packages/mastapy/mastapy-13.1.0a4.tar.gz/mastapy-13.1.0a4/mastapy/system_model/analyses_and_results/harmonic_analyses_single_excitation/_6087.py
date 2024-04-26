"""FaceGearHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6092,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "FaceGearHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.static_loads import _6911
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6113,
        _6059,
        _6115,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="FaceGearHarmonicAnalysisOfSingleExcitation")


class FaceGearHarmonicAnalysisOfSingleExcitation(
    _6092.GearHarmonicAnalysisOfSingleExcitation
):
    """FaceGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_FaceGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting FaceGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
            parent: "FaceGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6092.GearHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6092.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6113.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6113,
            )

            return self._parent._cast(
                _6113.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6059.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6059,
            )

            return self._parent._cast(_6059.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(_6115.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def face_gear_harmonic_analysis_of_single_excitation(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "FaceGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "FaceGearHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
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
    def cast_to(
        self: Self,
    ) -> "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_FaceGearHarmonicAnalysisOfSingleExcitation(self)
