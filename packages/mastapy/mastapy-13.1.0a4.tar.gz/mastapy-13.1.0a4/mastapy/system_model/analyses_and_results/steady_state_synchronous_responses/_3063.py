"""FEPartSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3007,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "FEPartSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.static_loads import _6914
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3031,
        _3086,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("FEPartSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="FEPartSteadyStateSynchronousResponse")


class FEPartSteadyStateSynchronousResponse(
    _3007.AbstractShaftOrHousingSteadyStateSynchronousResponse
):
    """FEPartSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _FE_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartSteadyStateSynchronousResponse")

    class _Cast_FEPartSteadyStateSynchronousResponse:
        """Special nested class for casting FEPartSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "FEPartSteadyStateSynchronousResponse._Cast_FEPartSteadyStateSynchronousResponse",
            parent: "FEPartSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response(
            self: "FEPartSteadyStateSynchronousResponse._Cast_FEPartSteadyStateSynchronousResponse",
        ) -> "_3007.AbstractShaftOrHousingSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3007.AbstractShaftOrHousingSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "FEPartSteadyStateSynchronousResponse._Cast_FEPartSteadyStateSynchronousResponse",
        ) -> "_3031.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3031,
            )

            return self._parent._cast(_3031.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "FEPartSteadyStateSynchronousResponse._Cast_FEPartSteadyStateSynchronousResponse",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "FEPartSteadyStateSynchronousResponse._Cast_FEPartSteadyStateSynchronousResponse",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FEPartSteadyStateSynchronousResponse._Cast_FEPartSteadyStateSynchronousResponse",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FEPartSteadyStateSynchronousResponse._Cast_FEPartSteadyStateSynchronousResponse",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FEPartSteadyStateSynchronousResponse._Cast_FEPartSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartSteadyStateSynchronousResponse._Cast_FEPartSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def fe_part_steady_state_synchronous_response(
            self: "FEPartSteadyStateSynchronousResponse._Cast_FEPartSteadyStateSynchronousResponse",
        ) -> "FEPartSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "FEPartSteadyStateSynchronousResponse._Cast_FEPartSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "FEPartSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2471.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6914.FEPartLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[FEPartSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.FEPartSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FEPartSteadyStateSynchronousResponse._Cast_FEPartSteadyStateSynchronousResponse":
        return self._Cast_FEPartSteadyStateSynchronousResponse(self)
