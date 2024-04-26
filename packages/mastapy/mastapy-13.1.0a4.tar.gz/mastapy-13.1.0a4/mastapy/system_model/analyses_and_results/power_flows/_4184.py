"""WormGearMeshPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4116
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "WormGearMeshPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.worm import _380
    from mastapy.system_model.connections_and_sockets.gears import _2347
    from mastapy.system_model.analyses_and_results.static_loads import _7010
    from mastapy.system_model.analyses_and_results.power_flows import _4123, _4090
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshPowerFlow",)


Self = TypeVar("Self", bound="WormGearMeshPowerFlow")


class WormGearMeshPowerFlow(_4116.GearMeshPowerFlow):
    """WormGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearMeshPowerFlow")

    class _Cast_WormGearMeshPowerFlow:
        """Special nested class for casting WormGearMeshPowerFlow to subclasses."""

        def __init__(
            self: "WormGearMeshPowerFlow._Cast_WormGearMeshPowerFlow",
            parent: "WormGearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_mesh_power_flow(
            self: "WormGearMeshPowerFlow._Cast_WormGearMeshPowerFlow",
        ) -> "_4116.GearMeshPowerFlow":
            return self._parent._cast(_4116.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "WormGearMeshPowerFlow._Cast_WormGearMeshPowerFlow",
        ) -> "_4123.InterMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4123

            return self._parent._cast(_4123.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "WormGearMeshPowerFlow._Cast_WormGearMeshPowerFlow",
        ) -> "_4090.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4090

            return self._parent._cast(_4090.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "WormGearMeshPowerFlow._Cast_WormGearMeshPowerFlow",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "WormGearMeshPowerFlow._Cast_WormGearMeshPowerFlow",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "WormGearMeshPowerFlow._Cast_WormGearMeshPowerFlow",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearMeshPowerFlow._Cast_WormGearMeshPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshPowerFlow._Cast_WormGearMeshPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_power_flow(
            self: "WormGearMeshPowerFlow._Cast_WormGearMeshPowerFlow",
        ) -> "WormGearMeshPowerFlow":
            return self._parent

        def __getattr__(
            self: "WormGearMeshPowerFlow._Cast_WormGearMeshPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearMeshPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_380.WormGearMeshRating":
        """mastapy.gears.rating.worm.WormGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_380.WormGearMeshRating":
        """mastapy.gears.rating.worm.WormGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2347.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_7010.WormGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "WormGearMeshPowerFlow._Cast_WormGearMeshPowerFlow":
        return self._Cast_WormGearMeshPowerFlow(self)
