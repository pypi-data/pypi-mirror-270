"""InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3562,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2299
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3531,
        _3536,
        _3538,
        _3543,
        _3548,
        _3553,
        _3556,
        _3559,
        _3564,
        _3567,
        _3574,
        _3580,
        _3585,
        _3589,
        _3593,
        _3596,
        _3599,
        _3607,
        _3617,
        _3619,
        _3626,
        _3629,
        _3633,
        _3636,
        _3645,
        _3651,
        _3654,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self",
    bound="InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
)


class InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed(
    _3562.ConnectionSteadyStateSynchronousResponseAtASpeed
):
    """InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
            parent: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3562.ConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3562.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3531.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3531,
            )

            return self._parent._cast(
                _3531.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_connection_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3536.BeltConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3536,
            )

            return self._parent._cast(
                _3536.BeltConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3538.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3538,
            )

            return self._parent._cast(
                _3538.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3543.BevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3543,
            )

            return self._parent._cast(
                _3543.BevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_connection_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3548.ClutchConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3548,
            )

            return self._parent._cast(
                _3548.ClutchConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3553.ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3553,
            )

            return self._parent._cast(
                _3553.ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3556.ConceptGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3556,
            )

            return self._parent._cast(
                _3556.ConceptGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3559.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3559,
            )

            return self._parent._cast(
                _3559.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3564.CouplingConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3564,
            )

            return self._parent._cast(
                _3564.CouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_belt_connection_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3567.CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3567,
            )

            return self._parent._cast(
                _3567.CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3574.CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3574,
            )

            return self._parent._cast(
                _3574.CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3580.FaceGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(
                _3580.FaceGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3585.GearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(
                _3585.GearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3589.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3589,
            )

            return self._parent._cast(
                _3589.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3593.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3593,
            )

            return self._parent._cast(
                _3593.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3596.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3596,
            )

            return self._parent._cast(
                _3596.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3599.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3599,
            )

            return self._parent._cast(
                _3599.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3607.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3607,
            )

            return self._parent._cast(
                _3607.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3617.RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3617,
            )

            return self._parent._cast(
                _3617.RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3619.RollingRingConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3619,
            )

            return self._parent._cast(
                _3619.RollingRingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3626.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3626,
            )

            return self._parent._cast(
                _3626.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3629.SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3629,
            )

            return self._parent._cast(
                _3629.SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3633.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3633,
            )

            return self._parent._cast(
                _3633.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3636.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3636,
            )

            return self._parent._cast(
                _3636.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3645.TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3645,
            )

            return self._parent._cast(
                _3645.TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3651.WormGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3651,
            )

            return self._parent._cast(
                _3651.WormGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3654.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3654,
            )

            return self._parent._cast(
                _3654.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2299.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

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
    ) -> "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed(
            self
        )
