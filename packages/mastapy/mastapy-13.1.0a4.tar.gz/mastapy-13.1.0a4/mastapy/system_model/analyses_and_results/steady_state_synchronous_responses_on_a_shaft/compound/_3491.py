"""RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3463,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2310
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3360,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3433,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
)


class RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
    _3463.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
):
    """RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = (
        _ROLLING_RING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3463.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3463.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3433.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3433,
            )

            return self._parent._cast(
                _3433.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_analysis(
            self: "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2310.RollingRingConnection":
        """mastapy.system_model.connections_and_sockets.RollingRingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2310.RollingRingConnection":
        """mastapy.system_model.connections_and_sockets.RollingRingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3360.RollingRingConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.RollingRingConnectionSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(
        self: Self,
    ) -> "List[RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3360.RollingRingConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.RollingRingConnectionSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
