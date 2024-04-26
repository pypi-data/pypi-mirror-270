"""ConnectorSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3084,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ConnectorSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2465
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3014,
        _3085,
        _3102,
        _3031,
        _3086,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConnectorSteadyStateSynchronousResponse")


class ConnectorSteadyStateSynchronousResponse(
    _3084.MountableComponentSteadyStateSynchronousResponse
):
    """ConnectorSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectorSteadyStateSynchronousResponse"
    )

    class _Cast_ConnectorSteadyStateSynchronousResponse:
        """Special nested class for casting ConnectorSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
            parent: "ConnectorSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_3084.MountableComponentSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3084.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_3031.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3031,
            )

            return self._parent._cast(_3031.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bearing_steady_state_synchronous_response(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_3014.BearingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3014,
            )

            return self._parent._cast(_3014.BearingSteadyStateSynchronousResponse)

        @property
        def oil_seal_steady_state_synchronous_response(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_3085.OilSealSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3085,
            )

            return self._parent._cast(_3085.OilSealSteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_steady_state_synchronous_response(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "_3102.ShaftHubConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3102,
            )

            return self._parent._cast(
                _3102.ShaftHubConnectionSteadyStateSynchronousResponse
            )

        @property
        def connector_steady_state_synchronous_response(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
        ) -> "ConnectorSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "ConnectorSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2465.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse":
        return self._Cast_ConnectorSteadyStateSynchronousResponse(self)
