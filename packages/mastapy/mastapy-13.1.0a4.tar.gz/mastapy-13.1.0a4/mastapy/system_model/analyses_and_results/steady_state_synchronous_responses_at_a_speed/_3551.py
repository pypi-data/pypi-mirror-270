"""CoaxialConnectionSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3624,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.static_loads import _6863
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3571,
        _3530,
        _3562,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="CoaxialConnectionSteadyStateSynchronousResponseAtASpeed")


class CoaxialConnectionSteadyStateSynchronousResponseAtASpeed(
    _3624.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
):
    """CoaxialConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_CoaxialConnectionSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CoaxialConnectionSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
            parent: "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3624.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3624.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3530.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3530,
            )

            return self._parent._cast(
                _3530.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3562.ConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3562,
            )

            return self._parent._cast(
                _3562.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_at_a_speed(
            self: "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3571.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3571,
            )

            return self._parent._cast(
                _3571.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coaxial_connection_steady_state_synchronous_response_at_a_speed(
            self: "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2287.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6863.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CoaxialConnectionSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CoaxialConnectionSteadyStateSynchronousResponseAtASpeed(self)
