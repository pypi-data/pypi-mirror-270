"""CVTPulleySteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3095,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "CVTPulleySteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3044,
        _3084,
        _3031,
        _3086,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleySteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CVTPulleySteadyStateSynchronousResponse")


class CVTPulleySteadyStateSynchronousResponse(
    _3095.PulleySteadyStateSynchronousResponse
):
    """CVTPulleySteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTPulleySteadyStateSynchronousResponse"
    )

    class _Cast_CVTPulleySteadyStateSynchronousResponse:
        """Special nested class for casting CVTPulleySteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
            parent: "CVTPulleySteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def pulley_steady_state_synchronous_response(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ) -> "_3095.PulleySteadyStateSynchronousResponse":
            return self._parent._cast(_3095.PulleySteadyStateSynchronousResponse)

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ) -> "_3044.CouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3044,
            )

            return self._parent._cast(_3044.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ) -> "_3084.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(
                _3084.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ) -> "_3031.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3031,
            )

            return self._parent._cast(_3031.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_pulley_steady_state_synchronous_response(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ) -> "CVTPulleySteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "CVTPulleySteadyStateSynchronousResponse.TYPE"
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
    ) -> "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse":
        return self._Cast_CVTPulleySteadyStateSynchronousResponse(self)
