"""GearMeshCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6637
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "GearMeshCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2331
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6574,
        _6581,
        _6586,
        _6599,
        _6602,
        _6620,
        _6626,
        _6635,
        _6639,
        _6642,
        _6645,
        _6672,
        _6678,
        _6681,
        _6696,
        _6699,
        _6604,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="GearMeshCriticalSpeedAnalysis")


class GearMeshCriticalSpeedAnalysis(
    _6637.InterMountableComponentConnectionCriticalSpeedAnalysis
):
    """GearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshCriticalSpeedAnalysis")

    class _Cast_GearMeshCriticalSpeedAnalysis:
        """Special nested class for casting GearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
            parent: "GearMeshCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6637.InterMountableComponentConnectionCriticalSpeedAnalysis":
            return self._parent._cast(
                _6637.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6604.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6604,
            )

            return self._parent._cast(_6604.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6574.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6574,
            )

            return self._parent._cast(
                _6574.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_mesh_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6581.BevelDifferentialGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6581,
            )

            return self._parent._cast(
                _6581.BevelDifferentialGearMeshCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6586.BevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6586,
            )

            return self._parent._cast(_6586.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def concept_gear_mesh_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6599.ConceptGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6599,
            )

            return self._parent._cast(_6599.ConceptGearMeshCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6602.ConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6602,
            )

            return self._parent._cast(_6602.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_mesh_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6620.CylindricalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6620,
            )

            return self._parent._cast(_6620.CylindricalGearMeshCriticalSpeedAnalysis)

        @property
        def face_gear_mesh_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6626.FaceGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6626,
            )

            return self._parent._cast(_6626.FaceGearMeshCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6635.HypoidGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6635,
            )

            return self._parent._cast(_6635.HypoidGearMeshCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6639.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6639,
            )

            return self._parent._cast(
                _6639.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6642.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6642,
            )

            return self._parent._cast(
                _6642.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6645.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6645,
            )

            return self._parent._cast(
                _6645.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6672.SpiralBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6672,
            )

            return self._parent._cast(_6672.SpiralBevelGearMeshCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6678.StraightBevelDiffGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6678,
            )

            return self._parent._cast(
                _6678.StraightBevelDiffGearMeshCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6681.StraightBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6681,
            )

            return self._parent._cast(_6681.StraightBevelGearMeshCriticalSpeedAnalysis)

        @property
        def worm_gear_mesh_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6696.WormGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6696,
            )

            return self._parent._cast(_6696.WormGearMeshCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "_6699.ZerolBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6699,
            )

            return self._parent._cast(_6699.ZerolBevelGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
        ) -> "GearMeshCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2331.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

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
    ) -> "GearMeshCriticalSpeedAnalysis._Cast_GearMeshCriticalSpeedAnalysis":
        return self._Cast_GearMeshCriticalSpeedAnalysis(self)
