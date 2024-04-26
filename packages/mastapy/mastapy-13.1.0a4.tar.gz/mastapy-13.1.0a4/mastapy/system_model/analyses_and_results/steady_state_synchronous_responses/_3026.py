"""BoltSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3031,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "BoltSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.static_loads import _6858
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3086,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BoltSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="BoltSteadyStateSynchronousResponse")


class BoltSteadyStateSynchronousResponse(_3031.ComponentSteadyStateSynchronousResponse):
    """BoltSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BOLT_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltSteadyStateSynchronousResponse")

    class _Cast_BoltSteadyStateSynchronousResponse:
        """Special nested class for casting BoltSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BoltSteadyStateSynchronousResponse._Cast_BoltSteadyStateSynchronousResponse",
            parent: "BoltSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response(
            self: "BoltSteadyStateSynchronousResponse._Cast_BoltSteadyStateSynchronousResponse",
        ) -> "_3031.ComponentSteadyStateSynchronousResponse":
            return self._parent._cast(_3031.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "BoltSteadyStateSynchronousResponse._Cast_BoltSteadyStateSynchronousResponse",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "BoltSteadyStateSynchronousResponse._Cast_BoltSteadyStateSynchronousResponse",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltSteadyStateSynchronousResponse._Cast_BoltSteadyStateSynchronousResponse",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltSteadyStateSynchronousResponse._Cast_BoltSteadyStateSynchronousResponse",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltSteadyStateSynchronousResponse._Cast_BoltSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltSteadyStateSynchronousResponse._Cast_BoltSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bolt_steady_state_synchronous_response(
            self: "BoltSteadyStateSynchronousResponse._Cast_BoltSteadyStateSynchronousResponse",
        ) -> "BoltSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BoltSteadyStateSynchronousResponse._Cast_BoltSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "BoltSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2460.Bolt":
        """mastapy.system_model.part_model.Bolt

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6858.BoltLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase

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
    ) -> "BoltSteadyStateSynchronousResponse._Cast_BoltSteadyStateSynchronousResponse":
        return self._Cast_BoltSteadyStateSynchronousResponse(self)
