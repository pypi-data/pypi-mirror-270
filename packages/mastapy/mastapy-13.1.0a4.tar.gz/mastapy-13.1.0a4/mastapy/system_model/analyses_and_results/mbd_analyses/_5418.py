"""BevelGearMeshMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5403
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "BevelGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5413,
        _5514,
        _5521,
        _5524,
        _5545,
        _5435,
        _5461,
        _5473,
        _5438,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7568, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BevelGearMeshMultibodyDynamicsAnalysis")


class BevelGearMeshMultibodyDynamicsAnalysis(
    _5403.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
):
    """BevelGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_BevelGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
            parent: "BevelGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5403.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5403.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5435.ConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(_5435.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5461.GearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461

            return self._parent._cast(_5461.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5473.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5473

            return self._parent._cast(
                _5473.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5438.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438

            return self._parent._cast(_5438.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7568.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5413.BevelDifferentialGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413

            return self._parent._cast(
                _5413.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5514.SpiralBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5514

            return self._parent._cast(
                _5514.SpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5521.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5521

            return self._parent._cast(
                _5521.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5524.StraightBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5524

            return self._parent._cast(
                _5524.StraightBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5545.ZerolBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5545

            return self._parent._cast(_5545.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "BevelGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearMeshMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2321.BevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelGearMesh

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
    ) -> "BevelGearMeshMultibodyDynamicsAnalysis._Cast_BevelGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_BevelGearMeshMultibodyDynamicsAnalysis(self)
