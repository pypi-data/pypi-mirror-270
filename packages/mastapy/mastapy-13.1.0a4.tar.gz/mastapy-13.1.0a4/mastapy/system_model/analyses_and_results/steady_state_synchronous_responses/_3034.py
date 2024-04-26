"""ConceptCouplingSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3045,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ConceptCouplingSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2599
    from mastapy.system_model.analyses_and_results.static_loads import _6867
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3105,
        _3006,
        _3086,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConceptCouplingSteadyStateSynchronousResponse")


class ConceptCouplingSteadyStateSynchronousResponse(
    _3045.CouplingSteadyStateSynchronousResponse
):
    """ConceptCouplingSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingSteadyStateSynchronousResponse"
    )

    class _Cast_ConceptCouplingSteadyStateSynchronousResponse:
        """Special nested class for casting ConceptCouplingSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
            parent: "ConceptCouplingSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_steady_state_synchronous_response(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_3045.CouplingSteadyStateSynchronousResponse":
            return self._parent._cast(_3045.CouplingSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_3105.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3105,
            )

            return self._parent._cast(
                _3105.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_3006.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(
                _3006.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_coupling_steady_state_synchronous_response(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
        ) -> "ConceptCouplingSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ConceptCouplingSteadyStateSynchronousResponse.TYPE",
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
    ) -> "ConceptCouplingSteadyStateSynchronousResponse._Cast_ConceptCouplingSteadyStateSynchronousResponse":
        return self._Cast_ConceptCouplingSteadyStateSynchronousResponse(self)
