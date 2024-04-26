"""ConicalGearMeshCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3198,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ConicalGearMeshCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3038,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3144,
        _3151,
        _3156,
        _3202,
        _3206,
        _3209,
        _3212,
        _3239,
        _3245,
        _3248,
        _3266,
        _3204,
        _3174,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConicalGearMeshCompoundSteadyStateSynchronousResponse")


class ConicalGearMeshCompoundSteadyStateSynchronousResponse(
    _3198.GearMeshCompoundSteadyStateSynchronousResponse
):
    """ConicalGearMeshCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ConicalGearMeshCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
            parent: "ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3198.GearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3198.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3204.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3204,
            )

            return self._parent._cast(
                _3204.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3174.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3174,
            )

            return self._parent._cast(
                _3174.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3144.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3144,
            )

            return self._parent._cast(
                _3144.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3151.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3151,
            )

            return self._parent._cast(
                _3151.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3156.BevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3156,
            )

            return self._parent._cast(
                _3156.BevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3202.HypoidGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3202,
            )

            return self._parent._cast(
                _3202.HypoidGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3206.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3206,
            )

            return self._parent._cast(
                _3206.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3209.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3209,
            )

            return self._parent._cast(
                _3209.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3212.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3212,
            )

            return self._parent._cast(
                _3212.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3239.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3239,
            )

            return self._parent._cast(
                _3239.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3245.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3245,
            )

            return self._parent._cast(
                _3245.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3248.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3248,
            )

            return self._parent._cast(
                _3248.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3266.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3266,
            )

            return self._parent._cast(
                _3266.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "ConicalGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ConicalGearMeshCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(
        self: Self,
    ) -> "List[ConicalGearMeshCompoundSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound.ConicalGearMeshCompoundSteadyStateSynchronousResponse]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3038.ConicalGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConicalGearMeshSteadyStateSynchronousResponse]

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
    ) -> "List[_3038.ConicalGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConicalGearMeshSteadyStateSynchronousResponse]

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
    ) -> "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse":
        return self._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse(self)
