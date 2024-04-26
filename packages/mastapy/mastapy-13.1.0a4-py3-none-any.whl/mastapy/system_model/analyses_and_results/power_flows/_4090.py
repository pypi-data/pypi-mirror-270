"""ConnectionPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7567
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ConnectionPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2290
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4145,
        _4058,
        _4059,
        _4064,
        _4066,
        _4071,
        _4076,
        _4079,
        _4081,
        _4084,
        _4087,
        _4092,
        _4095,
        _4099,
        _4100,
        _4103,
        _4109,
        _4116,
        _4120,
        _4123,
        _4124,
        _4127,
        _4130,
        _4138,
        _4141,
        _4150,
        _4152,
        _4157,
        _4159,
        _4162,
        _4165,
        _4168,
        _4178,
        _4184,
        _4187,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2750
    from mastapy.system_model.analyses_and_results.analysis_cases import _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionPowerFlow",)


Self = TypeVar("Self", bound="ConnectionPowerFlow")


class ConnectionPowerFlow(_7567.ConnectionStaticLoadAnalysisCase):
    """ConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONNECTION_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionPowerFlow")

    class _Cast_ConnectionPowerFlow:
        """Special nested class for casting ConnectionPowerFlow to subclasses."""

        def __init__(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
            parent: "ConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4058.AbstractShaftToMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4058

            return self._parent._cast(
                _4058.AbstractShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4059.AGMAGleasonConicalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def belt_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4064.BeltConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4064

            return self._parent._cast(_4064.BeltConnectionPowerFlow)

        @property
        def bevel_differential_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4066.BevelDifferentialGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4066

            return self._parent._cast(_4066.BevelDifferentialGearMeshPowerFlow)

        @property
        def bevel_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4071.BevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4071

            return self._parent._cast(_4071.BevelGearMeshPowerFlow)

        @property
        def clutch_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4076.ClutchConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4076

            return self._parent._cast(_4076.ClutchConnectionPowerFlow)

        @property
        def coaxial_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4079.CoaxialConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4079

            return self._parent._cast(_4079.CoaxialConnectionPowerFlow)

        @property
        def concept_coupling_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4081.ConceptCouplingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4081

            return self._parent._cast(_4081.ConceptCouplingConnectionPowerFlow)

        @property
        def concept_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4084.ConceptGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4084

            return self._parent._cast(_4084.ConceptGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4087.ConicalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4087

            return self._parent._cast(_4087.ConicalGearMeshPowerFlow)

        @property
        def coupling_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4092.CouplingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4092

            return self._parent._cast(_4092.CouplingConnectionPowerFlow)

        @property
        def cvt_belt_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4095.CVTBeltConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.CVTBeltConnectionPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4099.CycloidalDiscCentralBearingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(
                _4099.CycloidalDiscCentralBearingConnectionPowerFlow
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4100.CycloidalDiscPlanetaryBearingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4100

            return self._parent._cast(
                _4100.CycloidalDiscPlanetaryBearingConnectionPowerFlow
            )

        @property
        def cylindrical_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4103.CylindricalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(_4103.CylindricalGearMeshPowerFlow)

        @property
        def face_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4109.FaceGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4109

            return self._parent._cast(_4109.FaceGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4116.GearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.GearMeshPowerFlow)

        @property
        def hypoid_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4120.HypoidGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.HypoidGearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4123.InterMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4123

            return self._parent._cast(_4123.InterMountableComponentConnectionPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4124.KlingelnbergCycloPalloidConicalGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4124

            return self._parent._cast(
                _4124.KlingelnbergCycloPalloidConicalGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4127.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(
                _4127.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4130.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4130

            return self._parent._cast(
                _4130.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
            )

        @property
        def part_to_part_shear_coupling_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4138.PartToPartShearCouplingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4138

            return self._parent._cast(_4138.PartToPartShearCouplingConnectionPowerFlow)

        @property
        def planetary_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4141.PlanetaryConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4141

            return self._parent._cast(_4141.PlanetaryConnectionPowerFlow)

        @property
        def ring_pins_to_disc_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4150.RingPinsToDiscConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4150

            return self._parent._cast(_4150.RingPinsToDiscConnectionPowerFlow)

        @property
        def rolling_ring_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4152.RollingRingConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4152

            return self._parent._cast(_4152.RollingRingConnectionPowerFlow)

        @property
        def shaft_to_mountable_component_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4157.ShaftToMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4157

            return self._parent._cast(
                _4157.ShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def spiral_bevel_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4159.SpiralBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4159

            return self._parent._cast(_4159.SpiralBevelGearMeshPowerFlow)

        @property
        def spring_damper_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4162.SpringDamperConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4162

            return self._parent._cast(_4162.SpringDamperConnectionPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4165.StraightBevelDiffGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4165

            return self._parent._cast(_4165.StraightBevelDiffGearMeshPowerFlow)

        @property
        def straight_bevel_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4168.StraightBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4168

            return self._parent._cast(_4168.StraightBevelGearMeshPowerFlow)

        @property
        def torque_converter_connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4178.TorqueConverterConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4178

            return self._parent._cast(_4178.TorqueConverterConnectionPowerFlow)

        @property
        def worm_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4184.WormGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4184

            return self._parent._cast(_4184.WormGearMeshPowerFlow)

        @property
        def zerol_bevel_gear_mesh_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "_4187.ZerolBevelGearMeshPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4187

            return self._parent._cast(_4187.ZerolBevelGearMeshPowerFlow)

        @property
        def connection_power_flow(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow",
        ) -> "ConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConnectionPowerFlow._Cast_ConnectionPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_loaded(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLoaded

        if temp is None:
            return False

        return temp

    @property
    def component_design(self: Self) -> "_2290.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2290.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow(self: Self) -> "_4145.PowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlow

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def torsional_system_deflection_analysis(
        self: Self,
    ) -> "_2750.ConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorsionalSystemDeflectionAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConnectionPowerFlow._Cast_ConnectionPowerFlow":
        return self._Cast_ConnectionPowerFlow(self)
