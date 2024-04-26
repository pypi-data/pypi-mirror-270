"""Socket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_SOCKET = python_net_import("SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Socket")

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462, _2463
    from mastapy.system_model.connections_and_sockets import (
        _2290,
        _2284,
        _2285,
        _2292,
        _2294,
        _2296,
        _2297,
        _2298,
        _2300,
        _2301,
        _2302,
        _2303,
        _2304,
        _2306,
        _2307,
        _2308,
        _2311,
        _2312,
    )
    from mastapy.system_model.connections_and_sockets.gears import (
        _2318,
        _2320,
        _2322,
        _2324,
        _2326,
        _2328,
        _2330,
        _2332,
        _2334,
        _2335,
        _2339,
        _2340,
        _2342,
        _2344,
        _2346,
        _2348,
        _2350,
    )
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2351,
        _2352,
        _2354,
        _2355,
        _2357,
        _2358,
    )
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2361,
        _2363,
        _2365,
        _2367,
        _2369,
        _2371,
        _2372,
    )


__docformat__ = "restructuredtext en"
__all__ = ("Socket",)


Self = TypeVar("Self", bound="Socket")


class Socket(_0.APIBase):
    """Socket

    This is a mastapy class.
    """

    TYPE = _SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Socket")

    class _Cast_Socket:
        """Special nested class for casting Socket to subclasses."""

        def __init__(self: "Socket._Cast_Socket", parent: "Socket"):
            self._parent = parent

        @property
        def bearing_inner_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2284.BearingInnerSocket":
            from mastapy.system_model.connections_and_sockets import _2284

            return self._parent._cast(_2284.BearingInnerSocket)

        @property
        def bearing_outer_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2285.BearingOuterSocket":
            from mastapy.system_model.connections_and_sockets import _2285

            return self._parent._cast(_2285.BearingOuterSocket)

        @property
        def cvt_pulley_socket(self: "Socket._Cast_Socket") -> "_2292.CVTPulleySocket":
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.CVTPulleySocket)

        @property
        def cylindrical_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2294.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2294

            return self._parent._cast(_2294.CylindricalSocket)

        @property
        def electric_machine_stator_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2296.ElectricMachineStatorSocket":
            from mastapy.system_model.connections_and_sockets import _2296

            return self._parent._cast(_2296.ElectricMachineStatorSocket)

        @property
        def inner_shaft_socket(self: "Socket._Cast_Socket") -> "_2297.InnerShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2297

            return self._parent._cast(_2297.InnerShaftSocket)

        @property
        def inner_shaft_socket_base(
            self: "Socket._Cast_Socket",
        ) -> "_2298.InnerShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2298

            return self._parent._cast(_2298.InnerShaftSocketBase)

        @property
        def mountable_component_inner_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2300.MountableComponentInnerSocket":
            from mastapy.system_model.connections_and_sockets import _2300

            return self._parent._cast(_2300.MountableComponentInnerSocket)

        @property
        def mountable_component_outer_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2301.MountableComponentOuterSocket":
            from mastapy.system_model.connections_and_sockets import _2301

            return self._parent._cast(_2301.MountableComponentOuterSocket)

        @property
        def mountable_component_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2302.MountableComponentSocket":
            from mastapy.system_model.connections_and_sockets import _2302

            return self._parent._cast(_2302.MountableComponentSocket)

        @property
        def outer_shaft_socket(self: "Socket._Cast_Socket") -> "_2303.OuterShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.OuterShaftSocket)

        @property
        def outer_shaft_socket_base(
            self: "Socket._Cast_Socket",
        ) -> "_2304.OuterShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2304

            return self._parent._cast(_2304.OuterShaftSocketBase)

        @property
        def planetary_socket(self: "Socket._Cast_Socket") -> "_2306.PlanetarySocket":
            from mastapy.system_model.connections_and_sockets import _2306

            return self._parent._cast(_2306.PlanetarySocket)

        @property
        def planetary_socket_base(
            self: "Socket._Cast_Socket",
        ) -> "_2307.PlanetarySocketBase":
            from mastapy.system_model.connections_and_sockets import _2307

            return self._parent._cast(_2307.PlanetarySocketBase)

        @property
        def pulley_socket(self: "Socket._Cast_Socket") -> "_2308.PulleySocket":
            from mastapy.system_model.connections_and_sockets import _2308

            return self._parent._cast(_2308.PulleySocket)

        @property
        def rolling_ring_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2311.RollingRingSocket":
            from mastapy.system_model.connections_and_sockets import _2311

            return self._parent._cast(_2311.RollingRingSocket)

        @property
        def shaft_socket(self: "Socket._Cast_Socket") -> "_2312.ShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2312

            return self._parent._cast(_2312.ShaftSocket)

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2318.AGMAGleasonConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2318

            return self._parent._cast(_2318.AGMAGleasonConicalGearTeethSocket)

        @property
        def bevel_differential_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2320.BevelDifferentialGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.BevelDifferentialGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2322.BevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2322

            return self._parent._cast(_2322.BevelGearTeethSocket)

        @property
        def concept_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2324.ConceptGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2324

            return self._parent._cast(_2324.ConceptGearTeethSocket)

        @property
        def conical_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2326.ConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2326

            return self._parent._cast(_2326.ConicalGearTeethSocket)

        @property
        def cylindrical_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2328.CylindricalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.CylindricalGearTeethSocket)

        @property
        def face_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2330.FaceGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2330

            return self._parent._cast(_2330.FaceGearTeethSocket)

        @property
        def gear_teeth_socket(self: "Socket._Cast_Socket") -> "_2332.GearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2332

            return self._parent._cast(_2332.GearTeethSocket)

        @property
        def hypoid_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2334.HypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2334

            return self._parent._cast(_2334.HypoidGearTeethSocket)

        @property
        def klingelnberg_conical_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2335.KlingelnbergConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2335

            return self._parent._cast(_2335.KlingelnbergConicalGearTeethSocket)

        @property
        def klingelnberg_hypoid_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2339.KlingelnbergHypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2339

            return self._parent._cast(_2339.KlingelnbergHypoidGearTeethSocket)

        @property
        def klingelnberg_spiral_bevel_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2340.KlingelnbergSpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2340

            return self._parent._cast(_2340.KlingelnbergSpiralBevelGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2342.SpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2342

            return self._parent._cast(_2342.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2344.StraightBevelDiffGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2344

            return self._parent._cast(_2344.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2346.StraightBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2346

            return self._parent._cast(_2346.StraightBevelGearTeethSocket)

        @property
        def worm_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2348.WormGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2348

            return self._parent._cast(_2348.WormGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2350.ZerolBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2350

            return self._parent._cast(_2350.ZerolBevelGearTeethSocket)

        @property
        def cycloidal_disc_axial_left_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2351.CycloidalDiscAxialLeftSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2351

            return self._parent._cast(_2351.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_axial_right_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2352.CycloidalDiscAxialRightSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2352

            return self._parent._cast(_2352.CycloidalDiscAxialRightSocket)

        @property
        def cycloidal_disc_inner_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2354.CycloidalDiscInnerSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2354

            return self._parent._cast(_2354.CycloidalDiscInnerSocket)

        @property
        def cycloidal_disc_outer_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2355.CycloidalDiscOuterSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2355

            return self._parent._cast(_2355.CycloidalDiscOuterSocket)

        @property
        def cycloidal_disc_planetary_bearing_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2357.CycloidalDiscPlanetaryBearingSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2357

            return self._parent._cast(_2357.CycloidalDiscPlanetaryBearingSocket)

        @property
        def ring_pins_socket(self: "Socket._Cast_Socket") -> "_2358.RingPinsSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2358

            return self._parent._cast(_2358.RingPinsSocket)

        @property
        def clutch_socket(self: "Socket._Cast_Socket") -> "_2361.ClutchSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2361

            return self._parent._cast(_2361.ClutchSocket)

        @property
        def concept_coupling_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2363.ConceptCouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2363

            return self._parent._cast(_2363.ConceptCouplingSocket)

        @property
        def coupling_socket(self: "Socket._Cast_Socket") -> "_2365.CouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2365

            return self._parent._cast(_2365.CouplingSocket)

        @property
        def part_to_part_shear_coupling_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2367.PartToPartShearCouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2367

            return self._parent._cast(_2367.PartToPartShearCouplingSocket)

        @property
        def spring_damper_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2369.SpringDamperSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2369

            return self._parent._cast(_2369.SpringDamperSocket)

        @property
        def torque_converter_pump_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2371.TorqueConverterPumpSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2371

            return self._parent._cast(_2371.TorqueConverterPumpSocket)

        @property
        def torque_converter_turbine_socket(
            self: "Socket._Cast_Socket",
        ) -> "_2372.TorqueConverterTurbineSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2372

            return self._parent._cast(_2372.TorqueConverterTurbineSocket)

        @property
        def socket(self: "Socket._Cast_Socket") -> "Socket":
            return self._parent

        def __getattr__(self: "Socket._Cast_Socket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Socket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def connected_components(self: Self) -> "List[_2462.Component]":
        """List[mastapy.system_model.part_model.Component]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectedComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connections(self: Self) -> "List[_2290.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Connections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def owner(self: Self) -> "_2462.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Owner

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def connect_to(
        self: Self, component: "_2462.Component"
    ) -> "_2463.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.ConnectTo.Overloads[_COMPONENT](
            component.wrapped if component else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def connect_to_socket(
        self: Self, socket: "Socket"
    ) -> "_2463.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)
        """
        method_result = self.wrapped.ConnectTo.Overloads[_SOCKET](
            socket.wrapped if socket else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def connection_to(self: Self, socket: "Socket") -> "_2290.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)
        """
        method_result = self.wrapped.ConnectionTo(socket.wrapped if socket else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def get_possible_sockets_to_connect_to(
        self: Self, component_to_connect_to: "_2462.Component"
    ) -> "List[Socket]":
        """List[mastapy.system_model.connections_and_sockets.Socket]

        Args:
            component_to_connect_to (mastapy.system_model.part_model.Component)
        """
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.GetPossibleSocketsToConnectTo(
                component_to_connect_to.wrapped if component_to_connect_to else None
            )
        )

    @property
    def cast_to(self: Self) -> "Socket._Cast_Socket":
        return self._Cast_Socket(self)
