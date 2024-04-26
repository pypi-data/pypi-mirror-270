"""BevelDifferentialGearMeshModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5156
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "BevelDifferentialGearMeshModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2319
    from mastapy.system_model.analyses_and_results.static_loads import _6850
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5144,
        _5172,
        _5198,
        _5205,
        _5175,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="BevelDifferentialGearMeshModalAnalysisAtASpeed")


class BevelDifferentialGearMeshModalAnalysisAtASpeed(
    _5156.BevelGearMeshModalAnalysisAtASpeed
):
    """BevelDifferentialGearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed"
    )

    class _Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed:
        """Special nested class for casting BevelDifferentialGearMeshModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshModalAnalysisAtASpeed._Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed",
            parent: "BevelDifferentialGearMeshModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearMeshModalAnalysisAtASpeed._Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed",
        ) -> "_5156.BevelGearMeshModalAnalysisAtASpeed":
            return self._parent._cast(_5156.BevelGearMeshModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearMeshModalAnalysisAtASpeed._Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed",
        ) -> "_5144.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5144,
            )

            return self._parent._cast(
                _5144.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearMeshModalAnalysisAtASpeed._Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed",
        ) -> "_5172.ConicalGearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5172,
            )

            return self._parent._cast(_5172.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearMeshModalAnalysisAtASpeed._Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed",
        ) -> "_5198.GearMeshModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5198,
            )

            return self._parent._cast(_5198.GearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearMeshModalAnalysisAtASpeed._Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed",
        ) -> "_5205.InterMountableComponentConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(
                _5205.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearMeshModalAnalysisAtASpeed._Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed",
        ) -> "_5175.ConnectionModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5175,
            )

            return self._parent._cast(_5175.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "BevelDifferentialGearMeshModalAnalysisAtASpeed._Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelDifferentialGearMeshModalAnalysisAtASpeed._Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelDifferentialGearMeshModalAnalysisAtASpeed._Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearMeshModalAnalysisAtASpeed._Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshModalAnalysisAtASpeed._Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearMeshModalAnalysisAtASpeed._Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed",
        ) -> "BevelDifferentialGearMeshModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshModalAnalysisAtASpeed._Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed",
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
        instance_to_wrap: "BevelDifferentialGearMeshModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2319.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6850.BevelDifferentialGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase

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
    ) -> "BevelDifferentialGearMeshModalAnalysisAtASpeed._Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed":
        return self._Cast_BevelDifferentialGearMeshModalAnalysisAtASpeed(self)
