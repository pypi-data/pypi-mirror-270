"""BevelGearMeshCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3144,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "BevelGearMeshCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3022,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3151,
        _3239,
        _3245,
        _3248,
        _3266,
        _3172,
        _3198,
        _3204,
        _3174,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="BevelGearMeshCompoundSteadyStateSynchronousResponse")


class BevelGearMeshCompoundSteadyStateSynchronousResponse(
    _3144.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
):
    """BevelGearMeshCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting BevelGearMeshCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
            parent: "BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3144.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3144.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3172.ConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3172,
            )

            return self._parent._cast(
                _3172.ConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3198.GearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3198,
            )

            return self._parent._cast(
                _3198.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3204.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3204,
            )

            return self._parent._cast(
                _3204.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3174.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3174,
            )

            return self._parent._cast(
                _3174.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3151.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3151,
            )

            return self._parent._cast(
                _3151.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3239.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3239,
            )

            return self._parent._cast(
                _3239.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3245.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3245,
            )

            return self._parent._cast(
                _3245.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3248.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3248,
            )

            return self._parent._cast(
                _3248.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3266.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3266,
            )

            return self._parent._cast(
                _3266.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "BevelGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "BevelGearMeshCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3022.BevelGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelGearMeshSteadyStateSynchronousResponse]

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
    ) -> "List[_3022.BevelGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelGearMeshSteadyStateSynchronousResponse]

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
    ) -> "BevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse":
        return self._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponse(self)
