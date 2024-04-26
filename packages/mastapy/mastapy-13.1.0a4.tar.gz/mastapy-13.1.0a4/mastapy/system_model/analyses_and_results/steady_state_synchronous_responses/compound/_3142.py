"""AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3174,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3009,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3163,
        _3183,
        _3185,
        _3222,
        _3236,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = (
    "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
)


class AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse(
    _3174.ConnectionCompoundSteadyStateSynchronousResponse
):
    """AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
            parent: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3174.ConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3174.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3163.CoaxialConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3163,
            )

            return self._parent._cast(
                _3163.CoaxialConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3183.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3183,
            )

            return self._parent._cast(
                _3183.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3185.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3185,
            )

            return self._parent._cast(
                _3185.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_compound_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3222.PlanetaryConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3222,
            )

            return self._parent._cast(
                _3222.PlanetaryConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3236.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3236,
            )

            return self._parent._cast(
                _3236.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3009.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3009.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse]

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
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse(
            self
        )
