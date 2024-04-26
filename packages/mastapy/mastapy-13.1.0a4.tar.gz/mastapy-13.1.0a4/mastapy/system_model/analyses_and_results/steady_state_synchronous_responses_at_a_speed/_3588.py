"""GuideDxfModelSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3552,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "GuideDxfModelSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2473
    from mastapy.system_model.analyses_and_results.static_loads import _6923
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3606,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="GuideDxfModelSteadyStateSynchronousResponseAtASpeed")


class GuideDxfModelSteadyStateSynchronousResponseAtASpeed(
    _3552.ComponentSteadyStateSynchronousResponseAtASpeed
):
    """GuideDxfModelSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GuideDxfModelSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_GuideDxfModelSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting GuideDxfModelSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "GuideDxfModelSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelSteadyStateSynchronousResponseAtASpeed",
            parent: "GuideDxfModelSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "GuideDxfModelSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3552.ComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3552.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "GuideDxfModelSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3606.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3606,
            )

            return self._parent._cast(_3606.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "GuideDxfModelSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GuideDxfModelSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GuideDxfModelSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GuideDxfModelSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def guide_dxf_model_steady_state_synchronous_response_at_a_speed(
            self: "GuideDxfModelSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelSteadyStateSynchronousResponseAtASpeed",
        ) -> "GuideDxfModelSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "GuideDxfModelSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2473.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6923.GuideDxfModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase

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
    ) -> "GuideDxfModelSteadyStateSynchronousResponseAtASpeed._Cast_GuideDxfModelSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_GuideDxfModelSteadyStateSynchronousResponseAtASpeed(self)
