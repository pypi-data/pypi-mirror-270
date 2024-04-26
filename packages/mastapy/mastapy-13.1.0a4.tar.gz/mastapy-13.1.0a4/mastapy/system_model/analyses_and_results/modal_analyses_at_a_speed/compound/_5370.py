"""SpiralBevelGearMeshCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5287,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2341
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5240,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5275,
        _5303,
        _5329,
        _5335,
        _5305,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshCompoundModalAnalysisAtASpeed")


class SpiralBevelGearMeshCompoundModalAnalysisAtASpeed(
    _5287.BevelGearMeshCompoundModalAnalysisAtASpeed
):
    """SpiralBevelGearMeshCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed"
    )

    class _Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed:
        """Special nested class for casting SpiralBevelGearMeshCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
            parent: "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5287.BevelGearMeshCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5287.BevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5275.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5275,
            )

            return self._parent._cast(
                _5275.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5303.ConicalGearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5303,
            )

            return self._parent._cast(
                _5303.ConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5329.GearMeshCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5329,
            )

            return self._parent._cast(_5329.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5335.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5335,
            )

            return self._parent._cast(
                _5335.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_5305.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5305,
            )

            return self._parent._cast(_5305.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2341.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2341.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

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
    ) -> "List[_5240.SpiralBevelGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpiralBevelGearMeshModalAnalysisAtASpeed]

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
    ) -> "List[_5240.SpiralBevelGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpiralBevelGearMeshModalAnalysisAtASpeed]

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
    ) -> "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed":
        return self._Cast_SpiralBevelGearMeshCompoundModalAnalysisAtASpeed(self)
