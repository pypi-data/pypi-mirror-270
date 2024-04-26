"""PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3694,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2607
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3609,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3755,
        _3657,
        _3736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self",
    bound="PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
)


class PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed(
    _3694.CouplingCompoundSteadyStateSynchronousResponseAtASpeed
):
    """PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3694.CouplingCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3694.CouplingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3755.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3755,
            )

            return self._parent._cast(
                _3755.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3657.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3657,
            )

            return self._parent._cast(
                _3657.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3736.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2607.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2607.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

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
    ) -> "List[_3609.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3609.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
