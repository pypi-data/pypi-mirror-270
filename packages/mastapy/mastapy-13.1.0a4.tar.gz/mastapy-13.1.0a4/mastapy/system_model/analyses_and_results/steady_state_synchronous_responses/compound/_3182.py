"""CycloidalAssemblyCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3237,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "CycloidalAssemblyCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2586
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3049,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3139,
        _3218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblyCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CycloidalAssemblyCompoundSteadyStateSynchronousResponse")


class CycloidalAssemblyCompoundSteadyStateSynchronousResponse(
    _3237.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
):
    """CycloidalAssemblyCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CycloidalAssemblyCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponse._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponse",
            parent: "CycloidalAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponse._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3237.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3237.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponse._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3139.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponse._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponse._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponse._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponse._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponse._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "CycloidalAssemblyCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CycloidalAssemblyCompoundSteadyStateSynchronousResponse._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CycloidalAssemblyCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2586.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2586.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3049.CycloidalAssemblySteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CycloidalAssemblySteadyStateSynchronousResponse]

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
    ) -> "List[_3049.CycloidalAssemblySteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CycloidalAssemblySteadyStateSynchronousResponse]

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
    ) -> "CycloidalAssemblyCompoundSteadyStateSynchronousResponse._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponse":
        return self._Cast_CycloidalAssemblyCompoundSteadyStateSynchronousResponse(self)
