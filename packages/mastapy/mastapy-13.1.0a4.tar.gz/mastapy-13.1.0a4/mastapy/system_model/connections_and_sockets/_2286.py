"""BeltConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2299
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "BeltConnection"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2291, _2290
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnection",)


Self = TypeVar("Self", bound="BeltConnection")


class BeltConnection(_2299.InterMountableComponentConnection):
    """BeltConnection

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltConnection")

    class _Cast_BeltConnection:
        """Special nested class for casting BeltConnection to subclasses."""

        def __init__(
            self: "BeltConnection._Cast_BeltConnection", parent: "BeltConnection"
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection(
            self: "BeltConnection._Cast_BeltConnection",
        ) -> "_2299.InterMountableComponentConnection":
            return self._parent._cast(_2299.InterMountableComponentConnection)

        @property
        def connection(
            self: "BeltConnection._Cast_BeltConnection",
        ) -> "_2290.Connection":
            from mastapy.system_model.connections_and_sockets import _2290

            return self._parent._cast(_2290.Connection)

        @property
        def design_entity(
            self: "BeltConnection._Cast_BeltConnection",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def cvt_belt_connection(
            self: "BeltConnection._Cast_BeltConnection",
        ) -> "_2291.CVTBeltConnection":
            from mastapy.system_model.connections_and_sockets import _2291

            return self._parent._cast(_2291.CVTBeltConnection)

        @property
        def belt_connection(
            self: "BeltConnection._Cast_BeltConnection",
        ) -> "BeltConnection":
            return self._parent

        def __getattr__(self: "BeltConnection._Cast_BeltConnection", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BeltConnection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def stiffness_of_strand(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessOfStrand

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "BeltConnection._Cast_BeltConnection":
        return self._Cast_BeltConnection(self)
