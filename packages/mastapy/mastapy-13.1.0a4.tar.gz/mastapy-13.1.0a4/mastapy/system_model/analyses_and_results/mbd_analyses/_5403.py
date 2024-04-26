"""AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5435
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2317
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5413,
        _5418,
        _5466,
        _5514,
        _5521,
        _5524,
        _5545,
        _5461,
        _5473,
        _5438,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7568, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis")


class AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis(
    _5435.ConicalGearMeshMultibodyDynamicsAnalysis
):
    """AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
            parent: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5435.ConicalGearMeshMultibodyDynamicsAnalysis":
            return self._parent._cast(_5435.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5461.GearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461

            return self._parent._cast(_5461.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5473.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5473

            return self._parent._cast(
                _5473.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5438.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438

            return self._parent._cast(_5438.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7568.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5413.BevelDifferentialGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413

            return self._parent._cast(
                _5413.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5418.BevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5418

            return self._parent._cast(_5418.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5466.HypoidGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(_5466.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5514.SpiralBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5514

            return self._parent._cast(
                _5514.SpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5521.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5521

            return self._parent._cast(
                _5521.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5524.StraightBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5524

            return self._parent._cast(
                _5524.StraightBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5545.ZerolBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5545

            return self._parent._cast(_5545.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis.TYPE",
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
    ) -> "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis(self)
