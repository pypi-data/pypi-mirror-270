"""CMSNodalComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _126
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CMS_NODAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "CMSNodalComponent"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _147, _149


__docformat__ = "restructuredtext en"
__all__ = ("CMSNodalComponent",)


Self = TypeVar("Self", bound="CMSNodalComponent")


class CMSNodalComponent(_126.ArbitraryNodalComponent):
    """CMSNodalComponent

    This is a mastapy class.
    """

    TYPE = _CMS_NODAL_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CMSNodalComponent")

    class _Cast_CMSNodalComponent:
        """Special nested class for casting CMSNodalComponent to subclasses."""

        def __init__(
            self: "CMSNodalComponent._Cast_CMSNodalComponent",
            parent: "CMSNodalComponent",
        ):
            self._parent = parent

        @property
        def arbitrary_nodal_component(
            self: "CMSNodalComponent._Cast_CMSNodalComponent",
        ) -> "_126.ArbitraryNodalComponent":
            return self._parent._cast(_126.ArbitraryNodalComponent)

        @property
        def nodal_component(
            self: "CMSNodalComponent._Cast_CMSNodalComponent",
        ) -> "_147.NodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalComponent)

        @property
        def nodal_entity(
            self: "CMSNodalComponent._Cast_CMSNodalComponent",
        ) -> "_149.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _149

            return self._parent._cast(_149.NodalEntity)

        @property
        def cms_nodal_component(
            self: "CMSNodalComponent._Cast_CMSNodalComponent",
        ) -> "CMSNodalComponent":
            return self._parent

        def __getattr__(self: "CMSNodalComponent._Cast_CMSNodalComponent", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CMSNodalComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CMSNodalComponent._Cast_CMSNodalComponent":
        return self._Cast_CMSNodalComponent(self)
