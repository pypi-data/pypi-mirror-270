"""KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3854
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2337
    from mastapy.system_model.analyses_and_results.static_loads import _6943
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3818,
        _3846,
        _3853,
        _3821,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis")


class KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis(
    _3854.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
        ) -> "_3854.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis":
            return self._parent._cast(
                _3854.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
            )

        @property
        def conical_gear_mesh_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
        ) -> "_3818.ConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3818,
            )

            return self._parent._cast(_3818.ConicalGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
        ) -> "_3846.GearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.GearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
        ) -> "_3853.InterMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3853,
            )

            return self._parent._cast(
                _3853.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
        ) -> "_3821.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3821,
            )

            return self._parent._cast(_3821.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis.TYPE",
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
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis(self)
