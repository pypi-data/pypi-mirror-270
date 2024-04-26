"""ExternalForceEntity"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _147
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_FORCE_ENTITY = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "ExternalForceEntity"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _138, _139, _149


__docformat__ = "restructuredtext en"
__all__ = ("ExternalForceEntity",)


Self = TypeVar("Self", bound="ExternalForceEntity")


class ExternalForceEntity(_147.NodalComponent):
    """ExternalForceEntity

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_FORCE_ENTITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ExternalForceEntity")

    class _Cast_ExternalForceEntity:
        """Special nested class for casting ExternalForceEntity to subclasses."""

        def __init__(
            self: "ExternalForceEntity._Cast_ExternalForceEntity",
            parent: "ExternalForceEntity",
        ):
            self._parent = parent

        @property
        def nodal_component(
            self: "ExternalForceEntity._Cast_ExternalForceEntity",
        ) -> "_147.NodalComponent":
            return self._parent._cast(_147.NodalComponent)

        @property
        def nodal_entity(
            self: "ExternalForceEntity._Cast_ExternalForceEntity",
        ) -> "_149.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _149

            return self._parent._cast(_149.NodalEntity)

        @property
        def external_force_line_contact_entity(
            self: "ExternalForceEntity._Cast_ExternalForceEntity",
        ) -> "_138.ExternalForceLineContactEntity":
            from mastapy.nodal_analysis.nodal_entities import _138

            return self._parent._cast(_138.ExternalForceLineContactEntity)

        @property
        def external_force_single_point_entity(
            self: "ExternalForceEntity._Cast_ExternalForceEntity",
        ) -> "_139.ExternalForceSinglePointEntity":
            from mastapy.nodal_analysis.nodal_entities import _139

            return self._parent._cast(_139.ExternalForceSinglePointEntity)

        @property
        def external_force_entity(
            self: "ExternalForceEntity._Cast_ExternalForceEntity",
        ) -> "ExternalForceEntity":
            return self._parent

        def __getattr__(
            self: "ExternalForceEntity._Cast_ExternalForceEntity", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ExternalForceEntity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ExternalForceEntity._Cast_ExternalForceEntity":
        return self._Cast_ExternalForceEntity(self)
