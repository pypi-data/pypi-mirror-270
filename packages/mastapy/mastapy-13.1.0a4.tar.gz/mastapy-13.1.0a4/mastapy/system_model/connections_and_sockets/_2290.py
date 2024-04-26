"""Connection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.python_net import python_net_import
from mastapy.system_model import _2221
from mastapy._internal.cast_exception import CastException

_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_SOCKET = python_net_import("SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Socket")
_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Connection"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.connections_and_sockets import (
        _2314,
        _2283,
        _2286,
        _2287,
        _2291,
        _2299,
        _2305,
        _2310,
        _2313,
    )
    from mastapy.system_model.connections_and_sockets.gears import (
        _2317,
        _2319,
        _2321,
        _2323,
        _2325,
        _2327,
        _2329,
        _2331,
        _2333,
        _2336,
        _2337,
        _2338,
        _2341,
        _2343,
        _2345,
        _2347,
        _2349,
    )
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2353,
        _2356,
        _2359,
    )
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2360,
        _2362,
        _2364,
        _2366,
        _2368,
        _2370,
    )


__docformat__ = "restructuredtext en"
__all__ = ("Connection",)


Self = TypeVar("Self", bound="Connection")


class Connection(_2221.DesignEntity):
    """Connection

    This is a mastapy class.
    """

    TYPE = _CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Connection")

    class _Cast_Connection:
        """Special nested class for casting Connection to subclasses."""

        def __init__(self: "Connection._Cast_Connection", parent: "Connection"):
            self._parent = parent

        @property
        def design_entity(self: "Connection._Cast_Connection") -> "_2221.DesignEntity":
            return self._parent._cast(_2221.DesignEntity)

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2283.AbstractShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.AbstractShaftToMountableComponentConnection)

        @property
        def belt_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2286.BeltConnection":
            from mastapy.system_model.connections_and_sockets import _2286

            return self._parent._cast(_2286.BeltConnection)

        @property
        def coaxial_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2287.CoaxialConnection":
            from mastapy.system_model.connections_and_sockets import _2287

            return self._parent._cast(_2287.CoaxialConnection)

        @property
        def cvt_belt_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2291.CVTBeltConnection":
            from mastapy.system_model.connections_and_sockets import _2291

            return self._parent._cast(_2291.CVTBeltConnection)

        @property
        def inter_mountable_component_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2299.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2299

            return self._parent._cast(_2299.InterMountableComponentConnection)

        @property
        def planetary_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2305.PlanetaryConnection":
            from mastapy.system_model.connections_and_sockets import _2305

            return self._parent._cast(_2305.PlanetaryConnection)

        @property
        def rolling_ring_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2310.RollingRingConnection":
            from mastapy.system_model.connections_and_sockets import _2310

            return self._parent._cast(_2310.RollingRingConnection)

        @property
        def shaft_to_mountable_component_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2313.ShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2313

            return self._parent._cast(_2313.ShaftToMountableComponentConnection)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2317.AGMAGleasonConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2317

            return self._parent._cast(_2317.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2319.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2321.BevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2321

            return self._parent._cast(_2321.BevelGearMesh)

        @property
        def concept_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2323.ConceptGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.ConceptGearMesh)

        @property
        def conical_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2325.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.ConicalGearMesh)

        @property
        def cylindrical_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2327.CylindricalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.CylindricalGearMesh)

        @property
        def face_gear_mesh(self: "Connection._Cast_Connection") -> "_2329.FaceGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2329

            return self._parent._cast(_2329.FaceGearMesh)

        @property
        def gear_mesh(self: "Connection._Cast_Connection") -> "_2331.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2331

            return self._parent._cast(_2331.GearMesh)

        @property
        def hypoid_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2333.HypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2333

            return self._parent._cast(_2333.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2336.KlingelnbergCycloPalloidConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2336

            return self._parent._cast(_2336.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2337.KlingelnbergCycloPalloidHypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2337

            return self._parent._cast(_2337.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2338.KlingelnbergCycloPalloidSpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2338

            return self._parent._cast(_2338.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2341.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2341

            return self._parent._cast(_2341.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2343.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2343

            return self._parent._cast(_2343.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2345.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2345

            return self._parent._cast(_2345.StraightBevelGearMesh)

        @property
        def worm_gear_mesh(self: "Connection._Cast_Connection") -> "_2347.WormGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2347

            return self._parent._cast(_2347.WormGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2349.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2349

            return self._parent._cast(_2349.ZerolBevelGearMesh)

        @property
        def cycloidal_disc_central_bearing_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2353.CycloidalDiscCentralBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2353

            return self._parent._cast(_2353.CycloidalDiscCentralBearingConnection)

        @property
        def cycloidal_disc_planetary_bearing_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2356.CycloidalDiscPlanetaryBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2356

            return self._parent._cast(_2356.CycloidalDiscPlanetaryBearingConnection)

        @property
        def ring_pins_to_disc_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2359.RingPinsToDiscConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2359

            return self._parent._cast(_2359.RingPinsToDiscConnection)

        @property
        def clutch_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2360.ClutchConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2360

            return self._parent._cast(_2360.ClutchConnection)

        @property
        def concept_coupling_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2362.ConceptCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2362

            return self._parent._cast(_2362.ConceptCouplingConnection)

        @property
        def coupling_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2364.CouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2364

            return self._parent._cast(_2364.CouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2366.PartToPartShearCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2366

            return self._parent._cast(_2366.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2368.SpringDamperConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2368

            return self._parent._cast(_2368.SpringDamperConnection)

        @property
        def torque_converter_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2370.TorqueConverterConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2370

            return self._parent._cast(_2370.TorqueConverterConnection)

        @property
        def connection(self: "Connection._Cast_Connection") -> "Connection":
            return self._parent

        def __getattr__(self: "Connection._Cast_Connection", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Connection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_id(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionID

        if temp is None:
            return ""

        return temp

    @property
    def drawing_position(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.DrawingPosition

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @drawing_position.setter
    @enforce_parameter_types
    def drawing_position(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.DrawingPosition = value

    @property
    def speed_ratio_from_a_to_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedRatioFromAToB

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_ratio_from_a_to_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueRatioFromAToB

        if temp is None:
            return 0.0

        return temp

    @property
    def unique_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UniqueName

        if temp is None:
            return ""

        return temp

    @property
    def owner_a(self: Self) -> "_2462.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OwnerA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def owner_b(self: Self) -> "_2462.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OwnerB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def socket_a(self: Self) -> "_2314.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def socket_b(self: Self) -> "_2314.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def other_owner(self: Self, component: "_2462.Component") -> "_2462.Component":
        """mastapy.system_model.part_model.Component

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.OtherOwner(
            component.wrapped if component else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def other_socket_for_component(
        self: Self, component: "_2462.Component"
    ) -> "_2314.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.OtherSocket.Overloads[_COMPONENT](
            component.wrapped if component else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def other_socket(self: Self, socket: "_2314.Socket") -> "_2314.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)
        """
        method_result = self.wrapped.OtherSocket.Overloads[_SOCKET](
            socket.wrapped if socket else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def socket_for(self: Self, component: "_2462.Component") -> "_2314.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.SocketFor(component.wrapped if component else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "Connection._Cast_Connection":
        return self._Cast_Connection(self)
