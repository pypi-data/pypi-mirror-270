"""SynchroniserHalfCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3254,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "SynchroniserHalfCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2627
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3123,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3178,
        _3216,
        _3164,
        _3218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SynchroniserHalfCompoundSteadyStateSynchronousResponse")


class SynchroniserHalfCompoundSteadyStateSynchronousResponse(
    _3254.SynchroniserPartCompoundSteadyStateSynchronousResponse
):
    """SynchroniserHalfCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting SynchroniserHalfCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
            parent: "SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_steady_state_synchronous_response(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_3254.SynchroniserPartCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3254.SynchroniserPartCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_3178.CouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3178,
            )

            return self._parent._cast(
                _3178.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(
                _3216.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_3164.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3164,
            )

            return self._parent._cast(
                _3164.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_steady_state_synchronous_response(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ) -> "SynchroniserHalfCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "SynchroniserHalfCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2627.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3123.SynchroniserHalfSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SynchroniserHalfSteadyStateSynchronousResponse]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3123.SynchroniserHalfSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SynchroniserHalfSteadyStateSynchronousResponse]

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
    def cast_to(
        self: Self,
    ) -> "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse":
        return self._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse(self)
