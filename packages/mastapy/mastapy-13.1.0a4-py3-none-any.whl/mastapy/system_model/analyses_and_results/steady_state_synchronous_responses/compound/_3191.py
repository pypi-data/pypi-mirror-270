"""ExternalCADModelCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3164,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ExternalCADModelCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2470
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3059,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ExternalCADModelCompoundSteadyStateSynchronousResponse")


class ExternalCADModelCompoundSteadyStateSynchronousResponse(
    _3164.ComponentCompoundSteadyStateSynchronousResponse
):
    """ExternalCADModelCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ExternalCADModelCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_ExternalCADModelCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ExternalCADModelCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ExternalCADModelCompoundSteadyStateSynchronousResponse._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponse",
            parent: "ExternalCADModelCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def component_compound_steady_state_synchronous_response(
            self: "ExternalCADModelCompoundSteadyStateSynchronousResponse._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponse",
        ) -> "_3164.ComponentCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3164.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "ExternalCADModelCompoundSteadyStateSynchronousResponse._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "ExternalCADModelCompoundSteadyStateSynchronousResponse._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ExternalCADModelCompoundSteadyStateSynchronousResponse._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelCompoundSteadyStateSynchronousResponse._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def external_cad_model_compound_steady_state_synchronous_response(
            self: "ExternalCADModelCompoundSteadyStateSynchronousResponse._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponse",
        ) -> "ExternalCADModelCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelCompoundSteadyStateSynchronousResponse._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ExternalCADModelCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2470.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

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
    ) -> "List[_3059.ExternalCADModelSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ExternalCADModelSteadyStateSynchronousResponse]

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
    ) -> "List[_3059.ExternalCADModelSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ExternalCADModelSteadyStateSynchronousResponse]

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
    ) -> "ExternalCADModelCompoundSteadyStateSynchronousResponse._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponse":
        return self._Cast_ExternalCADModelCompoundSteadyStateSynchronousResponse(self)
