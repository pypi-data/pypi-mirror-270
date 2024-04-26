"""GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3682,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2473
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3588,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed"
)


class GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed(
    _3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
):
    """GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3736.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response_at_a_speed(
            self: "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2473.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

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
    ) -> "List[_3588.GuideDxfModelSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.GuideDxfModelSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3588.GuideDxfModelSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.GuideDxfModelSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
