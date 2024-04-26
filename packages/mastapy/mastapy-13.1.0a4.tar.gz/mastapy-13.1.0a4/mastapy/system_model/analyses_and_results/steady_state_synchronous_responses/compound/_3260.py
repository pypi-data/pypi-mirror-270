"""UnbalancedMassCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3261,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "UnbalancedMassCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2495
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3131,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3216,
        _3164,
        _3218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="UnbalancedMassCompoundSteadyStateSynchronousResponse")


class UnbalancedMassCompoundSteadyStateSynchronousResponse(
    _3261.VirtualComponentCompoundSteadyStateSynchronousResponse
):
    """UnbalancedMassCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_UnbalancedMassCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_UnbalancedMassCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting UnbalancedMassCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponse._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponse",
            parent: "UnbalancedMassCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_steady_state_synchronous_response(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponse._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponse",
        ) -> "_3261.VirtualComponentCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3261.VirtualComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponse._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(
                _3216.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponse._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponse",
        ) -> "_3164.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3164,
            )

            return self._parent._cast(
                _3164.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponse._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponse._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponse._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponse._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponse._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponse",
        ) -> "UnbalancedMassCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassCompoundSteadyStateSynchronousResponse._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "UnbalancedMassCompoundSteadyStateSynchronousResponse.TYPE",
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
    ) -> "List[_3131.UnbalancedMassSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.UnbalancedMassSteadyStateSynchronousResponse]

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
    ) -> "List[_3131.UnbalancedMassSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.UnbalancedMassSteadyStateSynchronousResponse]

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
    ) -> "UnbalancedMassCompoundSteadyStateSynchronousResponse._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponse":
        return self._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponse(self)
