"""AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3682,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3528,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3658,
        _3702,
        _3713,
        _3752,
        _3736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed"
)


class AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed(
    _3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
):
    """AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = (
        _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3736.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3658.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3658,
            )

            return self._parent._cast(
                _3658.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3702.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3702,
            )

            return self._parent._cast(
                _3702.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def fe_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3713.FEPartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3713,
            )

            return self._parent._cast(
                _3713.FEPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3752.ShaftCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3752,
            )

            return self._parent._cast(
                _3752.ShaftCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3528.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3528.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
