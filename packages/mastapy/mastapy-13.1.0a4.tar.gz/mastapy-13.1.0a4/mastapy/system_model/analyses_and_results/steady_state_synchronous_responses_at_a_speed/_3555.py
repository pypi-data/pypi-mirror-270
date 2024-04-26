"""ConceptCouplingSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3566,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2599
    from mastapy.system_model.analyses_and_results.static_loads import _6867
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3625,
        _3527,
        _3606,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="ConceptCouplingSteadyStateSynchronousResponseAtASpeed")


class ConceptCouplingSteadyStateSynchronousResponseAtASpeed(
    _3566.CouplingSteadyStateSynchronousResponseAtASpeed
):
    """ConceptCouplingSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_ConceptCouplingSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ConceptCouplingSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ConceptCouplingSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
            parent: "ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_steady_state_synchronous_response_at_a_speed(
            self: "ConceptCouplingSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3566.CouplingSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3566.CouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "ConceptCouplingSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3625.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3625,
            )

            return self._parent._cast(
                _3625.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "ConceptCouplingSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3527.AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3527,
            )

            return self._parent._cast(
                _3527.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "ConceptCouplingSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3606.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3606,
            )

            return self._parent._cast(_3606.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_coupling_steady_state_synchronous_response_at_a_speed(
            self: "ConceptCouplingSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
        ) -> "ConceptCouplingSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ConceptCouplingSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self: Self) -> "_6867.ConceptCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ConceptCouplingSteadyStateSynchronousResponseAtASpeed(self)
