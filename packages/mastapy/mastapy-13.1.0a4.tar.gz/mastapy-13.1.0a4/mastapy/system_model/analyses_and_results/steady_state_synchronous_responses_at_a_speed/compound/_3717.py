"""GearSetCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3755,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3586,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3663,
        _3670,
        _3675,
        _3688,
        _3691,
        _3706,
        _3712,
        _3721,
        _3725,
        _3728,
        _3731,
        _3741,
        _3758,
        _3764,
        _3767,
        _3782,
        _3785,
        _3657,
        _3736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearSetCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="GearSetCompoundSteadyStateSynchronousResponseAtASpeed")


class GearSetCompoundSteadyStateSynchronousResponseAtASpeed(
    _3755.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
):
    """GearSetCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting GearSetCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3755.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3755.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3657.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3657,
            )

            return self._parent._cast(
                _3657.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3736.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3663.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3663,
            )

            return self._parent._cast(
                _3663.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3670.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3670,
            )

            return self._parent._cast(
                _3670.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3675.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3675,
            )

            return self._parent._cast(
                _3675.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3688.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3688,
            )

            return self._parent._cast(
                _3688.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3691.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3691,
            )

            return self._parent._cast(
                _3691.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3706.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3706,
            )

            return self._parent._cast(
                _3706.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3712.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3712,
            )

            return self._parent._cast(
                _3712.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3721.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3721,
            )

            return self._parent._cast(
                _3721.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3725.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3725,
            )

            return self._parent._cast(
                _3725.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3728.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3728,
            )

            return self._parent._cast(
                _3728.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3731.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3731,
            )

            return self._parent._cast(
                _3731.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3741.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3741,
            )

            return self._parent._cast(
                _3741.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3758.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3758,
            )

            return self._parent._cast(
                _3758.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3764.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3764,
            )

            return self._parent._cast(
                _3764.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3767.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3767,
            )

            return self._parent._cast(
                _3767.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3782.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3782,
            )

            return self._parent._cast(
                _3782.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3785.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3785,
            )

            return self._parent._cast(
                _3785.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "GearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "GearSetCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3586.GearSetSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.GearSetSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3586.GearSetSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.GearSetSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_GearSetCompoundSteadyStateSynchronousResponseAtASpeed(self)
