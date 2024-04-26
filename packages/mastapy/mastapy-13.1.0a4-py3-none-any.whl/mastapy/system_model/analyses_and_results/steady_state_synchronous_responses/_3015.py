"""BeltConnectionSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3072,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "BeltConnectionSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2286
    from mastapy.system_model.analyses_and_results.static_loads import _6847
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3046,
        _3041,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="BeltConnectionSteadyStateSynchronousResponse")


class BeltConnectionSteadyStateSynchronousResponse(
    _3072.InterMountableComponentConnectionSteadyStateSynchronousResponse
):
    """BeltConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltConnectionSteadyStateSynchronousResponse"
    )

    class _Cast_BeltConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting BeltConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
            parent: "BeltConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "_3072.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3072.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "_3041.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(_3041.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_steady_state_synchronous_response(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "_3046.CVTBeltConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3046,
            )

            return self._parent._cast(
                _3046.CVTBeltConnectionSteadyStateSynchronousResponse
            )

        @property
        def belt_connection_steady_state_synchronous_response(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "BeltConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "BeltConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2286.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6847.BeltConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase

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
    ) -> "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse":
        return self._Cast_BeltConnectionSteadyStateSynchronousResponse(self)
