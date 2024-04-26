"""AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6066,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6045,
        _6048,
        _6049,
        _6050,
        _6097,
        _6135,
        _6141,
        _6144,
        _6147,
        _6148,
        _6162,
        _6092,
        _6113,
        _6059,
        _6115,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation")


class AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation(
    _6066.ConicalGearHarmonicAnalysisOfSingleExcitation
):
    """AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
            parent: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6066.ConicalGearHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6066.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6092.GearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(_6092.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6113.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6113,
            )

            return self._parent._cast(
                _6113.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6059.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6059,
            )

            return self._parent._cast(_6059.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(_6115.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6045.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6045,
            )

            return self._parent._cast(
                _6045.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6048.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6048,
            )

            return self._parent._cast(
                _6048.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6049.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6049,
            )

            return self._parent._cast(
                _6049.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6050.BevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6050,
            )

            return self._parent._cast(_6050.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.HypoidGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(
                _6097.HypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6135.SpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6135,
            )

            return self._parent._cast(
                _6135.SpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6141.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6141,
            )

            return self._parent._cast(
                _6141.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6144.StraightBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6144,
            )

            return self._parent._cast(
                _6144.StraightBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6147.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6147,
            )

            return self._parent._cast(
                _6147.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6148.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6148,
            )

            return self._parent._cast(
                _6148.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6162.ZerolBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6162,
            )

            return self._parent._cast(
                _6162.ZerolBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
        ) -> "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2531.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation(self)
