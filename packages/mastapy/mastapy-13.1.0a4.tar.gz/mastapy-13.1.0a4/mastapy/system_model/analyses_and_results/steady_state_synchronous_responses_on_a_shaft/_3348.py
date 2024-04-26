"""PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3305,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2366
    from mastapy.system_model.analyses_and_results.static_loads import _6956
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3333,
        _3303,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self",
    bound="PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
)


class PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft(
    _3305.CouplingConnectionSteadyStateSynchronousResponseOnAShaft
):
    """PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
            parent: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3305.CouplingConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3305.CouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3333.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3333,
            )

            return self._parent._cast(
                _3333.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3303.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3303,
            )

            return self._parent._cast(
                _3303.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft.TYPE",
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
    ) -> "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft(
            self
        )
