"""StraightBevelSunGearHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6141,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2568
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6050,
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
__all__ = ("StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="StraightBevelSunGearHarmonicAnalysisOfSingleExcitation")


class StraightBevelSunGearHarmonicAnalysisOfSingleExcitation(
    _6141.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
):
    """StraightBevelSunGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting StraightBevelSunGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
            parent: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(
            self: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6141.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6141.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6050.BevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6050,
            )

            return self._parent._cast(_6050.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6038.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6038,
            )

            return self._parent._cast(
                _6038.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6066.ConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6066,
            )

            return self._parent._cast(
                _6066.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6092.GearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(_6092.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6113.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6113,
            )

            return self._parent._cast(
                _6113.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6059.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6059,
            )

            return self._parent._cast(_6059.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(_6115.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(
            self: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
        ) -> "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2568.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelSunGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_StraightBevelSunGearHarmonicAnalysisOfSingleExcitation(self)
