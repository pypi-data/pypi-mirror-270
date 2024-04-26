"""ShaftSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2294
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "ShaftSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import (
        _2297,
        _2298,
        _2303,
        _2304,
        _2314,
    )
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2351,
        _2352,
        _2354,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSocket",)


Self = TypeVar("Self", bound="ShaftSocket")


class ShaftSocket(_2294.CylindricalSocket):
    """ShaftSocket

    This is a mastapy class.
    """

    TYPE = _SHAFT_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftSocket")

    class _Cast_ShaftSocket:
        """Special nested class for casting ShaftSocket to subclasses."""

        def __init__(self: "ShaftSocket._Cast_ShaftSocket", parent: "ShaftSocket"):
            self._parent = parent

        @property
        def cylindrical_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2294.CylindricalSocket":
            return self._parent._cast(_2294.CylindricalSocket)

        @property
        def socket(self: "ShaftSocket._Cast_ShaftSocket") -> "_2314.Socket":
            from mastapy.system_model.connections_and_sockets import _2314

            return self._parent._cast(_2314.Socket)

        @property
        def inner_shaft_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2297.InnerShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2297

            return self._parent._cast(_2297.InnerShaftSocket)

        @property
        def inner_shaft_socket_base(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2298.InnerShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2298

            return self._parent._cast(_2298.InnerShaftSocketBase)

        @property
        def outer_shaft_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2303.OuterShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.OuterShaftSocket)

        @property
        def outer_shaft_socket_base(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2304.OuterShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2304

            return self._parent._cast(_2304.OuterShaftSocketBase)

        @property
        def cycloidal_disc_axial_left_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2351.CycloidalDiscAxialLeftSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2351

            return self._parent._cast(_2351.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_axial_right_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2352.CycloidalDiscAxialRightSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2352

            return self._parent._cast(_2352.CycloidalDiscAxialRightSocket)

        @property
        def cycloidal_disc_inner_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2354.CycloidalDiscInnerSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2354

            return self._parent._cast(_2354.CycloidalDiscInnerSocket)

        @property
        def shaft_socket(self: "ShaftSocket._Cast_ShaftSocket") -> "ShaftSocket":
            return self._parent

        def __getattr__(self: "ShaftSocket._Cast_ShaftSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ShaftSocket._Cast_ShaftSocket":
        return self._Cast_ShaftSocket(self)
