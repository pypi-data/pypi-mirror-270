"""AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3172,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3010,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3151,
        _3156,
        _3202,
        _3239,
        _3245,
        _3248,
        _3266,
        _3198,
        _3204,
        _3174,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse"
)


class AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse(
    _3172.ConicalGearMeshCompoundSteadyStateSynchronousResponse
):
    """AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
            parent: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3172.ConicalGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3172.ConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3198.GearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3198,
            )

            return self._parent._cast(
                _3198.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3204.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3204,
            )

            return self._parent._cast(
                _3204.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3174.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3174,
            )

            return self._parent._cast(
                _3174.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3151.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3151,
            )

            return self._parent._cast(
                _3151.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3156.BevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3156,
            )

            return self._parent._cast(
                _3156.BevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3202.HypoidGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3202,
            )

            return self._parent._cast(
                _3202.HypoidGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3239.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3239,
            )

            return self._parent._cast(
                _3239.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3245.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3245,
            )

            return self._parent._cast(
                _3245.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3248.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3248,
            )

            return self._parent._cast(
                _3248.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3266.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3266,
            )

            return self._parent._cast(
                _3266.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3010.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3010.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse":
        return (
            self._Cast_AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse(
                self
            )
        )
