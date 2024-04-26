"""CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3277,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2291
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3333,
        _3303,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft")


class CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft(
    _3277.BeltConnectionSteadyStateSynchronousResponseOnAShaft
):
    """CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft",
            parent: "CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def belt_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3277.BeltConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3277.BeltConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3333.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3333,
            )

            return self._parent._cast(
                _3333.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3303.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3303,
            )

            return self._parent._cast(
                _3303.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2291.CVTBeltConnection":
        """mastapy.system_model.connections_and_sockets.CVTBeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft(self)
