"""InnerShaftSocketBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2312
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INNER_SHAFT_SOCKET_BASE = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "InnerShaftSocketBase"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2297, _2294, _2314
    from mastapy.system_model.connections_and_sockets.cycloidal import _2351, _2354


__docformat__ = "restructuredtext en"
__all__ = ("InnerShaftSocketBase",)


Self = TypeVar("Self", bound="InnerShaftSocketBase")


class InnerShaftSocketBase(_2312.ShaftSocket):
    """InnerShaftSocketBase

    This is a mastapy class.
    """

    TYPE = _INNER_SHAFT_SOCKET_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InnerShaftSocketBase")

    class _Cast_InnerShaftSocketBase:
        """Special nested class for casting InnerShaftSocketBase to subclasses."""

        def __init__(
            self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase",
            parent: "InnerShaftSocketBase",
        ):
            self._parent = parent

        @property
        def shaft_socket(
            self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase",
        ) -> "_2312.ShaftSocket":
            return self._parent._cast(_2312.ShaftSocket)

        @property
        def cylindrical_socket(
            self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase",
        ) -> "_2294.CylindricalSocket":
            from mastapy.system_model.connections_and_sockets import _2294

            return self._parent._cast(_2294.CylindricalSocket)

        @property
        def socket(
            self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase",
        ) -> "_2314.Socket":
            from mastapy.system_model.connections_and_sockets import _2314

            return self._parent._cast(_2314.Socket)

        @property
        def inner_shaft_socket(
            self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase",
        ) -> "_2297.InnerShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2297

            return self._parent._cast(_2297.InnerShaftSocket)

        @property
        def cycloidal_disc_axial_left_socket(
            self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase",
        ) -> "_2351.CycloidalDiscAxialLeftSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2351

            return self._parent._cast(_2351.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_inner_socket(
            self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase",
        ) -> "_2354.CycloidalDiscInnerSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2354

            return self._parent._cast(_2354.CycloidalDiscInnerSocket)

        @property
        def inner_shaft_socket_base(
            self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase",
        ) -> "InnerShaftSocketBase":
            return self._parent

        def __getattr__(
            self: "InnerShaftSocketBase._Cast_InnerShaftSocketBase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InnerShaftSocketBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "InnerShaftSocketBase._Cast_InnerShaftSocketBase":
        return self._Cast_InnerShaftSocketBase(self)
