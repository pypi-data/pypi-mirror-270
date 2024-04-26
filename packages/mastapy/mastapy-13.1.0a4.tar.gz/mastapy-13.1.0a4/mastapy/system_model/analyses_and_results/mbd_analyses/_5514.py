"""SpiralBevelGearMeshMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5418
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "SpiralBevelGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2341
    from mastapy.system_model.analyses_and_results.static_loads import _6981
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5403,
        _5435,
        _5461,
        _5473,
        _5438,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7568, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshMultibodyDynamicsAnalysis")


class SpiralBevelGearMeshMultibodyDynamicsAnalysis(
    _5418.BevelGearMeshMultibodyDynamicsAnalysis
):
    """SpiralBevelGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting SpiralBevelGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
            parent: "SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5418.BevelGearMeshMultibodyDynamicsAnalysis":
            return self._parent._cast(_5418.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5403.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(
                _5403.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5435.ConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(_5435.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5461.GearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461

            return self._parent._cast(_5461.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5473.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5473

            return self._parent._cast(
                _5473.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5438.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438

            return self._parent._cast(_5438.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7568.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "SpiralBevelGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "SpiralBevelGearMeshMultibodyDynamicsAnalysis.TYPE",
    ):
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
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis(self)
