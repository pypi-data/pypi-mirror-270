"""ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3156,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2349
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3136,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3144,
        _3172,
        _3198,
        _3204,
        _3174,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse")


class ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse(
    _3156.BevelGearMeshCompoundSteadyStateSynchronousResponse
):
    """ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
            parent: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3156.BevelGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3156.BevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3144.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3144,
            )

            return self._parent._cast(
                _3144.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3172.ConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3172,
            )

            return self._parent._cast(
                _3172.ConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3198.GearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3198,
            )

            return self._parent._cast(
                _3198.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3204.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3204,
            )

            return self._parent._cast(
                _3204.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_3174.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3174,
            )

            return self._parent._cast(
                _3174.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2349.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2349.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

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
    ) -> "List[_3136.ZerolBevelGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ZerolBevelGearMeshSteadyStateSynchronousResponse]

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
    ) -> "List[_3136.ZerolBevelGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ZerolBevelGearMeshSteadyStateSynchronousResponse]

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
    ) -> "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse":
        return self._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse(self)
