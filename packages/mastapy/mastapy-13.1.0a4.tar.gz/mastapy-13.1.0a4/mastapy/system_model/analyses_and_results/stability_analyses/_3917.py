"""ZerolBevelGearMeshStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3802
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ZerolBevelGearMeshStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2349
    from mastapy.system_model.analyses_and_results.static_loads import _7013
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3790,
        _3818,
        _3846,
        _3853,
        _3821,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshStabilityAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshStabilityAnalysis")


class ZerolBevelGearMeshStabilityAnalysis(_3802.BevelGearMeshStabilityAnalysis):
    """ZerolBevelGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearMeshStabilityAnalysis")

    class _Cast_ZerolBevelGearMeshStabilityAnalysis:
        """Special nested class for casting ZerolBevelGearMeshStabilityAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshStabilityAnalysis._Cast_ZerolBevelGearMeshStabilityAnalysis",
            parent: "ZerolBevelGearMeshStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "ZerolBevelGearMeshStabilityAnalysis._Cast_ZerolBevelGearMeshStabilityAnalysis",
        ) -> "_3802.BevelGearMeshStabilityAnalysis":
            return self._parent._cast(_3802.BevelGearMeshStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "ZerolBevelGearMeshStabilityAnalysis._Cast_ZerolBevelGearMeshStabilityAnalysis",
        ) -> "_3790.AGMAGleasonConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "ZerolBevelGearMeshStabilityAnalysis._Cast_ZerolBevelGearMeshStabilityAnalysis",
        ) -> "_3818.ConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3818,
            )

            return self._parent._cast(_3818.ConicalGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "ZerolBevelGearMeshStabilityAnalysis._Cast_ZerolBevelGearMeshStabilityAnalysis",
        ) -> "_3846.GearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.GearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "ZerolBevelGearMeshStabilityAnalysis._Cast_ZerolBevelGearMeshStabilityAnalysis",
        ) -> "_3853.InterMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3853,
            )

            return self._parent._cast(
                _3853.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "ZerolBevelGearMeshStabilityAnalysis._Cast_ZerolBevelGearMeshStabilityAnalysis",
        ) -> "_3821.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3821,
            )

            return self._parent._cast(_3821.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ZerolBevelGearMeshStabilityAnalysis._Cast_ZerolBevelGearMeshStabilityAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ZerolBevelGearMeshStabilityAnalysis._Cast_ZerolBevelGearMeshStabilityAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ZerolBevelGearMeshStabilityAnalysis._Cast_ZerolBevelGearMeshStabilityAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearMeshStabilityAnalysis._Cast_ZerolBevelGearMeshStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshStabilityAnalysis._Cast_ZerolBevelGearMeshStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_stability_analysis(
            self: "ZerolBevelGearMeshStabilityAnalysis._Cast_ZerolBevelGearMeshStabilityAnalysis",
        ) -> "ZerolBevelGearMeshStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshStabilityAnalysis._Cast_ZerolBevelGearMeshStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ZerolBevelGearMeshStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2349.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_7013.ZerolBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase

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
    ) -> (
        "ZerolBevelGearMeshStabilityAnalysis._Cast_ZerolBevelGearMeshStabilityAnalysis"
    ):
        return self._Cast_ZerolBevelGearMeshStabilityAnalysis(self)
