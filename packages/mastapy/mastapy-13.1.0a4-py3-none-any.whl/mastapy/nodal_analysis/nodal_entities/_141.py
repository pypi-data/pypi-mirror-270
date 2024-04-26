"""GearMeshNodalComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _148
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_NODAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "GearMeshNodalComponent"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _149


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshNodalComponent",)


Self = TypeVar("Self", bound="GearMeshNodalComponent")


class GearMeshNodalComponent(_148.NodalComposite):
    """GearMeshNodalComponent

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_NODAL_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshNodalComponent")

    class _Cast_GearMeshNodalComponent:
        """Special nested class for casting GearMeshNodalComponent to subclasses."""

        def __init__(
            self: "GearMeshNodalComponent._Cast_GearMeshNodalComponent",
            parent: "GearMeshNodalComponent",
        ):
            self._parent = parent

        @property
        def nodal_composite(
            self: "GearMeshNodalComponent._Cast_GearMeshNodalComponent",
        ) -> "_148.NodalComposite":
            return self._parent._cast(_148.NodalComposite)

        @property
        def nodal_entity(
            self: "GearMeshNodalComponent._Cast_GearMeshNodalComponent",
        ) -> "_149.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _149

            return self._parent._cast(_149.NodalEntity)

        @property
        def gear_mesh_nodal_component(
            self: "GearMeshNodalComponent._Cast_GearMeshNodalComponent",
        ) -> "GearMeshNodalComponent":
            return self._parent

        def __getattr__(
            self: "GearMeshNodalComponent._Cast_GearMeshNodalComponent", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshNodalComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearMeshNodalComponent._Cast_GearMeshNodalComponent":
        return self._Cast_GearMeshNodalComponent(self)
