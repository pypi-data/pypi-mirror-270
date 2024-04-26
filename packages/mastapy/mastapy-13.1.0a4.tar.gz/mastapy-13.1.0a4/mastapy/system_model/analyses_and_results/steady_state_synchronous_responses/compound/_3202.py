"""HypoidGearMeshCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3144,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "HypoidGearMeshCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2333
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3069,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3172,
        _3198,
        _3204,
        _3174,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="HypoidGearMeshCompoundSteadyStateSynchronousResponse")


class HypoidGearMeshCompoundSteadyStateSynchronousResponse(
    _3144.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
):
    """HypoidGearMeshCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting HypoidGearMeshCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "HypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponse",
            parent: "HypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "HypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3144.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3144.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "HypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3172.ConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3172,
            )

            return self._parent._cast(
                _3172.ConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "HypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3198.GearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3198,
            )

            return self._parent._cast(
                _3198.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "HypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3204.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3204,
            )

            return self._parent._cast(
                _3204.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "HypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3174.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3174,
            )

            return self._parent._cast(
                _3174.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "HypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "HypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "HypoidGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "HypoidGearMeshCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2333.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2333.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3069.HypoidGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.HypoidGearMeshSteadyStateSynchronousResponse]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3069.HypoidGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.HypoidGearMeshSteadyStateSynchronousResponse]

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
    def cast_to(
        self: Self,
    ) -> "HypoidGearMeshCompoundSteadyStateSynchronousResponse._Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponse":
        return self._Cast_HypoidGearMeshCompoundSteadyStateSynchronousResponse(self)
