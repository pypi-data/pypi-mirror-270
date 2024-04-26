"""ZerolBevelGearHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6050,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "ZerolBevelGearHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2571
    from mastapy.system_model.analyses_and_results.static_loads import _7012
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6038,
        _6066,
        _6092,
        _6113,
        _6059,
        _6115,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="ZerolBevelGearHarmonicAnalysisOfSingleExcitation")


class ZerolBevelGearHarmonicAnalysisOfSingleExcitation(
    _6050.BevelGearHarmonicAnalysisOfSingleExcitation
):
    """ZerolBevelGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ZerolBevelGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ZerolBevelGearHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation",
            parent: "ZerolBevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6050.BevelGearHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6050.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6038.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6038,
            )

            return self._parent._cast(
                _6038.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6066.ConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6066,
            )

            return self._parent._cast(
                _6066.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6092.GearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(_6092.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6113.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6113,
            )

            return self._parent._cast(
                _6113.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6059.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6059,
            )

            return self._parent._cast(_6059.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(_6115.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "ZerolBevelGearHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "ZerolBevelGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation",
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
        self: Self,
        instance_to_wrap: "ZerolBevelGearHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2571.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_7012.ZerolBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase

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
    ) -> "ZerolBevelGearHarmonicAnalysisOfSingleExcitation._Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ZerolBevelGearHarmonicAnalysisOfSingleExcitation(self)
