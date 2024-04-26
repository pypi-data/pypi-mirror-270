"""InterMountableComponentConnectionPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4090
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "InterMountableComponentConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2299
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4059,
        _4064,
        _4066,
        _4071,
        _4076,
        _4081,
        _4084,
        _4087,
        _4092,
        _4095,
        _4103,
        _4109,
        _4116,
        _4120,
        _4124,
        _4127,
        _4130,
        _4138,
        _4150,
        _4152,
        _4159,
        _4162,
        _4165,
        _4168,
        _4178,
        _4184,
        _4187,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionPowerFlow",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionPowerFlow")


class InterMountableComponentConnectionPowerFlow(_4090.ConnectionPowerFlow):
    """InterMountableComponentConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_InterMountableComponentConnectionPowerFlow"
    )

    class _Cast_InterMountableComponentConnectionPowerFlow:
        """Special nested class for casting InterMountableComponentConnectionPowerFlow to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
            parent: "InterMountableComponentConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def connection_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4090.ConnectionPowerFlow":
            return self._parent._cast(_4090.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4059.AGMAGleasonConicalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def belt_connection_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4064.BeltConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4064

            return self._parent._cast(_4064.BeltConnectionPowerFlow)

        @property
        def bevel_differential_gear_mesh_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4066.BevelDifferentialGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4066

            return self._parent._cast(_4066.BevelDifferentialGearMeshPowerFlow)

        @property
        def bevel_gear_mesh_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4071.BevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4071

            return self._parent._cast(_4071.BevelGearMeshPowerFlow)

        @property
        def clutch_connection_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4076.ClutchConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4076

            return self._parent._cast(_4076.ClutchConnectionPowerFlow)

        @property
        def concept_coupling_connection_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4081.ConceptCouplingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4081

            return self._parent._cast(_4081.ConceptCouplingConnectionPowerFlow)

        @property
        def concept_gear_mesh_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4084.ConceptGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4084

            return self._parent._cast(_4084.ConceptGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4087.ConicalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4087

            return self._parent._cast(_4087.ConicalGearMeshPowerFlow)

        @property
        def coupling_connection_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4092.CouplingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4092

            return self._parent._cast(_4092.CouplingConnectionPowerFlow)

        @property
        def cvt_belt_connection_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4095.CVTBeltConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.CVTBeltConnectionPowerFlow)

        @property
        def cylindrical_gear_mesh_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4103.CylindricalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(_4103.CylindricalGearMeshPowerFlow)

        @property
        def face_gear_mesh_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4109.FaceGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4109

            return self._parent._cast(_4109.FaceGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4116.GearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.GearMeshPowerFlow)

        @property
        def hypoid_gear_mesh_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4120.HypoidGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.HypoidGearMeshPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4124.KlingelnbergCycloPalloidConicalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4124

            return self._parent._cast(
                _4124.KlingelnbergCycloPalloidConicalGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4127.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(
                _4127.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4130.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4130

            return self._parent._cast(
                _4130.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
            )

        @property
        def part_to_part_shear_coupling_connection_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4138.PartToPartShearCouplingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4138

            return self._parent._cast(_4138.PartToPartShearCouplingConnectionPowerFlow)

        @property
        def ring_pins_to_disc_connection_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4150.RingPinsToDiscConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4150

            return self._parent._cast(_4150.RingPinsToDiscConnectionPowerFlow)

        @property
        def rolling_ring_connection_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4152.RollingRingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4152

            return self._parent._cast(_4152.RollingRingConnectionPowerFlow)

        @property
        def spiral_bevel_gear_mesh_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4159.SpiralBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4159

            return self._parent._cast(_4159.SpiralBevelGearMeshPowerFlow)

        @property
        def spring_damper_connection_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4162.SpringDamperConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4162

            return self._parent._cast(_4162.SpringDamperConnectionPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4165.StraightBevelDiffGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4165

            return self._parent._cast(_4165.StraightBevelDiffGearMeshPowerFlow)

        @property
        def straight_bevel_gear_mesh_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4168.StraightBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4168

            return self._parent._cast(_4168.StraightBevelGearMeshPowerFlow)

        @property
        def torque_converter_connection_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4178.TorqueConverterConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4178

            return self._parent._cast(_4178.TorqueConverterConnectionPowerFlow)

        @property
        def worm_gear_mesh_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4184.WormGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4184

            return self._parent._cast(_4184.WormGearMeshPowerFlow)

        @property
        def zerol_bevel_gear_mesh_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "_4187.ZerolBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4187

            return self._parent._cast(_4187.ZerolBevelGearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
        ) -> "InterMountableComponentConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
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
        self: Self, instance_to_wrap: "InterMountableComponentConnectionPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2299.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

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
    ) -> "InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow":
        return self._Cast_InterMountableComponentConnectionPowerFlow(self)
