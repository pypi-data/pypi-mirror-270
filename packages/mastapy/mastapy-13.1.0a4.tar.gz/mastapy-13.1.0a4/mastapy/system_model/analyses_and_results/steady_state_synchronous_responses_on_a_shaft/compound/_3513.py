"""SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3437,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3383,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3512,
        _3514,
        _3475,
        _3423,
        _3477,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft"
)


class SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft(
    _3437.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
):
    """SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3437.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3437.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3475.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3475,
            )

            return self._parent._cast(
                _3475.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3423.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3423,
            )

            return self._parent._cast(
                _3423.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3477.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3477,
            )

            return self._parent._cast(
                _3477.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3512.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3512,
            )

            return self._parent._cast(
                _3512.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3514.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3514,
            )

            return self._parent._cast(
                _3514.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3383.SynchroniserPartSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.SynchroniserPartSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3383.SynchroniserPartSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.SynchroniserPartSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
