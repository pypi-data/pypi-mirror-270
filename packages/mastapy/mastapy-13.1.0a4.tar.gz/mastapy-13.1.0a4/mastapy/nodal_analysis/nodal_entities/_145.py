"""InertialForceComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _147
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INERTIAL_FORCE_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "InertialForceComponent"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _149


__docformat__ = "restructuredtext en"
__all__ = ("InertialForceComponent",)


Self = TypeVar("Self", bound="InertialForceComponent")


class InertialForceComponent(_147.NodalComponent):
    """InertialForceComponent

    This is a mastapy class.
    """

    TYPE = _INERTIAL_FORCE_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InertialForceComponent")

    class _Cast_InertialForceComponent:
        """Special nested class for casting InertialForceComponent to subclasses."""

        def __init__(
            self: "InertialForceComponent._Cast_InertialForceComponent",
            parent: "InertialForceComponent",
        ):
            self._parent = parent

        @property
        def nodal_component(
            self: "InertialForceComponent._Cast_InertialForceComponent",
        ) -> "_147.NodalComponent":
            return self._parent._cast(_147.NodalComponent)

        @property
        def nodal_entity(
            self: "InertialForceComponent._Cast_InertialForceComponent",
        ) -> "_149.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _149

            return self._parent._cast(_149.NodalEntity)

        @property
        def inertial_force_component(
            self: "InertialForceComponent._Cast_InertialForceComponent",
        ) -> "InertialForceComponent":
            return self._parent

        def __getattr__(
            self: "InertialForceComponent._Cast_InertialForceComponent", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InertialForceComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "InertialForceComponent._Cast_InertialForceComponent":
        return self._Cast_InertialForceComponent(self)
