"""ExternalForceSinglePointEntity"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _137
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_FORCE_SINGLE_POINT_ENTITY = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "ExternalForceSinglePointEntity"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _147, _149


__docformat__ = "restructuredtext en"
__all__ = ("ExternalForceSinglePointEntity",)


Self = TypeVar("Self", bound="ExternalForceSinglePointEntity")


class ExternalForceSinglePointEntity(_137.ExternalForceEntity):
    """ExternalForceSinglePointEntity

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_FORCE_SINGLE_POINT_ENTITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ExternalForceSinglePointEntity")

    class _Cast_ExternalForceSinglePointEntity:
        """Special nested class for casting ExternalForceSinglePointEntity to subclasses."""

        def __init__(
            self: "ExternalForceSinglePointEntity._Cast_ExternalForceSinglePointEntity",
            parent: "ExternalForceSinglePointEntity",
        ):
            self._parent = parent

        @property
        def external_force_entity(
            self: "ExternalForceSinglePointEntity._Cast_ExternalForceSinglePointEntity",
        ) -> "_137.ExternalForceEntity":
            return self._parent._cast(_137.ExternalForceEntity)

        @property
        def nodal_component(
            self: "ExternalForceSinglePointEntity._Cast_ExternalForceSinglePointEntity",
        ) -> "_147.NodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalComponent)

        @property
        def nodal_entity(
            self: "ExternalForceSinglePointEntity._Cast_ExternalForceSinglePointEntity",
        ) -> "_149.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _149

            return self._parent._cast(_149.NodalEntity)

        @property
        def external_force_single_point_entity(
            self: "ExternalForceSinglePointEntity._Cast_ExternalForceSinglePointEntity",
        ) -> "ExternalForceSinglePointEntity":
            return self._parent

        def __getattr__(
            self: "ExternalForceSinglePointEntity._Cast_ExternalForceSinglePointEntity",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ExternalForceSinglePointEntity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ExternalForceSinglePointEntity._Cast_ExternalForceSinglePointEntity":
        return self._Cast_ExternalForceSinglePointEntity(self)
