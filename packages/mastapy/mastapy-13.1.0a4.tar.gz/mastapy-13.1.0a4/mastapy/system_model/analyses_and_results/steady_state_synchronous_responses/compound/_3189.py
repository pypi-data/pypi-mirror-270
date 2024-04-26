"""CylindricalPlanetGearCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3186,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3056,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3197,
        _3216,
        _3164,
        _3218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="CylindricalPlanetGearCompoundSteadyStateSynchronousResponse"
)


class CylindricalPlanetGearCompoundSteadyStateSynchronousResponse(
    _3186.CylindricalGearCompoundSteadyStateSynchronousResponse
):
    """CylindricalPlanetGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CylindricalPlanetGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
            parent: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3186.CylindricalGearCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3186.CylindricalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3197.GearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(_3197.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(
                _3216.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3164.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3164,
            )

            return self._parent._cast(
                _3164.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ) -> "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3056.CylindricalPlanetGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CylindricalPlanetGearSteadyStateSynchronousResponse]

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
    ) -> "List[_3056.CylindricalPlanetGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CylindricalPlanetGearSteadyStateSynchronousResponse]

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
    ) -> "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse":
        return self._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse(
            self
        )
