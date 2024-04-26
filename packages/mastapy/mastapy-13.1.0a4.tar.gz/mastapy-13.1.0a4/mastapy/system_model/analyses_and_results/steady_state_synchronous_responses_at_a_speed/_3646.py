"""TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3565,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2631
    from mastapy.system_model.analyses_and_results.static_loads import _7001
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3604,
        _3552,
        _3606,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed"
)


class TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed(
    _3565.CouplingHalfSteadyStateSynchronousResponseAtASpeed
):
    """TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
            parent: "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3565.CouplingHalfSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3565.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(
                _3604.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3552.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3552,
            )

            return self._parent._cast(
                _3552.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3606.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3606,
            )

            return self._parent._cast(_3606.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def torque_converter_pump_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
        ) -> "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2631.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_7001.TorqueConverterPumpLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase

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
    ) -> "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed(
            self
        )
