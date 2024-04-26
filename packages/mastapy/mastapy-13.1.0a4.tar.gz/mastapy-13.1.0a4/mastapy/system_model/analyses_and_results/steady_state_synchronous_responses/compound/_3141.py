"""AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3164,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3007,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3140,
        _3184,
        _3195,
        _3234,
        _3218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse"
)


class AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse(
    _3164.ComponentCompoundSteadyStateSynchronousResponse
):
    """AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse",
            parent: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def component_compound_steady_state_synchronous_response(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse",
        ) -> "_3164.ComponentCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3164.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_steady_state_synchronous_response(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse",
        ) -> "_3140.AbstractShaftCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3140,
            )

            return self._parent._cast(
                _3140.AbstractShaftCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse",
        ) -> "_3184.CycloidalDiscCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3184,
            )

            return self._parent._cast(
                _3184.CycloidalDiscCompoundSteadyStateSynchronousResponse
            )

        @property
        def fe_part_compound_steady_state_synchronous_response(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse",
        ) -> "_3195.FEPartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(
                _3195.FEPartCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_compound_steady_state_synchronous_response(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse",
        ) -> "_3234.ShaftCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3234,
            )

            return self._parent._cast(_3234.ShaftCompoundSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse",
        ) -> "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3007.AbstractShaftOrHousingSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AbstractShaftOrHousingSteadyStateSynchronousResponse]

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
    ) -> "List[_3007.AbstractShaftOrHousingSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AbstractShaftOrHousingSteadyStateSynchronousResponse]

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
    ) -> "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse":
        return self._Cast_AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse(
            self
        )
