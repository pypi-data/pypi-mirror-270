"""RollingRingConnectionSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3592,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2310
    from mastapy.system_model.analyses_and_results.static_loads import _6973
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3562,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="RollingRingConnectionSteadyStateSynchronousResponseAtASpeed"
)


class RollingRingConnectionSteadyStateSynchronousResponseAtASpeed(
    _3592.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
):
    """RollingRingConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_RollingRingConnectionSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting RollingRingConnectionSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",
            parent: "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3592.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3592.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3562.ConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3562,
            )

            return self._parent._cast(
                _3562.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_steady_state_synchronous_response_at_a_speed(
            self: "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(self: Self) -> "_6973.RollingRingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[RollingRingConnectionSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.RollingRingConnectionSteadyStateSynchronousResponseAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingConnectionSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_RollingRingConnectionSteadyStateSynchronousResponseAtASpeed(
            self
        )
