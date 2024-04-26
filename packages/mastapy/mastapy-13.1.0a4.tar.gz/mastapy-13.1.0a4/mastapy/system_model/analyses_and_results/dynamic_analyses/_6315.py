"""BevelDifferentialGearMeshDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "BevelDifferentialGearMeshDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2319
    from mastapy.system_model.analyses_and_results.static_loads import _6850
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6308,
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
__all__ = ("BevelDifferentialGearMeshDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearMeshDynamicAnalysis")


class BevelDifferentialGearMeshDynamicAnalysis(_6320.BevelGearMeshDynamicAnalysis):
    """BevelDifferentialGearMeshDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearMeshDynamicAnalysis"
    )

    class _Cast_BevelDifferentialGearMeshDynamicAnalysis:
        """Special nested class for casting BevelDifferentialGearMeshDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
            parent: "BevelDifferentialGearMeshDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_dynamic_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ) -> "_6320.BevelGearMeshDynamicAnalysis":
            return self._parent._cast(_6320.BevelGearMeshDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ) -> "_6308.AGMAGleasonConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308

            return self._parent._cast(_6308.AGMAGleasonConicalGearMeshDynamicAnalysis)

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ) -> "_6336.ConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336

            return self._parent._cast(_6336.ConicalGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ) -> "_6364.GearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.GearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ) -> "_6370.InterMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370

            return self._parent._cast(
                _6370.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ) -> "_6338.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338

            return self._parent._cast(_6338.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ) -> "_7566.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_dynamic_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ) -> "BevelDifferentialGearMeshDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearMeshDynamicAnalysis.TYPE"
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
    ) -> "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis":
        return self._Cast_BevelDifferentialGearMeshDynamicAnalysis(self)
