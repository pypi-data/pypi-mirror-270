"""ZerolBevelGearTeethSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2322
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ZerolBevelGearTeethSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2318, _2326, _2332
    from mastapy.system_model.connections_and_sockets import _2314


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearTeethSocket",)


Self = TypeVar("Self", bound="ZerolBevelGearTeethSocket")


class ZerolBevelGearTeethSocket(_2322.BevelGearTeethSocket):
    """ZerolBevelGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearTeethSocket")

    class _Cast_ZerolBevelGearTeethSocket:
        """Special nested class for casting ZerolBevelGearTeethSocket to subclasses."""

        def __init__(
            self: "ZerolBevelGearTeethSocket._Cast_ZerolBevelGearTeethSocket",
            parent: "ZerolBevelGearTeethSocket",
        ):
            self._parent = parent

        @property
        def bevel_gear_teeth_socket(
            self: "ZerolBevelGearTeethSocket._Cast_ZerolBevelGearTeethSocket",
        ) -> "_2322.BevelGearTeethSocket":
            return self._parent._cast(_2322.BevelGearTeethSocket)

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "ZerolBevelGearTeethSocket._Cast_ZerolBevelGearTeethSocket",
        ) -> "_2318.AGMAGleasonConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2318

            return self._parent._cast(_2318.AGMAGleasonConicalGearTeethSocket)

        @property
        def conical_gear_teeth_socket(
            self: "ZerolBevelGearTeethSocket._Cast_ZerolBevelGearTeethSocket",
        ) -> "_2326.ConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2326

            return self._parent._cast(_2326.ConicalGearTeethSocket)

        @property
        def gear_teeth_socket(
            self: "ZerolBevelGearTeethSocket._Cast_ZerolBevelGearTeethSocket",
        ) -> "_2332.GearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2332

            return self._parent._cast(_2332.GearTeethSocket)

        @property
        def socket(
            self: "ZerolBevelGearTeethSocket._Cast_ZerolBevelGearTeethSocket",
        ) -> "_2314.Socket":
            from mastapy.system_model.connections_and_sockets import _2314

            return self._parent._cast(_2314.Socket)

        @property
        def zerol_bevel_gear_teeth_socket(
            self: "ZerolBevelGearTeethSocket._Cast_ZerolBevelGearTeethSocket",
        ) -> "ZerolBevelGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearTeethSocket._Cast_ZerolBevelGearTeethSocket", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearTeethSocket._Cast_ZerolBevelGearTeethSocket":
        return self._Cast_ZerolBevelGearTeethSocket(self)
