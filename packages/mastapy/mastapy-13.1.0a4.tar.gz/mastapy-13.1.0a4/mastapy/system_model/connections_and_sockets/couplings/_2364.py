"""CouplingConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2299
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "CouplingConnection"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2360,
        _2362,
        _2366,
        _2368,
        _2370,
    )
    from mastapy.system_model.connections_and_sockets import _2290
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnection",)


Self = TypeVar("Self", bound="CouplingConnection")


class CouplingConnection(_2299.InterMountableComponentConnection):
    """CouplingConnection

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnection")

    class _Cast_CouplingConnection:
        """Special nested class for casting CouplingConnection to subclasses."""

        def __init__(
            self: "CouplingConnection._Cast_CouplingConnection",
            parent: "CouplingConnection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "_2299.InterMountableComponentConnection":
            return self._parent._cast(_2299.InterMountableComponentConnection)

        @property
        def connection(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "_2290.Connection":
            from mastapy.system_model.connections_and_sockets import _2290

            return self._parent._cast(_2290.Connection)

        @property
        def design_entity(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def clutch_connection(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "_2360.ClutchConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2360

            return self._parent._cast(_2360.ClutchConnection)

        @property
        def concept_coupling_connection(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "_2362.ConceptCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2362

            return self._parent._cast(_2362.ConceptCouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "_2366.PartToPartShearCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2366

            return self._parent._cast(_2366.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "_2368.SpringDamperConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2368

            return self._parent._cast(_2368.SpringDamperConnection)

        @property
        def torque_converter_connection(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "_2370.TorqueConverterConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2370

            return self._parent._cast(_2370.TorqueConverterConnection)

        @property
        def coupling_connection(
            self: "CouplingConnection._Cast_CouplingConnection",
        ) -> "CouplingConnection":
            return self._parent

        def __getattr__(self: "CouplingConnection._Cast_CouplingConnection", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingConnection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CouplingConnection._Cast_CouplingConnection":
        return self._Cast_CouplingConnection(self)
