"""ConceptCouplingCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3176,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ConceptCouplingCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2599
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3034,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3237,
        _3139,
        _3218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConceptCouplingCompoundSteadyStateSynchronousResponse")


class ConceptCouplingCompoundSteadyStateSynchronousResponse(
    _3176.CouplingCompoundSteadyStateSynchronousResponse
):
    """ConceptCouplingCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_ConceptCouplingCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ConceptCouplingCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponse",
            parent: "ConceptCouplingCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_compound_steady_state_synchronous_response(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_3176.CouplingCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3176.CouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_3237.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3237,
            )

            return self._parent._cast(
                _3237.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_3139.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_coupling_compound_steady_state_synchronous_response(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponse",
        ) -> "ConceptCouplingCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ConceptCouplingCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2599.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2599.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

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
    ) -> "List[_3034.ConceptCouplingSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConceptCouplingSteadyStateSynchronousResponse]

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
    ) -> "List[_3034.ConceptCouplingSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConceptCouplingSteadyStateSynchronousResponse]

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
    ) -> "ConceptCouplingCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponse":
        return self._Cast_ConceptCouplingCompoundSteadyStateSynchronousResponse(self)
