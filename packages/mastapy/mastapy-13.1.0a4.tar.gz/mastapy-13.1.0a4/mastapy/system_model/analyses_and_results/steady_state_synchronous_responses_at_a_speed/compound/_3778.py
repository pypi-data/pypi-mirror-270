"""UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3779,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2495
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3649,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3734,
        _3682,
        _3736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed"
)


class UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed(
    _3779.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
):
    """UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3779.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3779.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3734.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3734,
            )

            return self._parent._cast(
                _3734.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3682,
            )

            return self._parent._cast(
                _3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3736.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_at_a_speed(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2495.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

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
    ) -> "List[_3649.UnbalancedMassSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.UnbalancedMassSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3649.UnbalancedMassSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.UnbalancedMassSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
