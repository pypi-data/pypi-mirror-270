"""InterMountableComponentConnectionModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5175
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "InterMountableComponentConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2299
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5144,
        _5149,
        _5151,
        _5156,
        _5161,
        _5166,
        _5169,
        _5172,
        _5177,
        _5180,
        _5187,
        _5193,
        _5198,
        _5202,
        _5206,
        _5209,
        _5212,
        _5221,
        _5231,
        _5233,
        _5240,
        _5243,
        _5246,
        _5249,
        _5258,
        _5264,
        _5267,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionModalAnalysisAtASpeed")


class InterMountableComponentConnectionModalAnalysisAtASpeed(
    _5175.ConnectionModalAnalysisAtASpeed
):
    """InterMountableComponentConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
    )

    class _Cast_InterMountableComponentConnectionModalAnalysisAtASpeed:
        """Special nested class for casting InterMountableComponentConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
            parent: "InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5175.ConnectionModalAnalysisAtASpeed":
            return self._parent._cast(_5175.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5144.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5144,
            )

            return self._parent._cast(
                _5144.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def belt_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5149.BeltConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5149,
            )

            return self._parent._cast(_5149.BeltConnectionModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5151.BevelDifferentialGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5151,
            )

            return self._parent._cast(
                _5151.BevelDifferentialGearMeshModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5156.BevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5156,
            )

            return self._parent._cast(_5156.BevelGearMeshModalAnalysisAtASpeed)

        @property
        def clutch_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5161.ClutchConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5161,
            )

            return self._parent._cast(_5161.ClutchConnectionModalAnalysisAtASpeed)

        @property
        def concept_coupling_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5166.ConceptCouplingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5166,
            )

            return self._parent._cast(
                _5166.ConceptCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def concept_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5169.ConceptGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5169,
            )

            return self._parent._cast(_5169.ConceptGearMeshModalAnalysisAtASpeed)

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5172.ConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5172,
            )

            return self._parent._cast(_5172.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def coupling_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5177.CouplingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5177,
            )

            return self._parent._cast(_5177.CouplingConnectionModalAnalysisAtASpeed)

        @property
        def cvt_belt_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5180.CVTBeltConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5180,
            )

            return self._parent._cast(_5180.CVTBeltConnectionModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5187.CylindricalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5187,
            )

            return self._parent._cast(_5187.CylindricalGearMeshModalAnalysisAtASpeed)

        @property
        def face_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5193.FaceGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5193,
            )

            return self._parent._cast(_5193.FaceGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5198.GearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5198,
            )

            return self._parent._cast(_5198.GearMeshModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5202.HypoidGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5202,
            )

            return self._parent._cast(_5202.HypoidGearMeshModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5206.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5206,
            )

            return self._parent._cast(
                _5206.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5209.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5209,
            )

            return self._parent._cast(
                _5209.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5212.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5212,
            )

            return self._parent._cast(
                _5212.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5221.PartToPartShearCouplingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5221,
            )

            return self._parent._cast(
                _5221.PartToPartShearCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5231.RingPinsToDiscConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5231,
            )

            return self._parent._cast(
                _5231.RingPinsToDiscConnectionModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5233.RollingRingConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5233,
            )

            return self._parent._cast(_5233.RollingRingConnectionModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5240.SpiralBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5240,
            )

            return self._parent._cast(_5240.SpiralBevelGearMeshModalAnalysisAtASpeed)

        @property
        def spring_damper_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5243.SpringDamperConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5243,
            )

            return self._parent._cast(_5243.SpringDamperConnectionModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5246.StraightBevelDiffGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5246,
            )

            return self._parent._cast(
                _5246.StraightBevelDiffGearMeshModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5249.StraightBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5249,
            )

            return self._parent._cast(_5249.StraightBevelGearMeshModalAnalysisAtASpeed)

        @property
        def torque_converter_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5258.TorqueConverterConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5258,
            )

            return self._parent._cast(
                _5258.TorqueConverterConnectionModalAnalysisAtASpeed
            )

        @property
        def worm_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5264.WormGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5264,
            )

            return self._parent._cast(_5264.WormGearMeshModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "_5267.ZerolBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5267,
            )

            return self._parent._cast(_5267.ZerolBevelGearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "InterMountableComponentConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
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
        instance_to_wrap: "InterMountableComponentConnectionModalAnalysisAtASpeed.TYPE",
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
    ) -> "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed":
        return self._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed(self)
