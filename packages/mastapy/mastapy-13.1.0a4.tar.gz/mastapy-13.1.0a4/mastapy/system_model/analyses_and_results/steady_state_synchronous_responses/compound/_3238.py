"""SpiralBevelGearCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3155,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "SpiralBevelGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2561
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3108,
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
__all__ = ("SpiralBevelGearCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SpiralBevelGearCompoundSteadyStateSynchronousResponse")


class SpiralBevelGearCompoundSteadyStateSynchronousResponse(
    _3155.BevelGearCompoundSteadyStateSynchronousResponse
):
    """SpiralBevelGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_SpiralBevelGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting SpiralBevelGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_SpiralBevelGearCompoundSteadyStateSynchronousResponse",
            parent: "SpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_steady_state_synchronous_response(
            self: "SpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_SpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3155.BevelGearCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3155.BevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
            self: "SpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_SpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3143.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3143,
            )

            return self._parent._cast(
                _3143.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "SpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_SpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3171.ConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3171,
            )

            return self._parent._cast(
                _3171.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "SpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_SpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3197.GearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(_3197.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "SpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_SpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(
                _3216.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "SpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_SpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3164.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3164,
            )

            return self._parent._cast(
                _3164.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "SpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_SpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_SpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_SpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_SpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "SpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_SpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "SpiralBevelGearCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_SpiralBevelGearCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "SpiralBevelGearCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2561.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

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
    ) -> "List[_3108.SpiralBevelGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SpiralBevelGearSteadyStateSynchronousResponse]

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
    ) -> "List[_3108.SpiralBevelGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SpiralBevelGearSteadyStateSynchronousResponse]

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
    ) -> "SpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_SpiralBevelGearCompoundSteadyStateSynchronousResponse":
        return self._Cast_SpiralBevelGearCompoundSteadyStateSynchronousResponse(self)
