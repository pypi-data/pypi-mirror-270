"""BevelGearMeshSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3010,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "BevelGearMeshSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3017,
        _3106,
        _3115,
        _3118,
        _3136,
        _3038,
        _3065,
        _3072,
        _3041,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="BevelGearMeshSteadyStateSynchronousResponse")


class BevelGearMeshSteadyStateSynchronousResponse(
    _3010.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
):
    """BevelGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshSteadyStateSynchronousResponse"
    )

    class _Cast_BevelGearMeshSteadyStateSynchronousResponse:
        """Special nested class for casting BevelGearMeshSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
            parent: "BevelGearMeshSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3010.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3010.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3038.ConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3038,
            )

            return self._parent._cast(
                _3038.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3065.GearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(_3065.GearMeshSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3072.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3072,
            )

            return self._parent._cast(
                _3072.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3041.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(_3041.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3017.BevelDifferentialGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3017,
            )

            return self._parent._cast(
                _3017.BevelDifferentialGearMeshSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3106.SpiralBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3106,
            )

            return self._parent._cast(
                _3106.SpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3115.StraightBevelDiffGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3115,
            )

            return self._parent._cast(
                _3115.StraightBevelDiffGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3118.StraightBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3118,
            )

            return self._parent._cast(
                _3118.StraightBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3136.ZerolBevelGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3136,
            )

            return self._parent._cast(
                _3136.ZerolBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
        ) -> "BevelGearMeshSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "BevelGearMeshSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2321.BevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearMeshSteadyStateSynchronousResponse._Cast_BevelGearMeshSteadyStateSynchronousResponse":
        return self._Cast_BevelGearMeshSteadyStateSynchronousResponse(self)
