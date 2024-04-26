"""KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3171,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3075,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3208,
        _3211,
        _3197,
        _3216,
        _3164,
        _3218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",
)


class KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse(
    _3171.ConicalGearCompoundSteadyStateSynchronousResponse
):
    """KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",
            parent: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3171.ConicalGearCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3171.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3197.GearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(_3197.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(
                _3216.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3164.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3164,
            )

            return self._parent._cast(
                _3164.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3208.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3208,
            )

            return self._parent._cast(
                _3208.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3211.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3211,
            )

            return self._parent._cast(
                _3211.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> (
            "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse"
        ):
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> (
        "List[_3075.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse]

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
    ) -> (
        "List[_3075.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse]

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
    ) -> "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse":
        return self._Cast_KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse(
            self
        )
