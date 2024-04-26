"""ConcentricConnectionNodalComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _158
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCENTRIC_CONNECTION_NODAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "ConcentricConnectionNodalComponent"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _156, _157, _134, _148, _149


__docformat__ = "restructuredtext en"
__all__ = ("ConcentricConnectionNodalComponent",)


Self = TypeVar("Self", bound="ConcentricConnectionNodalComponent")


class ConcentricConnectionNodalComponent(_158.TwoBodyConnectionNodalComponent):
    """ConcentricConnectionNodalComponent

    This is a mastapy class.
    """

    TYPE = _CONCENTRIC_CONNECTION_NODAL_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConcentricConnectionNodalComponent")

    class _Cast_ConcentricConnectionNodalComponent:
        """Special nested class for casting ConcentricConnectionNodalComponent to subclasses."""

        def __init__(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
            parent: "ConcentricConnectionNodalComponent",
        ):
            self._parent = parent

        @property
        def two_body_connection_nodal_component(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
        ) -> "_158.TwoBodyConnectionNodalComponent":
            return self._parent._cast(_158.TwoBodyConnectionNodalComponent)

        @property
        def component_nodal_composite(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
        ) -> "_134.ComponentNodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _134

            return self._parent._cast(_134.ComponentNodalComposite)

        @property
        def nodal_composite(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
        ) -> "_148.NodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _148

            return self._parent._cast(_148.NodalComposite)

        @property
        def nodal_entity(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
        ) -> "_149.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _149

            return self._parent._cast(_149.NodalEntity)

        @property
        def torsional_friction_node_pair(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
        ) -> "_156.TorsionalFrictionNodePair":
            from mastapy.nodal_analysis.nodal_entities import _156

            return self._parent._cast(_156.TorsionalFrictionNodePair)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
        ) -> "_157.TorsionalFrictionNodePairSimpleLockedStiffness":
            from mastapy.nodal_analysis.nodal_entities import _157

            return self._parent._cast(
                _157.TorsionalFrictionNodePairSimpleLockedStiffness
            )

        @property
        def concentric_connection_nodal_component(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
        ) -> "ConcentricConnectionNodalComponent":
            return self._parent

        def __getattr__(
            self: "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "ConcentricConnectionNodalComponent.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConcentricConnectionNodalComponent._Cast_ConcentricConnectionNodalComponent":
        return self._Cast_ConcentricConnectionNodalComponent(self)
