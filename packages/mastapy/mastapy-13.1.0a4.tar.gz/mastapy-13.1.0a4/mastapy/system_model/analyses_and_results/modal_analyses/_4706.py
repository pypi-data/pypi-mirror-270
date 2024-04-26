"""SpiralBevelGearMeshModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4611
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "SpiralBevelGearMeshModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2341
    from mastapy.system_model.analyses_and_results.static_loads import _6981
    from mastapy.system_model.analyses_and_results.system_deflections import _2830
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4599,
        _4627,
        _4658,
        _4665,
        _4630,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshModalAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshModalAnalysis")


class SpiralBevelGearMeshModalAnalysis(_4611.BevelGearMeshModalAnalysis):
    """SpiralBevelGearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearMeshModalAnalysis")

    class _Cast_SpiralBevelGearMeshModalAnalysis:
        """Special nested class for casting SpiralBevelGearMeshModalAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshModalAnalysis._Cast_SpiralBevelGearMeshModalAnalysis",
            parent: "SpiralBevelGearMeshModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_modal_analysis(
            self: "SpiralBevelGearMeshModalAnalysis._Cast_SpiralBevelGearMeshModalAnalysis",
        ) -> "_4611.BevelGearMeshModalAnalysis":
            return self._parent._cast(_4611.BevelGearMeshModalAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(
            self: "SpiralBevelGearMeshModalAnalysis._Cast_SpiralBevelGearMeshModalAnalysis",
        ) -> "_4599.AGMAGleasonConicalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.AGMAGleasonConicalGearMeshModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(
            self: "SpiralBevelGearMeshModalAnalysis._Cast_SpiralBevelGearMeshModalAnalysis",
        ) -> "_4627.ConicalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4627

            return self._parent._cast(_4627.ConicalGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(
            self: "SpiralBevelGearMeshModalAnalysis._Cast_SpiralBevelGearMeshModalAnalysis",
        ) -> "_4658.GearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.GearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "SpiralBevelGearMeshModalAnalysis._Cast_SpiralBevelGearMeshModalAnalysis",
        ) -> "_4665.InterMountableComponentConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4665

            return self._parent._cast(
                _4665.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "SpiralBevelGearMeshModalAnalysis._Cast_SpiralBevelGearMeshModalAnalysis",
        ) -> "_4630.ConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4630

            return self._parent._cast(_4630.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "SpiralBevelGearMeshModalAnalysis._Cast_SpiralBevelGearMeshModalAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshModalAnalysis._Cast_SpiralBevelGearMeshModalAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshModalAnalysis._Cast_SpiralBevelGearMeshModalAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshModalAnalysis._Cast_SpiralBevelGearMeshModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshModalAnalysis._Cast_SpiralBevelGearMeshModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_modal_analysis(
            self: "SpiralBevelGearMeshModalAnalysis._Cast_SpiralBevelGearMeshModalAnalysis",
        ) -> "SpiralBevelGearMeshModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshModalAnalysis._Cast_SpiralBevelGearMeshModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearMeshModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(self: Self) -> "_6981.SpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2830.SpiralBevelGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshModalAnalysis._Cast_SpiralBevelGearMeshModalAnalysis":
        return self._Cast_SpiralBevelGearMeshModalAnalysis(self)
