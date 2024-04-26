"""ClutchHalfSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3565,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "ClutchHalfSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.static_loads import _6860
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3604,
        _3552,
        _3606,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="ClutchHalfSteadyStateSynchronousResponseAtASpeed")


class ClutchHalfSteadyStateSynchronousResponseAtASpeed(
    _3565.CouplingHalfSteadyStateSynchronousResponseAtASpeed
):
    """ClutchHalfSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ClutchHalfSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_ClutchHalfSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ClutchHalfSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ClutchHalfSteadyStateSynchronousResponseAtASpeed._Cast_ClutchHalfSteadyStateSynchronousResponseAtASpeed",
            parent: "ClutchHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "ClutchHalfSteadyStateSynchronousResponseAtASpeed._Cast_ClutchHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3565.CouplingHalfSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3565.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "ClutchHalfSteadyStateSynchronousResponseAtASpeed._Cast_ClutchHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(
                _3604.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "ClutchHalfSteadyStateSynchronousResponseAtASpeed._Cast_ClutchHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3552.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3552,
            )

            return self._parent._cast(
                _3552.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "ClutchHalfSteadyStateSynchronousResponseAtASpeed._Cast_ClutchHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3606.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3606,
            )

            return self._parent._cast(_3606.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ClutchHalfSteadyStateSynchronousResponseAtASpeed._Cast_ClutchHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ClutchHalfSteadyStateSynchronousResponseAtASpeed._Cast_ClutchHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ClutchHalfSteadyStateSynchronousResponseAtASpeed._Cast_ClutchHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchHalfSteadyStateSynchronousResponseAtASpeed._Cast_ClutchHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfSteadyStateSynchronousResponseAtASpeed._Cast_ClutchHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_steady_state_synchronous_response_at_a_speed(
            self: "ClutchHalfSteadyStateSynchronousResponseAtASpeed._Cast_ClutchHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "ClutchHalfSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ClutchHalfSteadyStateSynchronousResponseAtASpeed._Cast_ClutchHalfSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ClutchHalfSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2597.ClutchHalf":
        """mastapy.system_model.part_model.couplings.ClutchHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6860.ClutchHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase

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
    ) -> "ClutchHalfSteadyStateSynchronousResponseAtASpeed._Cast_ClutchHalfSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ClutchHalfSteadyStateSynchronousResponseAtASpeed(self)
