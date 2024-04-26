"""ConnectorCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3734,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3563,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3665,
        _3735,
        _3753,
        _3682,
        _3736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="ConnectorCompoundSteadyStateSynchronousResponseAtASpeed")


class ConnectorCompoundSteadyStateSynchronousResponseAtASpeed(
    _3734.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
):
    """ConnectorCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ConnectorCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3734.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3734.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3682,
            )

            return self._parent._cast(
                _3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3736.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bearing_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3665.BearingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3665,
            )

            return self._parent._cast(
                _3665.BearingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3735.OilSealCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3735,
            )

            return self._parent._cast(
                _3735.OilSealCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3753.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3753,
            )

            return self._parent._cast(
                _3753.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_compound_steady_state_synchronous_response_at_a_speed(
            self: "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3563.ConnectorSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ConnectorSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3563.ConnectorSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ConnectorSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ConnectorCompoundSteadyStateSynchronousResponseAtASpeed(self)
