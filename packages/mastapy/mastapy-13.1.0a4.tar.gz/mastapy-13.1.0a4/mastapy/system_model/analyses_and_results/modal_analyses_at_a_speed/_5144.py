"""AGMAGleasonConicalGearMeshModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5172
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2317
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5151,
        _5156,
        _5202,
        _5240,
        _5246,
        _5249,
        _5267,
        _5198,
        _5205,
        _5175,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshModalAnalysisAtASpeed")


class AGMAGleasonConicalGearMeshModalAnalysisAtASpeed(
    _5172.ConicalGearMeshModalAnalysisAtASpeed
):
    """AGMAGleasonConicalGearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed"
    )

    class _Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed:
        """Special nested class for casting AGMAGleasonConicalGearMeshModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
            parent: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5172.ConicalGearMeshModalAnalysisAtASpeed":
            return self._parent._cast(_5172.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5198.GearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5198,
            )

            return self._parent._cast(_5198.GearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5205.InterMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(
                _5205.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5175.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5175,
            )

            return self._parent._cast(_5175.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5151.BevelDifferentialGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5151,
            )

            return self._parent._cast(
                _5151.BevelDifferentialGearMeshModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5156.BevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5156,
            )

            return self._parent._cast(_5156.BevelGearMeshModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5202.HypoidGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5202,
            )

            return self._parent._cast(_5202.HypoidGearMeshModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5240.SpiralBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5240,
            )

            return self._parent._cast(_5240.SpiralBevelGearMeshModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5246.StraightBevelDiffGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5246,
            )

            return self._parent._cast(
                _5246.StraightBevelDiffGearMeshModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5249.StraightBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5249,
            )

            return self._parent._cast(_5249.StraightBevelGearMeshModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ) -> "_5267.ZerolBevelGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5267,
            )

            return self._parent._cast(_5267.ZerolBevelGearMeshModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
        ) -> "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2317.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

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
    ) -> "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed":
        return self._Cast_AGMAGleasonConicalGearMeshModalAnalysisAtASpeed(self)
