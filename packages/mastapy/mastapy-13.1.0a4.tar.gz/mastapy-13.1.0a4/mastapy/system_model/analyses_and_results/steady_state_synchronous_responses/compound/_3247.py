"""StraightBevelGearCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3155,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "StraightBevelGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2565
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3120,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3143,
        _3171,
        _3197,
        _3216,
        _3164,
        _3218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="StraightBevelGearCompoundSteadyStateSynchronousResponse")


class StraightBevelGearCompoundSteadyStateSynchronousResponse(
    _3155.BevelGearCompoundSteadyStateSynchronousResponse
):
    """StraightBevelGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting StraightBevelGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
            parent: "StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3155.BevelGearCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3155.BevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3143.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3143,
            )

            return self._parent._cast(
                _3143.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3171.ConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3171,
            )

            return self._parent._cast(
                _3171.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3197.GearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(_3197.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(
                _3216.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3164.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3164,
            )

            return self._parent._cast(
                _3164.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "StraightBevelGearCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "StraightBevelGearCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2565.StraightBevelGear":
        """mastapy.system_model.part_model.gears.StraightBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3120.StraightBevelGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3120.StraightBevelGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse":
        return self._Cast_StraightBevelGearCompoundSteadyStateSynchronousResponse(self)
