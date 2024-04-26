"""BevelGearMeshDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "BevelGearMeshDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6315,
        _6405,
        _6411,
        _6414,
        _6432,
        _6336,
        _6364,
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
__all__ = ("BevelGearMeshDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelGearMeshDynamicAnalysis")


class BevelGearMeshDynamicAnalysis(_6308.AGMAGleasonConicalGearMeshDynamicAnalysis):
    """BevelGearMeshDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshDynamicAnalysis")

    class _Cast_BevelGearMeshDynamicAnalysis:
        """Special nested class for casting BevelGearMeshDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
            parent: "BevelGearMeshDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "_6308.AGMAGleasonConicalGearMeshDynamicAnalysis":
            return self._parent._cast(_6308.AGMAGleasonConicalGearMeshDynamicAnalysis)

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "_6336.ConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336

            return self._parent._cast(_6336.ConicalGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "_6364.GearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.GearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "_6370.InterMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370

            return self._parent._cast(
                _6370.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "_6338.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338

            return self._parent._cast(_6338.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "_7566.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "_6315.BevelDifferentialGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315

            return self._parent._cast(_6315.BevelDifferentialGearMeshDynamicAnalysis)

        @property
        def spiral_bevel_gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "_6405.SpiralBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6405

            return self._parent._cast(_6405.SpiralBevelGearMeshDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "_6411.StraightBevelDiffGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6411

            return self._parent._cast(_6411.StraightBevelDiffGearMeshDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "_6414.StraightBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6414

            return self._parent._cast(_6414.StraightBevelGearMeshDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "_6432.ZerolBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6432

            return self._parent._cast(_6432.ZerolBevelGearMeshDynamicAnalysis)

        @property
        def bevel_gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "BevelGearMeshDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMeshDynamicAnalysis.TYPE"):
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
    ) -> "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis":
        return self._Cast_BevelGearMeshDynamicAnalysis(self)
