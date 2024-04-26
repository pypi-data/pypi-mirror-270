"""ExternalCADModelSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3031,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ExternalCADModelSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2470
    from mastapy.system_model.analyses_and_results.static_loads import _6910
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3086,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ExternalCADModelSteadyStateSynchronousResponse")


class ExternalCADModelSteadyStateSynchronousResponse(
    _3031.ComponentSteadyStateSynchronousResponse
):
    """ExternalCADModelSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ExternalCADModelSteadyStateSynchronousResponse"
    )

    class _Cast_ExternalCADModelSteadyStateSynchronousResponse:
        """Special nested class for casting ExternalCADModelSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
            parent: "ExternalCADModelSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
        ) -> "_3031.ComponentSteadyStateSynchronousResponse":
            return self._parent._cast(_3031.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def external_cad_model_steady_state_synchronous_response(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
        ) -> "ExternalCADModelSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ExternalCADModelSteadyStateSynchronousResponse.TYPE",
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
    ) -> "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse":
        return self._Cast_ExternalCADModelSteadyStateSynchronousResponse(self)
