"""CylindricalSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2314
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CylindricalSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import (
        _2284,
        _2285,
        _2292,
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
    from mastapy.system_model.connections_and_sockets.gears import _2328
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
__all__ = ("CylindricalSocket",)


Self = TypeVar("Self", bound="CylindricalSocket")


class CylindricalSocket(_2314.Socket):
    """CylindricalSocket

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalSocket")

    class _Cast_CylindricalSocket:
        """Special nested class for casting CylindricalSocket to subclasses."""

        def __init__(
            self: "CylindricalSocket._Cast_CylindricalSocket",
            parent: "CylindricalSocket",
        ):
            self._parent = parent

        @property
        def socket(self: "CylindricalSocket._Cast_CylindricalSocket") -> "_2314.Socket":
            return self._parent._cast(_2314.Socket)

        @property
        def bearing_inner_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2284.BearingInnerSocket":
            from mastapy.system_model.connections_and_sockets import _2284

            return self._parent._cast(_2284.BearingInnerSocket)

        @property
        def bearing_outer_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2285.BearingOuterSocket":
            from mastapy.system_model.connections_and_sockets import _2285

            return self._parent._cast(_2285.BearingOuterSocket)

        @property
        def cvt_pulley_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2292.CVTPulleySocket":
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.CVTPulleySocket)

        @property
        def inner_shaft_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2297.InnerShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2297

            return self._parent._cast(_2297.InnerShaftSocket)

        @property
        def inner_shaft_socket_base(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2298.InnerShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2298

            return self._parent._cast(_2298.InnerShaftSocketBase)

        @property
        def mountable_component_inner_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2300.MountableComponentInnerSocket":
            from mastapy.system_model.connections_and_sockets import _2300

            return self._parent._cast(_2300.MountableComponentInnerSocket)

        @property
        def mountable_component_outer_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2301.MountableComponentOuterSocket":
            from mastapy.system_model.connections_and_sockets import _2301

            return self._parent._cast(_2301.MountableComponentOuterSocket)

        @property
        def mountable_component_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2302.MountableComponentSocket":
            from mastapy.system_model.connections_and_sockets import _2302

            return self._parent._cast(_2302.MountableComponentSocket)

        @property
        def outer_shaft_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2303.OuterShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.OuterShaftSocket)

        @property
        def outer_shaft_socket_base(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2304.OuterShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2304

            return self._parent._cast(_2304.OuterShaftSocketBase)

        @property
        def planetary_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2306.PlanetarySocket":
            from mastapy.system_model.connections_and_sockets import _2306

            return self._parent._cast(_2306.PlanetarySocket)

        @property
        def planetary_socket_base(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2307.PlanetarySocketBase":
            from mastapy.system_model.connections_and_sockets import _2307

            return self._parent._cast(_2307.PlanetarySocketBase)

        @property
        def pulley_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2308.PulleySocket":
            from mastapy.system_model.connections_and_sockets import _2308

            return self._parent._cast(_2308.PulleySocket)

        @property
        def rolling_ring_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2311.RollingRingSocket":
            from mastapy.system_model.connections_and_sockets import _2311

            return self._parent._cast(_2311.RollingRingSocket)

        @property
        def shaft_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2312.ShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2312

            return self._parent._cast(_2312.ShaftSocket)

        @property
        def cylindrical_gear_teeth_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2328.CylindricalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.CylindricalGearTeethSocket)

        @property
        def cycloidal_disc_axial_left_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2351.CycloidalDiscAxialLeftSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2351

            return self._parent._cast(_2351.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_axial_right_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2352.CycloidalDiscAxialRightSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2352

            return self._parent._cast(_2352.CycloidalDiscAxialRightSocket)

        @property
        def cycloidal_disc_inner_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2354.CycloidalDiscInnerSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2354

            return self._parent._cast(_2354.CycloidalDiscInnerSocket)

        @property
        def cycloidal_disc_outer_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2355.CycloidalDiscOuterSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2355

            return self._parent._cast(_2355.CycloidalDiscOuterSocket)

        @property
        def cycloidal_disc_planetary_bearing_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2357.CycloidalDiscPlanetaryBearingSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2357

            return self._parent._cast(_2357.CycloidalDiscPlanetaryBearingSocket)

        @property
        def ring_pins_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2358.RingPinsSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2358

            return self._parent._cast(_2358.RingPinsSocket)

        @property
        def clutch_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2361.ClutchSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2361

            return self._parent._cast(_2361.ClutchSocket)

        @property
        def concept_coupling_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2363.ConceptCouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2363

            return self._parent._cast(_2363.ConceptCouplingSocket)

        @property
        def coupling_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2365.CouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2365

            return self._parent._cast(_2365.CouplingSocket)

        @property
        def part_to_part_shear_coupling_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2367.PartToPartShearCouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2367

            return self._parent._cast(_2367.PartToPartShearCouplingSocket)

        @property
        def spring_damper_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2369.SpringDamperSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2369

            return self._parent._cast(_2369.SpringDamperSocket)

        @property
        def torque_converter_pump_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2371.TorqueConverterPumpSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2371

            return self._parent._cast(_2371.TorqueConverterPumpSocket)

        @property
        def torque_converter_turbine_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2372.TorqueConverterTurbineSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2372

            return self._parent._cast(_2372.TorqueConverterTurbineSocket)

        @property
        def cylindrical_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "CylindricalSocket":
            return self._parent

        def __getattr__(self: "CylindricalSocket._Cast_CylindricalSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CylindricalSocket._Cast_CylindricalSocket":
        return self._Cast_CylindricalSocket(self)
