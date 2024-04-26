"""BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3668,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3541,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3673,
        _3661,
        _3689,
        _3715,
        _3734,
        _3682,
        _3736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self",
    bound="BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
)


class BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed(
    _3668.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
):
    """BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3668.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            return self._parent._cast(
                _3668.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3673.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3673,
            )

            return self._parent._cast(
                _3673.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3661.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3661,
            )

            return self._parent._cast(
                _3661.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3689.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3689,
            )

            return self._parent._cast(
                _3689.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3715.GearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3715,
            )

            return self._parent._cast(
                _3715.GearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3734.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3734,
            )

            return self._parent._cast(
                _3734.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3682,
            )

            return self._parent._cast(
                _3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3736.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> (
        "List[_3541.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed]

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
    ) -> (
        "List[_3541.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
