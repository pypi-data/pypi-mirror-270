"""AGMAGleasonConicalGearMeshPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4087
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "AGMAGleasonConicalGearMeshPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2317
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4066,
        _4071,
        _4120,
        _4159,
        _4165,
        _4168,
        _4187,
        _4116,
        _4123,
        _4090,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshPowerFlow",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshPowerFlow")


class AGMAGleasonConicalGearMeshPowerFlow(_4087.ConicalGearMeshPowerFlow):
    """AGMAGleasonConicalGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshPowerFlow")

    class _Cast_AGMAGleasonConicalGearMeshPowerFlow:
        """Special nested class for casting AGMAGleasonConicalGearMeshPowerFlow to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
            parent: "AGMAGleasonConicalGearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_power_flow(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
        ) -> "_4087.ConicalGearMeshPowerFlow":
            return self._parent._cast(_4087.ConicalGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
        ) -> "_4116.GearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
        ) -> "_4123.InterMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4123

            return self._parent._cast(_4123.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
        ) -> "_4090.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4090

            return self._parent._cast(_4090.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_power_flow(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
        ) -> "_4066.BevelDifferentialGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4066

            return self._parent._cast(_4066.BevelDifferentialGearMeshPowerFlow)

        @property
        def bevel_gear_mesh_power_flow(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
        ) -> "_4071.BevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4071

            return self._parent._cast(_4071.BevelGearMeshPowerFlow)

        @property
        def hypoid_gear_mesh_power_flow(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
        ) -> "_4120.HypoidGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.HypoidGearMeshPowerFlow)

        @property
        def spiral_bevel_gear_mesh_power_flow(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
        ) -> "_4159.SpiralBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4159

            return self._parent._cast(_4159.SpiralBevelGearMeshPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
        ) -> "_4165.StraightBevelDiffGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4165

            return self._parent._cast(_4165.StraightBevelDiffGearMeshPowerFlow)

        @property
        def straight_bevel_gear_mesh_power_flow(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
        ) -> "_4168.StraightBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4168

            return self._parent._cast(_4168.StraightBevelGearMeshPowerFlow)

        @property
        def zerol_bevel_gear_mesh_power_flow(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
        ) -> "_4187.ZerolBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4187

            return self._parent._cast(_4187.ZerolBevelGearMeshPowerFlow)

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
        ) -> "AGMAGleasonConicalGearMeshPowerFlow":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearMeshPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2317.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

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
    ) -> (
        "AGMAGleasonConicalGearMeshPowerFlow._Cast_AGMAGleasonConicalGearMeshPowerFlow"
    ):
        return self._Cast_AGMAGleasonConicalGearMeshPowerFlow(self)
