"""SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3513,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2629
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3384,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3437,
        _3475,
        _3423,
        _3477,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft"
)


class SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft(
    _3513.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
):
    """SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3513.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3513.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3437.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3437,
            )

            return self._parent._cast(
                _3437.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3475.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3475,
            )

            return self._parent._cast(
                _3475.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3423.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3423,
            )

            return self._parent._cast(
                _3423.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3477.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3477,
            )

            return self._parent._cast(
                _3477.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2629.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3384.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3384.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft]

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
    def cast_to(
        self: Self,
    ) -> "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
