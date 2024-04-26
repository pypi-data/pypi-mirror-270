"""KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6639
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
        "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2337
    from mastapy.system_model.analyses_and_results.static_loads import _6943
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6602,
        _6631,
        _6637,
        _6604,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis"
)


class KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis(
    _6639.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_6639.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis":
            return self._parent._cast(
                _6639.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_6602.ConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6602,
            )

            return self._parent._cast(_6602.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_6631.GearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.GearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_6637.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6637,
            )

            return self._parent._cast(
                _6637.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_6604.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6604,
            )

            return self._parent._cast(_6604.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2337.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6943.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase

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
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis(
            self
        )
