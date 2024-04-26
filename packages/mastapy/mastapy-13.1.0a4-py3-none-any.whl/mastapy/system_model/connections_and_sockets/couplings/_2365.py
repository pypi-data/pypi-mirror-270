"""CouplingSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2294
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "CouplingSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2361,
        _2363,
        _2367,
        _2369,
        _2371,
        _2372,
    )
    from mastapy.system_model.connections_and_sockets import _2314


__docformat__ = "restructuredtext en"
__all__ = ("CouplingSocket",)


Self = TypeVar("Self", bound="CouplingSocket")


class CouplingSocket(_2294.CylindricalSocket):
    """CouplingSocket

    This is a mastapy class.
    """

    TYPE = _COUPLING_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingSocket")

    class _Cast_CouplingSocket:
        """Special nested class for casting CouplingSocket to subclasses."""

        def __init__(
            self: "CouplingSocket._Cast_CouplingSocket", parent: "CouplingSocket"
        ):
            self._parent = parent

        @property
        def cylindrical_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ) -> "_2294.CylindricalSocket":
            return self._parent._cast(_2294.CylindricalSocket)

        @property
        def socket(self: "CouplingSocket._Cast_CouplingSocket") -> "_2314.Socket":
            from mastapy.system_model.connections_and_sockets import _2314

            return self._parent._cast(_2314.Socket)

        @property
        def clutch_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ) -> "_2361.ClutchSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2361

            return self._parent._cast(_2361.ClutchSocket)

        @property
        def concept_coupling_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ) -> "_2363.ConceptCouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2363

            return self._parent._cast(_2363.ConceptCouplingSocket)

        @property
        def part_to_part_shear_coupling_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ) -> "_2367.PartToPartShearCouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2367

            return self._parent._cast(_2367.PartToPartShearCouplingSocket)

        @property
        def spring_damper_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ) -> "_2369.SpringDamperSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2369

            return self._parent._cast(_2369.SpringDamperSocket)

        @property
        def torque_converter_pump_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ) -> "_2371.TorqueConverterPumpSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2371

            return self._parent._cast(_2371.TorqueConverterPumpSocket)

        @property
        def torque_converter_turbine_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ) -> "_2372.TorqueConverterTurbineSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2372

            return self._parent._cast(_2372.TorqueConverterTurbineSocket)

        @property
        def coupling_socket(
            self: "CouplingSocket._Cast_CouplingSocket",
        ) -> "CouplingSocket":
            return self._parent

        def __getattr__(self: "CouplingSocket._Cast_CouplingSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CouplingSocket._Cast_CouplingSocket":
        return self._Cast_CouplingSocket(self)
