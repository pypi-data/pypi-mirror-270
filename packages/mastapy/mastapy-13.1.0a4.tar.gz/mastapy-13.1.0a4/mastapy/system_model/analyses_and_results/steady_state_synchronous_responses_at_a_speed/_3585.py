"""GearMeshSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3592,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "GearMeshSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2331
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3531,
        _3538,
        _3543,
        _3556,
        _3559,
        _3574,
        _3580,
        _3589,
        _3593,
        _3596,
        _3599,
        _3626,
        _3633,
        _3636,
        _3651,
        _3654,
        _3562,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="GearMeshSteadyStateSynchronousResponseAtASpeed")


class GearMeshSteadyStateSynchronousResponseAtASpeed(
    _3592.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
):
    """GearMeshSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMeshSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_GearMeshSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting GearMeshSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
            parent: "GearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3592.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3592.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3562.ConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3562,
            )

            return self._parent._cast(
                _3562.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3531.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3531,
            )

            return self._parent._cast(
                _3531.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3538.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3538,
            )

            return self._parent._cast(
                _3538.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3543.BevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3543,
            )

            return self._parent._cast(
                _3543.BevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3556.ConceptGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3556,
            )

            return self._parent._cast(
                _3556.ConceptGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3559.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3559,
            )

            return self._parent._cast(
                _3559.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3574.CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3574,
            )

            return self._parent._cast(
                _3574.CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3580.FaceGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(
                _3580.FaceGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3589.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3589,
            )

            return self._parent._cast(
                _3589.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3593.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3593,
            )

            return self._parent._cast(
                _3593.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3596.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3596,
            )

            return self._parent._cast(
                _3596.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3599.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3599,
            )

            return self._parent._cast(
                _3599.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3626.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3626,
            )

            return self._parent._cast(
                _3626.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3633.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3633,
            )

            return self._parent._cast(
                _3633.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3636.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3636,
            )

            return self._parent._cast(
                _3636.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3651.WormGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3651,
            )

            return self._parent._cast(
                _3651.WormGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3654.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3654,
            )

            return self._parent._cast(
                _3654.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "GearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "GearMeshSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2331.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

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
    ) -> "GearMeshSteadyStateSynchronousResponseAtASpeed._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_GearMeshSteadyStateSynchronousResponseAtASpeed(self)
