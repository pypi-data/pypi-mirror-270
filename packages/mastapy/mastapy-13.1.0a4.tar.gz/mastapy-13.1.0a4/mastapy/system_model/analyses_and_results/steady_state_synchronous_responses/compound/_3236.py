"""ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3142,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3104,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3163,
        _3183,
        _3222,
        _3174,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self",
    bound="ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
)


class ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse(
    _3142.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
):
    """ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
            parent: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3142.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3142.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3174.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3174,
            )

            return self._parent._cast(
                _3174.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3163.CoaxialConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3163,
            )

            return self._parent._cast(
                _3163.CoaxialConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3183.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3183,
            )

            return self._parent._cast(
                _3183.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3222.PlanetaryConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3222,
            )

            return self._parent._cast(
                _3222.PlanetaryConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> (
            "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse"
        ):
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> (
        "List[_3104.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse]

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
    ) -> (
        "List[_3104.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse]

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
    ) -> "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
        return self._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse(
            self
        )
