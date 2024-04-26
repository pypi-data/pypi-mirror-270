"""InterMountableComponentConnectionModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4915,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "InterMountableComponentConnectionModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2299
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4884,
        _4889,
        _4891,
        _4896,
        _4901,
        _4906,
        _4909,
        _4912,
        _4917,
        _4920,
        _4927,
        _4934,
        _4939,
        _4943,
        _4947,
        _4950,
        _4953,
        _4962,
        _4972,
        _4974,
        _4981,
        _4984,
        _4987,
        _4990,
        _4999,
        _5005,
        _5008,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionModalAnalysisAtAStiffness"
)


class InterMountableComponentConnectionModalAnalysisAtAStiffness(
    _4915.ConnectionModalAnalysisAtAStiffness
):
    """InterMountableComponentConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
    )

    class _Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting InterMountableComponentConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
            parent: "InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4915.ConnectionModalAnalysisAtAStiffness":
            return self._parent._cast(_4915.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4884.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4884,
            )

            return self._parent._cast(
                _4884.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def belt_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4889.BeltConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4889,
            )

            return self._parent._cast(_4889.BeltConnectionModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4891.BevelDifferentialGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4891,
            )

            return self._parent._cast(
                _4891.BevelDifferentialGearMeshModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4896.BevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4896,
            )

            return self._parent._cast(_4896.BevelGearMeshModalAnalysisAtAStiffness)

        @property
        def clutch_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4901.ClutchConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4901,
            )

            return self._parent._cast(_4901.ClutchConnectionModalAnalysisAtAStiffness)

        @property
        def concept_coupling_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4906.ConceptCouplingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4906,
            )

            return self._parent._cast(
                _4906.ConceptCouplingConnectionModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4909.ConceptGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4909,
            )

            return self._parent._cast(_4909.ConceptGearMeshModalAnalysisAtAStiffness)

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4912.ConicalGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4912,
            )

            return self._parent._cast(_4912.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def coupling_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4917.CouplingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4917,
            )

            return self._parent._cast(_4917.CouplingConnectionModalAnalysisAtAStiffness)

        @property
        def cvt_belt_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4920.CVTBeltConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4920,
            )

            return self._parent._cast(_4920.CVTBeltConnectionModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4927.CylindricalGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4927,
            )

            return self._parent._cast(
                _4927.CylindricalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def face_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4934.FaceGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4934,
            )

            return self._parent._cast(_4934.FaceGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4939.GearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4939,
            )

            return self._parent._cast(_4939.GearMeshModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4943.HypoidGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4943,
            )

            return self._parent._cast(_4943.HypoidGearMeshModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4947.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4947,
            )

            return self._parent._cast(
                _4947.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4950.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4950,
            )

            return self._parent._cast(
                _4950.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> (
            "_4953.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4953,
            )

            return self._parent._cast(
                _4953.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4962.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4962,
            )

            return self._parent._cast(
                _4962.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness
            )

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4972.RingPinsToDiscConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4972,
            )

            return self._parent._cast(
                _4972.RingPinsToDiscConnectionModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4974.RollingRingConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4974,
            )

            return self._parent._cast(
                _4974.RollingRingConnectionModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4981.SpiralBevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4981,
            )

            return self._parent._cast(
                _4981.SpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4984.SpringDamperConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4984,
            )

            return self._parent._cast(
                _4984.SpringDamperConnectionModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4987.StraightBevelDiffGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4987,
            )

            return self._parent._cast(
                _4987.StraightBevelDiffGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4990.StraightBevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4990,
            )

            return self._parent._cast(
                _4990.StraightBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_4999.TorqueConverterConnectionModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4999,
            )

            return self._parent._cast(
                _4999.TorqueConverterConnectionModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_5005.WormGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5005,
            )

            return self._parent._cast(_5005.WormGearMeshModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "_5008.ZerolBevelGearMeshModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _5008,
            )

            return self._parent._cast(_5008.ZerolBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "InterMountableComponentConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
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
        instance_to_wrap: "InterMountableComponentConnectionModalAnalysisAtAStiffness.TYPE",
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
    ) -> "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness":
        return self._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness(
            self
        )
