"""BevelGearSetCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3145,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "BevelGearSetCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3023,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3152,
        _3240,
        _3246,
        _3249,
        _3267,
        _3173,
        _3199,
        _3237,
        _3139,
        _3218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="BevelGearSetCompoundSteadyStateSynchronousResponse")


class BevelGearSetCompoundSteadyStateSynchronousResponse(
    _3145.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
):
    """BevelGearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearSetCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_BevelGearSetCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting BevelGearSetCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
            parent: "BevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3145.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3145.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3173.ConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3173,
            )

            return self._parent._cast(
                _3173.ConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3199.GearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3199,
            )

            return self._parent._cast(
                _3199.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3237.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3237,
            )

            return self._parent._cast(
                _3237.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3139.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3152.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3152,
            )

            return self._parent._cast(
                _3152.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3240.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3240,
            )

            return self._parent._cast(
                _3240.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3246.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3246,
            )

            return self._parent._cast(
                _3246.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3249.StraightBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3249,
            )

            return self._parent._cast(
                _3249.StraightBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3267.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3267,
            )

            return self._parent._cast(
                _3267.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "BevelGearSetCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "BevelGearSetCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3023.BevelGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelGearSetSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3023.BevelGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelGearSetSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse":
        return self._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse(self)
