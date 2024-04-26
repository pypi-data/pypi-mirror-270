"""ConicalGearMeshModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5198
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "ConicalGearMeshModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5144,
        _5151,
        _5156,
        _5202,
        _5206,
        _5209,
        _5212,
        _5240,
        _5246,
        _5249,
        _5267,
        _5205,
        _5175,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ConicalGearMeshModalAnalysisAtASpeed")


class ConicalGearMeshModalAnalysisAtASpeed(_5198.GearMeshModalAnalysisAtASpeed):
    """ConicalGearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshModalAnalysisAtASpeed")

    class _Cast_ConicalGearMeshModalAnalysisAtASpeed:
        """Special nested class for casting ConicalGearMeshModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
            parent: "ConicalGearMeshModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5198.GearMeshModalAnalysisAtASpeed":
            return self._parent._cast(_5198.GearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5205.InterMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(
                _5205.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5175.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5175,
            )

            return self._parent._cast(_5175.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5144.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5144,
            )

            return self._parent._cast(
                _5144.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_speed(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5151.BevelDifferentialGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5151,
            )

            return self._parent._cast(
                _5151.BevelDifferentialGearMeshModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5156.BevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5156,
            )

            return self._parent._cast(_5156.BevelGearMeshModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5202.HypoidGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5202,
            )

            return self._parent._cast(_5202.HypoidGearMeshModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5206.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5206,
            )

            return self._parent._cast(
                _5206.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5209.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5209,
            )

            return self._parent._cast(
                _5209.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5212.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5212,
            )

            return self._parent._cast(
                _5212.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5240.SpiralBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5240,
            )

            return self._parent._cast(_5240.SpiralBevelGearMeshModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5246.StraightBevelDiffGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5246,
            )

            return self._parent._cast(
                _5246.StraightBevelDiffGearMeshModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5249.StraightBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5249,
            )

            return self._parent._cast(_5249.StraightBevelGearMeshModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5267.ZerolBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5267,
            )

            return self._parent._cast(_5267.ZerolBevelGearMeshModalAnalysisAtASpeed)

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
        ) -> "ConicalGearMeshModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "ConicalGearMeshModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2325.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ConicalGearMeshModalAnalysisAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "ConicalGearMeshModalAnalysisAtASpeed._Cast_ConicalGearMeshModalAnalysisAtASpeed":
        return self._Cast_ConicalGearMeshModalAnalysisAtASpeed(self)
