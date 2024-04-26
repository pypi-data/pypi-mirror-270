"""CVTPulleySteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3615,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "CVTPulleySteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3565,
        _3604,
        _3552,
        _3606,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleySteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="CVTPulleySteadyStateSynchronousResponseAtASpeed")


class CVTPulleySteadyStateSynchronousResponseAtASpeed(
    _3615.PulleySteadyStateSynchronousResponseAtASpeed
):
    """CVTPulleySteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CVTPulleySteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
            parent: "CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def pulley_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3615.PulleySteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3615.PulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3565.CouplingHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3565,
            )

            return self._parent._cast(
                _3565.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(
                _3604.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3552.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3552,
            )

            return self._parent._cast(
                _3552.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ) -> "_3606.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3606,
            )

            return self._parent._cast(_3606.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_pulley_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ) -> "CVTPulleySteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CVTPulleySteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed(self)
