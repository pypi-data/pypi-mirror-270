"""SplineContactNodalComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _148
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPLINE_CONTACT_NODAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "SplineContactNodalComponent"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _149


__docformat__ = "restructuredtext en"
__all__ = ("SplineContactNodalComponent",)


Self = TypeVar("Self", bound="SplineContactNodalComponent")


class SplineContactNodalComponent(_148.NodalComposite):
    """SplineContactNodalComponent

    This is a mastapy class.
    """

    TYPE = _SPLINE_CONTACT_NODAL_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SplineContactNodalComponent")

    class _Cast_SplineContactNodalComponent:
        """Special nested class for casting SplineContactNodalComponent to subclasses."""

        def __init__(
            self: "SplineContactNodalComponent._Cast_SplineContactNodalComponent",
            parent: "SplineContactNodalComponent",
        ):
            self._parent = parent

        @property
        def nodal_composite(
            self: "SplineContactNodalComponent._Cast_SplineContactNodalComponent",
        ) -> "_148.NodalComposite":
            return self._parent._cast(_148.NodalComposite)

        @property
        def nodal_entity(
            self: "SplineContactNodalComponent._Cast_SplineContactNodalComponent",
        ) -> "_149.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _149

            return self._parent._cast(_149.NodalEntity)

        @property
        def spline_contact_nodal_component(
            self: "SplineContactNodalComponent._Cast_SplineContactNodalComponent",
        ) -> "SplineContactNodalComponent":
            return self._parent

        def __getattr__(
            self: "SplineContactNodalComponent._Cast_SplineContactNodalComponent",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SplineContactNodalComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_teeth_in_contact(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfTeethInContact

        if temp is None:
            return 0

        return temp

    @property
    def number_of_teeth_in_contact_left_flank(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfTeethInContactLeftFlank

        if temp is None:
            return 0

        return temp

    @property
    def number_of_teeth_in_contact_right_flank(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfTeethInContactRightFlank

        if temp is None:
            return 0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "SplineContactNodalComponent._Cast_SplineContactNodalComponent":
        return self._Cast_SplineContactNodalComponent(self)
