"""ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3456,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3302,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3402,
        _3409,
        _3412,
        _3413,
        _3414,
        _3460,
        _3464,
        _3467,
        _3470,
        _3497,
        _3503,
        _3506,
        _3509,
        _3510,
        _3524,
        _3475,
        _3423,
        _3477,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
)


class ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft(
    _3456.GearCompoundSteadyStateSynchronousResponseOnAShaft
):
    """ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3456.GearCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3456.GearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3475.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3475,
            )

            return self._parent._cast(
                _3475.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3423.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3423,
            )

            return self._parent._cast(
                _3423.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3477.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3477,
            )

            return self._parent._cast(
                _3477.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3402.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3402,
            )

            return self._parent._cast(
                _3402.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3409.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3409,
            )

            return self._parent._cast(
                _3409.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3412.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3412,
            )

            return self._parent._cast(
                _3412.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3413.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3413,
            )

            return self._parent._cast(
                _3413.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3414.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3414,
            )

            return self._parent._cast(
                _3414.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3460.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3460,
            )

            return self._parent._cast(
                _3460.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3464.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3464,
            )

            return self._parent._cast(
                _3464.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3467.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3467,
            )

            return self._parent._cast(
                _3467.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3470.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3470,
            )

            return self._parent._cast(
                _3470.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3497.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3497,
            )

            return self._parent._cast(
                _3497.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3503.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3503,
            )

            return self._parent._cast(
                _3503.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3506.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3506,
            )

            return self._parent._cast(
                _3506.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3509.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3509,
            )

            return self._parent._cast(
                _3509.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3510.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3510,
            )

            return self._parent._cast(
                _3510.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3524.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3524,
            )

            return self._parent._cast(
                _3524.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(
        self: Self,
    ) -> "List[ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3302.ConicalGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ConicalGearSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3302.ConicalGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ConicalGearSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
