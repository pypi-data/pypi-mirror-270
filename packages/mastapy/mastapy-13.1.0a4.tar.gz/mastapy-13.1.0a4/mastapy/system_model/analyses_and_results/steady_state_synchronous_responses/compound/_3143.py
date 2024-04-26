"""AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3171,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3012,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3150,
        _3153,
        _3154,
        _3155,
        _3201,
        _3238,
        _3244,
        _3247,
        _3250,
        _3251,
        _3265,
        _3197,
        _3216,
        _3164,
        _3218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse"
)


class AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse(
    _3171.ConicalGearCompoundSteadyStateSynchronousResponse
):
    """AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
            parent: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3171.ConicalGearCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3171.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3197.GearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(_3197.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(
                _3216.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3164.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3164,
            )

            return self._parent._cast(
                _3164.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3150.BevelDifferentialGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3150,
            )

            return self._parent._cast(
                _3150.BevelDifferentialGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3153.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3153,
            )

            return self._parent._cast(
                _3153.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3154.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3154,
            )

            return self._parent._cast(
                _3154.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3155.BevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3155,
            )

            return self._parent._cast(
                _3155.BevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3201.HypoidGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3201,
            )

            return self._parent._cast(
                _3201.HypoidGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3238.SpiralBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3238,
            )

            return self._parent._cast(
                _3238.SpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3244.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3244,
            )

            return self._parent._cast(
                _3244.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3247.StraightBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3247,
            )

            return self._parent._cast(
                _3247.StraightBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3250.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3250,
            )

            return self._parent._cast(
                _3250.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3251.StraightBevelSunGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3251,
            )

            return self._parent._cast(
                _3251.StraightBevelSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3265.ZerolBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3265,
            )

            return self._parent._cast(
                _3265.ZerolBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
        ) -> "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3012.AGMAGleasonConicalGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AGMAGleasonConicalGearSteadyStateSynchronousResponse]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3012.AGMAGleasonConicalGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AGMAGleasonConicalGearSteadyStateSynchronousResponse]

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
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse":
        return self._Cast_AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse(
            self
        )
