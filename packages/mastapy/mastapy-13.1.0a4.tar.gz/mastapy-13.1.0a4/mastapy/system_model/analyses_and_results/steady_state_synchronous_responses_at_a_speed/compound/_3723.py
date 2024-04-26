"""KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3689,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3595,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3726,
        _3729,
        _3715,
        _3734,
        _3682,
        _3736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = (
    "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
)


class KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed(
    _3689.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
):
    """KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3689.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3689.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3715.GearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3715,
            )

            return self._parent._cast(
                _3715.GearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3734.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3734,
            )

            return self._parent._cast(
                _3734.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3682,
            )

            return self._parent._cast(
                _3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3736.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3726.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3726,
            )

            return self._parent._cast(
                _3726.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3729.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3729,
            )

            return self._parent._cast(
                _3729.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3595.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3595.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
