"""KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6103,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2557
    from mastapy.system_model.analyses_and_results.static_loads import _6944
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6104,
        _6105,
        _6068,
        _6094,
        _6134,
        _6034,
        _6115,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
)


class KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation(
    _6103.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
):
    """KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
            parent: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6103.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6103.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6068.ConicalGearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6068,
            )

            return self._parent._cast(
                _6068.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6094.GearSetHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6094,
            )

            return self._parent._cast(_6094.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6134.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6134,
            )

            return self._parent._cast(
                _6134.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6034.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6034,
            )

            return self._parent._cast(
                _6034.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(_6115.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2557.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6944.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_conical_gears_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6104.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidConicalGearsHarmonicAnalysisOfSingleExcitation
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6104.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidGearsHarmonicAnalysisOfSingleExcitation
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_conical_meshes_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6105.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidConicalMeshesHarmonicAnalysisOfSingleExcitation
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6105.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidMeshesHarmonicAnalysisOfSingleExcitation
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation(
            self
        )
