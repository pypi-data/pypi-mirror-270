"""MountableComponentSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2294
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "MountableComponentSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import (
        _2284,
        _2285,
        _2300,
        _2301,
        _2314,
    )


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentSocket",)


Self = TypeVar("Self", bound="MountableComponentSocket")


class MountableComponentSocket(_2294.CylindricalSocket):
    """MountableComponentSocket

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentSocket")

    class _Cast_MountableComponentSocket:
        """Special nested class for casting MountableComponentSocket to subclasses."""

        def __init__(
            self: "MountableComponentSocket._Cast_MountableComponentSocket",
            parent: "MountableComponentSocket",
        ):
            self._parent = parent

        @property
        def cylindrical_socket(
            self: "MountableComponentSocket._Cast_MountableComponentSocket",
        ) -> "_2294.CylindricalSocket":
            return self._parent._cast(_2294.CylindricalSocket)

        @property
        def socket(
            self: "MountableComponentSocket._Cast_MountableComponentSocket",
        ) -> "_2314.Socket":
            from mastapy.system_model.connections_and_sockets import _2314

            return self._parent._cast(_2314.Socket)

        @property
        def bearing_inner_socket(
            self: "MountableComponentSocket._Cast_MountableComponentSocket",
        ) -> "_2284.BearingInnerSocket":
            from mastapy.system_model.connections_and_sockets import _2284

            return self._parent._cast(_2284.BearingInnerSocket)

        @property
        def bearing_outer_socket(
            self: "MountableComponentSocket._Cast_MountableComponentSocket",
        ) -> "_2285.BearingOuterSocket":
            from mastapy.system_model.connections_and_sockets import _2285

            return self._parent._cast(_2285.BearingOuterSocket)

        @property
        def mountable_component_inner_socket(
            self: "MountableComponentSocket._Cast_MountableComponentSocket",
        ) -> "_2300.MountableComponentInnerSocket":
            from mastapy.system_model.connections_and_sockets import _2300

            return self._parent._cast(_2300.MountableComponentInnerSocket)

        @property
        def mountable_component_outer_socket(
            self: "MountableComponentSocket._Cast_MountableComponentSocket",
        ) -> "_2301.MountableComponentOuterSocket":
            from mastapy.system_model.connections_and_sockets import _2301

            return self._parent._cast(_2301.MountableComponentOuterSocket)

        @property
        def mountable_component_socket(
            self: "MountableComponentSocket._Cast_MountableComponentSocket",
        ) -> "MountableComponentSocket":
            return self._parent

        def __getattr__(
            self: "MountableComponentSocket._Cast_MountableComponentSocket", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponentSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentSocket._Cast_MountableComponentSocket":
        return self._Cast_MountableComponentSocket(self)
