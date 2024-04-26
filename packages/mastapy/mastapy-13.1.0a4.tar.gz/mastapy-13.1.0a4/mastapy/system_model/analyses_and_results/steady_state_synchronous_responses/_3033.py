"""ConceptCouplingHalfSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3044,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ConceptCouplingHalfSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2600
    from mastapy.system_model.analyses_and_results.static_loads import _6866
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3084,
        _3031,
        _3086,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConceptCouplingHalfSteadyStateSynchronousResponse")


class ConceptCouplingHalfSteadyStateSynchronousResponse(
    _3044.CouplingHalfSteadyStateSynchronousResponse
):
    """ConceptCouplingHalfSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingHalfSteadyStateSynchronousResponse"
    )

    class _Cast_ConceptCouplingHalfSteadyStateSynchronousResponse:
        """Special nested class for casting ConceptCouplingHalfSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
            parent: "ConceptCouplingHalfSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3044.CouplingHalfSteadyStateSynchronousResponse":
            return self._parent._cast(_3044.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3084.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(
                _3084.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3031.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3031,
            )

            return self._parent._cast(_3031.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_coupling_half_steady_state_synchronous_response(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
        ) -> "ConceptCouplingHalfSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ConceptCouplingHalfSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2600.ConceptCouplingHalf":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6866.ConceptCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingHalfSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse":
        return self._Cast_ConceptCouplingHalfSteadyStateSynchronousResponse(self)
