"""ConicalGearMeshDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ConicalGearMeshDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6308,
        _6315,
        _6320,
        _6368,
        _6372,
        _6375,
        _6378,
        _6405,
        _6411,
        _6414,
        _6432,
        _6370,
        _6338,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7566,
        _7567,
        _7564,
    )
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshDynamicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMeshDynamicAnalysis")


class ConicalGearMeshDynamicAnalysis(_6364.GearMeshDynamicAnalysis):
    """ConicalGearMeshDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshDynamicAnalysis")

    class _Cast_ConicalGearMeshDynamicAnalysis:
        """Special nested class for casting ConicalGearMeshDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
            parent: "ConicalGearMeshDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_6364.GearMeshDynamicAnalysis":
            return self._parent._cast(_6364.GearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_6370.InterMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370

            return self._parent._cast(
                _6370.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_6338.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338

            return self._parent._cast(_6338.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_7566.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_6308.AGMAGleasonConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308

            return self._parent._cast(_6308.AGMAGleasonConicalGearMeshDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_6315.BevelDifferentialGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315

            return self._parent._cast(_6315.BevelDifferentialGearMeshDynamicAnalysis)

        @property
        def bevel_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_6320.BevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320

            return self._parent._cast(_6320.BevelGearMeshDynamicAnalysis)

        @property
        def hypoid_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_6368.HypoidGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6368

            return self._parent._cast(_6368.HypoidGearMeshDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_6372.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6372

            return self._parent._cast(
                _6372.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_6375.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6375

            return self._parent._cast(
                _6375.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_6378.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6378

            return self._parent._cast(
                _6378.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_6405.SpiralBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6405

            return self._parent._cast(_6405.SpiralBevelGearMeshDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_6411.StraightBevelDiffGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6411

            return self._parent._cast(_6411.StraightBevelDiffGearMeshDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_6414.StraightBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6414

            return self._parent._cast(_6414.StraightBevelGearMeshDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "_6432.ZerolBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6432

            return self._parent._cast(_6432.ZerolBevelGearMeshDynamicAnalysis)

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "ConicalGearMeshDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMeshDynamicAnalysis.TYPE"):
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
    def planetaries(self: Self) -> "List[ConicalGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearMeshDynamicAnalysis]

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
    ) -> "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis":
        return self._Cast_ConicalGearMeshDynamicAnalysis(self)
