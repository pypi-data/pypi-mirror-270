"""RootAssemblyCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3146,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "RootAssemblyCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3101,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3139,
        _3218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="RootAssemblyCompoundSteadyStateSynchronousResponse")


class RootAssemblyCompoundSteadyStateSynchronousResponse(
    _3146.AssemblyCompoundSteadyStateSynchronousResponse
):
    """RootAssemblyCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RootAssemblyCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_RootAssemblyCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting RootAssemblyCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponse._Cast_RootAssemblyCompoundSteadyStateSynchronousResponse",
            parent: "RootAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def assembly_compound_steady_state_synchronous_response(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponse._Cast_RootAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3146.AssemblyCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3146.AssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponse._Cast_RootAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3139.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponse._Cast_RootAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponse._Cast_RootAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponse._Cast_RootAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponse._Cast_RootAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def root_assembly_compound_steady_state_synchronous_response(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponse._Cast_RootAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "RootAssemblyCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCompoundSteadyStateSynchronousResponse._Cast_RootAssemblyCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "RootAssemblyCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3101.RootAssemblySteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.RootAssemblySteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3101.RootAssemblySteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.RootAssemblySteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblyCompoundSteadyStateSynchronousResponse._Cast_RootAssemblyCompoundSteadyStateSynchronousResponse":
        return self._Cast_RootAssemblyCompoundSteadyStateSynchronousResponse(self)
