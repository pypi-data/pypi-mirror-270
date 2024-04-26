"""ShaftToMountableComponentConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2283
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "ShaftToMountableComponentConnection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287, _2305, _2290
    from mastapy.system_model.connections_and_sockets.cycloidal import _2353
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnection",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnection")


class ShaftToMountableComponentConnection(
    _2283.AbstractShaftToMountableComponentConnection
):
    """ShaftToMountableComponentConnection

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftToMountableComponentConnection")

    class _Cast_ShaftToMountableComponentConnection:
        """Special nested class for casting ShaftToMountableComponentConnection to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
            parent: "ShaftToMountableComponentConnection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
        ) -> "_2283.AbstractShaftToMountableComponentConnection":
            return self._parent._cast(_2283.AbstractShaftToMountableComponentConnection)

        @property
        def connection(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
        ) -> "_2290.Connection":
            from mastapy.system_model.connections_and_sockets import _2290

            return self._parent._cast(_2290.Connection)

        @property
        def design_entity(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def coaxial_connection(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
        ) -> "_2287.CoaxialConnection":
            from mastapy.system_model.connections_and_sockets import _2287

            return self._parent._cast(_2287.CoaxialConnection)

        @property
        def planetary_connection(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
        ) -> "_2305.PlanetaryConnection":
            from mastapy.system_model.connections_and_sockets import _2305

            return self._parent._cast(_2305.PlanetaryConnection)

        @property
        def cycloidal_disc_central_bearing_connection(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
        ) -> "_2353.CycloidalDiscCentralBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2353

            return self._parent._cast(_2353.CycloidalDiscCentralBearingConnection)

        @property
        def shaft_to_mountable_component_connection(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
        ) -> "ShaftToMountableComponentConnection":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
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
        self: Self, instance_to_wrap: "ShaftToMountableComponentConnection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection"
    ):
        return self._Cast_ShaftToMountableComponentConnection(self)
