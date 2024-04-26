"""AGMAGleasonConicalGearTeethSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2326
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "AGMAGleasonConicalGearTeethSocket",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import (
        _2320,
        _2322,
        _2334,
        _2342,
        _2344,
        _2346,
        _2350,
        _2332,
    )
    from mastapy.system_model.connections_and_sockets import _2314


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearTeethSocket",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearTeethSocket")


class AGMAGleasonConicalGearTeethSocket(_2326.ConicalGearTeethSocket):
    """AGMAGleasonConicalGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearTeethSocket")

    class _Cast_AGMAGleasonConicalGearTeethSocket:
        """Special nested class for casting AGMAGleasonConicalGearTeethSocket to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
            parent: "AGMAGleasonConicalGearTeethSocket",
        ):
            self._parent = parent

        @property
        def conical_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ) -> "_2326.ConicalGearTeethSocket":
            return self._parent._cast(_2326.ConicalGearTeethSocket)

        @property
        def gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ) -> "_2332.GearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2332

            return self._parent._cast(_2332.GearTeethSocket)

        @property
        def socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ) -> "_2314.Socket":
            from mastapy.system_model.connections_and_sockets import _2314

            return self._parent._cast(_2314.Socket)

        @property
        def bevel_differential_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ) -> "_2320.BevelDifferentialGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.BevelDifferentialGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ) -> "_2322.BevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2322

            return self._parent._cast(_2322.BevelGearTeethSocket)

        @property
        def hypoid_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ) -> "_2334.HypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2334

            return self._parent._cast(_2334.HypoidGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ) -> "_2342.SpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2342

            return self._parent._cast(_2342.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ) -> "_2344.StraightBevelDiffGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2344

            return self._parent._cast(_2344.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ) -> "_2346.StraightBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2346

            return self._parent._cast(_2346.StraightBevelGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ) -> "_2350.ZerolBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2350

            return self._parent._cast(_2350.ZerolBevelGearTeethSocket)

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ) -> "AGMAGleasonConicalGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearTeethSocket.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket":
        return self._Cast_AGMAGleasonConicalGearTeethSocket(self)
