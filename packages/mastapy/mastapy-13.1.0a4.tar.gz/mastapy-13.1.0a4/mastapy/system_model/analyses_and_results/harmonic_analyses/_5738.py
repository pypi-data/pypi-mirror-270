"""ConicalGearHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5779
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ConicalGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.system_deflections import _2749
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5709,
        _5716,
        _5719,
        _5720,
        _5721,
        _5797,
        _5801,
        _5804,
        _5807,
        _5838,
        _5845,
        _5848,
        _5851,
        _5852,
        _5867,
        _5812,
        _5731,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearHarmonicAnalysis")


class ConicalGearHarmonicAnalysis(_5779.GearHarmonicAnalysis):
    """ConicalGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearHarmonicAnalysis")

    class _Cast_ConicalGearHarmonicAnalysis:
        """Special nested class for casting ConicalGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
            parent: "ConicalGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5779.GearHarmonicAnalysis":
            return self._parent._cast(_5779.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5812.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5731.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5731,
            )

            return self._parent._cast(_5731.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5709.AGMAGleasonConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5709,
            )

            return self._parent._cast(_5709.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5716.BevelDifferentialGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5716,
            )

            return self._parent._cast(_5716.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5719.BevelDifferentialPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5719,
            )

            return self._parent._cast(_5719.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5720.BevelDifferentialSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5720,
            )

            return self._parent._cast(_5720.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5721.BevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5721,
            )

            return self._parent._cast(_5721.BevelGearHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5797.HypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5797,
            )

            return self._parent._cast(_5797.HypoidGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5801.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5801,
            )

            return self._parent._cast(
                _5801.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5804.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5804,
            )

            return self._parent._cast(
                _5804.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5807.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5807,
            )

            return self._parent._cast(
                _5807.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5838.SpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5838,
            )

            return self._parent._cast(_5838.SpiralBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5845.StraightBevelDiffGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5845,
            )

            return self._parent._cast(_5845.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5848.StraightBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5848,
            )

            return self._parent._cast(_5848.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5851.StraightBevelPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5851,
            )

            return self._parent._cast(_5851.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5852.StraightBevelSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5852,
            )

            return self._parent._cast(_5852.StraightBevelSunGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "_5867.ZerolBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5867,
            )

            return self._parent._cast(_5867.ZerolBevelGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
        ) -> "ConicalGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2541.ConicalGear":
        """mastapy.system_model.part_model.gears.ConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearHarmonicAnalysis]

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
    def system_deflection_results(self: Self) -> "_2749.ConicalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSystemDeflection

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
    ) -> "ConicalGearHarmonicAnalysis._Cast_ConicalGearHarmonicAnalysis":
        return self._Cast_ConicalGearHarmonicAnalysis(self)
