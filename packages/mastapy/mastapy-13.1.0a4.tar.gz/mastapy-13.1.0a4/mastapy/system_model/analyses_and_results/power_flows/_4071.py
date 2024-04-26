"""BevelGearMeshPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4059
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "BevelGearMeshPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4066,
        _4159,
        _4165,
        _4168,
        _4187,
        _4087,
        _4116,
        _4123,
        _4090,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshPowerFlow",)


Self = TypeVar("Self", bound="BevelGearMeshPowerFlow")


class BevelGearMeshPowerFlow(_4059.AGMAGleasonConicalGearMeshPowerFlow):
    """BevelGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshPowerFlow")

    class _Cast_BevelGearMeshPowerFlow:
        """Special nested class for casting BevelGearMeshPowerFlow to subclasses."""

        def __init__(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
            parent: "BevelGearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4059.AGMAGleasonConicalGearMeshPowerFlow":
            return self._parent._cast(_4059.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4087.ConicalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4087

            return self._parent._cast(_4087.ConicalGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4116.GearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4123.InterMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4123

            return self._parent._cast(_4123.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4090.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4090

            return self._parent._cast(_4090.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4066.BevelDifferentialGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4066

            return self._parent._cast(_4066.BevelDifferentialGearMeshPowerFlow)

        @property
        def spiral_bevel_gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4159.SpiralBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4159

            return self._parent._cast(_4159.SpiralBevelGearMeshPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4165.StraightBevelDiffGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4165

            return self._parent._cast(_4165.StraightBevelDiffGearMeshPowerFlow)

        @property
        def straight_bevel_gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4168.StraightBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4168

            return self._parent._cast(_4168.StraightBevelGearMeshPowerFlow)

        @property
        def zerol_bevel_gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "_4187.ZerolBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4187

            return self._parent._cast(_4187.ZerolBevelGearMeshPowerFlow)

        @property
        def bevel_gear_mesh_power_flow(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow",
        ) -> "BevelGearMeshPowerFlow":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMeshPowerFlow.TYPE"):
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
    def cast_to(self: Self) -> "BevelGearMeshPowerFlow._Cast_BevelGearMeshPowerFlow":
        return self._Cast_BevelGearMeshPowerFlow(self)
