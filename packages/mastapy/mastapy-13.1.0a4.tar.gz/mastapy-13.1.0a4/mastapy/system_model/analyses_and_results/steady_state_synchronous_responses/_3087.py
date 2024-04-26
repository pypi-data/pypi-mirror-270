"""PartToPartShearCouplingConnectionSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3043,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "PartToPartShearCouplingConnectionSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2366
    from mastapy.system_model.analyses_and_results.static_loads import _6956
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3072,
        _3041,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingConnectionSteadyStateSynchronousResponse"
)


class PartToPartShearCouplingConnectionSteadyStateSynchronousResponse(
    _3043.CouplingConnectionSteadyStateSynchronousResponse
):
    """PartToPartShearCouplingConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponse",
    )

    class _Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting PartToPartShearCouplingConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponse",
            parent: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_connection_steady_state_synchronous_response(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3043.CouplingConnectionSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3043.CouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3072.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3072,
            )

            return self._parent._cast(
                _3072.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_3041.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(_3041.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponse",
        ) -> "PartToPartShearCouplingConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2366.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6956.PartToPartShearCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase

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
    ) -> "PartToPartShearCouplingConnectionSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponse":
        return (
            self._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponse(
                self
            )
        )
