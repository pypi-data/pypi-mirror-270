"""ExternalCADModelSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3552,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "ExternalCADModelSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2470
    from mastapy.system_model.analyses_and_results.static_loads import _6910
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3606,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="ExternalCADModelSteadyStateSynchronousResponseAtASpeed")


class ExternalCADModelSteadyStateSynchronousResponseAtASpeed(
    _3552.ComponentSteadyStateSynchronousResponseAtASpeed
):
    """ExternalCADModelSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ExternalCADModelSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_ExternalCADModelSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ExternalCADModelSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ExternalCADModelSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelSteadyStateSynchronousResponseAtASpeed",
            parent: "ExternalCADModelSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "ExternalCADModelSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3552.ComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3552.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "ExternalCADModelSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3606.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3606,
            )

            return self._parent._cast(_3606.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ExternalCADModelSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ExternalCADModelSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ExternalCADModelSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ExternalCADModelSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def external_cad_model_steady_state_synchronous_response_at_a_speed(
            self: "ExternalCADModelSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelSteadyStateSynchronousResponseAtASpeed",
        ) -> "ExternalCADModelSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ExternalCADModelSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2470.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6910.ExternalCADModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase

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
    ) -> "ExternalCADModelSteadyStateSynchronousResponseAtASpeed._Cast_ExternalCADModelSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ExternalCADModelSteadyStateSynchronousResponseAtASpeed(self)
