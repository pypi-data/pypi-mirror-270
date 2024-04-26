"""MeasurementComponentSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3132,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "MeasurementComponentSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2481
    from mastapy.system_model.analyses_and_results.static_loads import _6949
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3084,
        _3031,
        _3086,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="MeasurementComponentSteadyStateSynchronousResponse")


class MeasurementComponentSteadyStateSynchronousResponse(
    _3132.VirtualComponentSteadyStateSynchronousResponse
):
    """MeasurementComponentSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentSteadyStateSynchronousResponse"
    )

    class _Cast_MeasurementComponentSteadyStateSynchronousResponse:
        """Special nested class for casting MeasurementComponentSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
            parent: "MeasurementComponentSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def virtual_component_steady_state_synchronous_response(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_3132.VirtualComponentSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3132.VirtualComponentSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_3084.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(
                _3084.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_3031.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3031,
            )

            return self._parent._cast(_3031.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def measurement_component_steady_state_synchronous_response(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "MeasurementComponentSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
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
        instance_to_wrap: "MeasurementComponentSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2481.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6949.MeasurementComponentLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase

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
    ) -> "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse":
        return self._Cast_MeasurementComponentSteadyStateSynchronousResponse(self)
