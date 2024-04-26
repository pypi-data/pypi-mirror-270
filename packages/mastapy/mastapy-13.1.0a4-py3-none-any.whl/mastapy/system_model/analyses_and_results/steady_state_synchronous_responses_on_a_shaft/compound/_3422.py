"""CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3495,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3292,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3442,
        _3401,
        _3433,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
)


class CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
    _3495.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
):
    """CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3495.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3495.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3401.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3401,
            )

            return self._parent._cast(
                _3401.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3433.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3433,
            )

            return self._parent._cast(
                _3433.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_analysis(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3442.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3442,
            )

            return self._parent._cast(
                _3442.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coaxial_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2287.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3292.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3292.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
