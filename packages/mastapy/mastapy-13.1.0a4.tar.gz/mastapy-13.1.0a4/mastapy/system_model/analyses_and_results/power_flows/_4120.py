"""HypoidGearMeshPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4059
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "HypoidGearMeshPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.hypoid import _445
    from mastapy.system_model.connections_and_sockets.gears import _2333
    from mastapy.system_model.analyses_and_results.static_loads import _6933
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4087,
        _4116,
        _4123,
        _4090,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshPowerFlow",)


Self = TypeVar("Self", bound="HypoidGearMeshPowerFlow")


class HypoidGearMeshPowerFlow(_4059.AGMAGleasonConicalGearMeshPowerFlow):
    """HypoidGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearMeshPowerFlow")

    class _Cast_HypoidGearMeshPowerFlow:
        """Special nested class for casting HypoidGearMeshPowerFlow to subclasses."""

        def __init__(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
            parent: "HypoidGearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_4059.AGMAGleasonConicalGearMeshPowerFlow":
            return self._parent._cast(_4059.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_4087.ConicalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4087

            return self._parent._cast(_4087.ConicalGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_4116.GearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_4123.InterMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4123

            return self._parent._cast(_4123.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_4090.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4090

            return self._parent._cast(_4090.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_power_flow(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow",
        ) -> "HypoidGearMeshPowerFlow":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearMeshPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_445.HypoidGearMeshRating":
        """mastapy.gears.rating.hypoid.HypoidGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_445.HypoidGearMeshRating":
        """mastapy.gears.rating.hypoid.HypoidGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2333.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6933.HypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow":
        return self._Cast_HypoidGearMeshPowerFlow(self)
