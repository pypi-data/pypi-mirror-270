"""ConicalGearTeethSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2332
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConicalGearTeethSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import (
        _2318,
        _2320,
        _2322,
        _2334,
        _2335,
        _2339,
        _2340,
        _2342,
        _2344,
        _2346,
        _2350,
    )
    from mastapy.system_model.connections_and_sockets import _2314


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearTeethSocket",)


Self = TypeVar("Self", bound="ConicalGearTeethSocket")


class ConicalGearTeethSocket(_2332.GearTeethSocket):
    """ConicalGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearTeethSocket")

    class _Cast_ConicalGearTeethSocket:
        """Special nested class for casting ConicalGearTeethSocket to subclasses."""

        def __init__(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
            parent: "ConicalGearTeethSocket",
        ):
            self._parent = parent

        @property
        def gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2332.GearTeethSocket":
            return self._parent._cast(_2332.GearTeethSocket)

        @property
        def socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2314.Socket":
            from mastapy.system_model.connections_and_sockets import _2314

            return self._parent._cast(_2314.Socket)

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2318.AGMAGleasonConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2318

            return self._parent._cast(_2318.AGMAGleasonConicalGearTeethSocket)

        @property
        def bevel_differential_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2320.BevelDifferentialGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.BevelDifferentialGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2322.BevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2322

            return self._parent._cast(_2322.BevelGearTeethSocket)

        @property
        def hypoid_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2334.HypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2334

            return self._parent._cast(_2334.HypoidGearTeethSocket)

        @property
        def klingelnberg_conical_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2335.KlingelnbergConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2335

            return self._parent._cast(_2335.KlingelnbergConicalGearTeethSocket)

        @property
        def klingelnberg_hypoid_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2339.KlingelnbergHypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2339

            return self._parent._cast(_2339.KlingelnbergHypoidGearTeethSocket)

        @property
        def klingelnberg_spiral_bevel_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2340.KlingelnbergSpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2340

            return self._parent._cast(_2340.KlingelnbergSpiralBevelGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2342.SpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2342

            return self._parent._cast(_2342.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2344.StraightBevelDiffGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2344

            return self._parent._cast(_2344.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2346.StraightBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2346

            return self._parent._cast(_2346.StraightBevelGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2350.ZerolBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2350

            return self._parent._cast(_2350.ZerolBevelGearTeethSocket)

        @property
        def conical_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "ConicalGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket":
        return self._Cast_ConicalGearTeethSocket(self)
