"""NullNodalEntity"""

from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.nodal_entities import _149
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NULL_NODAL_ENTITY = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "NullNodalEntity"
)


__docformat__ = "restructuredtext en"
__all__ = ("NullNodalEntity",)


Self = TypeVar("Self", bound="NullNodalEntity")


class NullNodalEntity(_149.NodalEntity):
    """NullNodalEntity

    This is a mastapy class.
    """

    TYPE = _NULL_NODAL_ENTITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NullNodalEntity")

    class _Cast_NullNodalEntity:
        """Special nested class for casting NullNodalEntity to subclasses."""

        def __init__(
            self: "NullNodalEntity._Cast_NullNodalEntity", parent: "NullNodalEntity"
        ):
            self._parent = parent

        @property
        def nodal_entity(
            self: "NullNodalEntity._Cast_NullNodalEntity",
        ) -> "_149.NodalEntity":
            return self._parent._cast(_149.NodalEntity)

        @property
        def null_nodal_entity(
            self: "NullNodalEntity._Cast_NullNodalEntity",
        ) -> "NullNodalEntity":
            return self._parent

        def __getattr__(self: "NullNodalEntity._Cast_NullNodalEntity", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NullNodalEntity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "NullNodalEntity._Cast_NullNodalEntity":
        return self._Cast_NullNodalEntity(self)
