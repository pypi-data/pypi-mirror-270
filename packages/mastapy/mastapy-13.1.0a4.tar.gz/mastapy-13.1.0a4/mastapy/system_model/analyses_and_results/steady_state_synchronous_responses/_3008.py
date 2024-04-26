"""AbstractShaftSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3007,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "AbstractShaftSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3052,
        _3103,
        _3031,
        _3086,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="AbstractShaftSteadyStateSynchronousResponse")


class AbstractShaftSteadyStateSynchronousResponse(
    _3007.AbstractShaftOrHousingSteadyStateSynchronousResponse
):
    """AbstractShaftSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftSteadyStateSynchronousResponse"
    )

    class _Cast_AbstractShaftSteadyStateSynchronousResponse:
        """Special nested class for casting AbstractShaftSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
            parent: "AbstractShaftSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_3007.AbstractShaftOrHousingSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3007.AbstractShaftOrHousingSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_3031.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3031,
            )

            return self._parent._cast(_3031.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_steady_state_synchronous_response(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_3052.CycloidalDiscSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3052,
            )

            return self._parent._cast(_3052.CycloidalDiscSteadyStateSynchronousResponse)

        @property
        def shaft_steady_state_synchronous_response(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "_3103.ShaftSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3103,
            )

            return self._parent._cast(_3103.ShaftSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_steady_state_synchronous_response(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
        ) -> "AbstractShaftSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "AbstractShaftSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2453.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

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
    ) -> "AbstractShaftSteadyStateSynchronousResponse._Cast_AbstractShaftSteadyStateSynchronousResponse":
        return self._Cast_AbstractShaftSteadyStateSynchronousResponse(self)
