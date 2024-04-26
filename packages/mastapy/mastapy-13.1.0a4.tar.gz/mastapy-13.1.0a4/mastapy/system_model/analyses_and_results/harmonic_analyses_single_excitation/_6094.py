"""GearSetHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6134,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "GearSetHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6092,
        _6093,
        _6040,
        _6047,
        _6052,
        _6065,
        _6068,
        _6083,
        _6089,
        _6099,
        _6103,
        _6106,
        _6109,
        _6120,
        _6137,
        _6143,
        _6146,
        _6161,
        _6164,
        _6034,
        _6115,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearSetHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="GearSetHarmonicAnalysisOfSingleExcitation")


class GearSetHarmonicAnalysisOfSingleExcitation(
    _6134.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
):
    """GearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearSetHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_GearSetHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting GearSetHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
            parent: "GearSetHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6134.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6134.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6034.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6034,
            )

            return self._parent._cast(
                _6034.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(_6115.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6040.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6047.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6047,
            )

            return self._parent._cast(
                _6047.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6052.BevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6052,
            )

            return self._parent._cast(
                _6052.BevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6065.ConceptGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6065,
            )

            return self._parent._cast(
                _6065.ConceptGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6068.ConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6068,
            )

            return self._parent._cast(
                _6068.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6083.CylindricalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6083,
            )

            return self._parent._cast(
                _6083.CylindricalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6089.FaceGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(
                _6089.FaceGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6099.HypoidGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6099,
            )

            return self._parent._cast(
                _6099.HypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6103.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6103,
            )

            return self._parent._cast(
                _6103.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6106.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6106,
            )

            return self._parent._cast(
                _6106.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6109.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6109,
            )

            return self._parent._cast(
                _6109.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6120.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6120,
            )

            return self._parent._cast(
                _6120.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6137.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6137,
            )

            return self._parent._cast(
                _6137.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6143.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6143,
            )

            return self._parent._cast(
                _6143.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6146.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6146,
            )

            return self._parent._cast(
                _6146.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6161.WormGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6161,
            )

            return self._parent._cast(
                _6161.WormGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6164.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6164,
            )

            return self._parent._cast(
                _6164.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "GearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "GearSetHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2550.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6092.GearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.GearHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6093.GearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.GearMeshHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetHarmonicAnalysisOfSingleExcitation._Cast_GearSetHarmonicAnalysisOfSingleExcitation":
        return self._Cast_GearSetHarmonicAnalysisOfSingleExcitation(self)
