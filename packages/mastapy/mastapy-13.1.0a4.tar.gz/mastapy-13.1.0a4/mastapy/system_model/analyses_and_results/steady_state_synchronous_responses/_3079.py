"""KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3073,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2338
    from mastapy.system_model.analyses_and_results.static_loads import _6946
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3038,
        _3065,
        _3072,
        _3041,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
)


class KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse(
    _3073.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3073.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3073.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3038.ConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3038,
            )

            return self._parent._cast(
                _3038.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3065.GearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(_3065.GearMeshSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3072.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3072,
            )

            return self._parent._cast(
                _3072.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_3041.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(_3041.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
        ) -> (
            "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse"
        ):
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2338.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6946.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse(
            self
        )
