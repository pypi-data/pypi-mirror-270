"""ComponentNodalComposite"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _148
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_NODAL_COMPOSITE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "ComponentNodalComposite"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import (
        _128,
        _129,
        _130,
        _135,
        _143,
        _153,
        _156,
        _157,
        _158,
        _149,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ComponentNodalComposite",)


Self = TypeVar("Self", bound="ComponentNodalComposite")


class ComponentNodalComposite(_148.NodalComposite):
    """ComponentNodalComposite

    This is a mastapy class.
    """

    TYPE = _COMPONENT_NODAL_COMPOSITE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentNodalComposite")

    class _Cast_ComponentNodalComposite:
        """Special nested class for casting ComponentNodalComposite to subclasses."""

        def __init__(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
            parent: "ComponentNodalComposite",
        ):
            self._parent = parent

        @property
        def nodal_composite(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_148.NodalComposite":
            return self._parent._cast(_148.NodalComposite)

        @property
        def nodal_entity(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_149.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _149

            return self._parent._cast(_149.NodalEntity)

        @property
        def bar_elastic_mbd(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_128.BarElasticMBD":
            from mastapy.nodal_analysis.nodal_entities import _128

            return self._parent._cast(_128.BarElasticMBD)

        @property
        def bar_mbd(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_129.BarMBD":
            from mastapy.nodal_analysis.nodal_entities import _129

            return self._parent._cast(_129.BarMBD)

        @property
        def bar_rigid_mbd(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_130.BarRigidMBD":
            from mastapy.nodal_analysis.nodal_entities import _130

            return self._parent._cast(_130.BarRigidMBD)

        @property
        def concentric_connection_nodal_component(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_135.ConcentricConnectionNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _135

            return self._parent._cast(_135.ConcentricConnectionNodalComponent)

        @property
        def gear_mesh_point_on_flank_contact(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_143.GearMeshPointOnFlankContact":
            from mastapy.nodal_analysis.nodal_entities import _143

            return self._parent._cast(_143.GearMeshPointOnFlankContact)

        @property
        def simple_bar(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_153.SimpleBar":
            from mastapy.nodal_analysis.nodal_entities import _153

            return self._parent._cast(_153.SimpleBar)

        @property
        def torsional_friction_node_pair(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_156.TorsionalFrictionNodePair":
            from mastapy.nodal_analysis.nodal_entities import _156

            return self._parent._cast(_156.TorsionalFrictionNodePair)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_157.TorsionalFrictionNodePairSimpleLockedStiffness":
            from mastapy.nodal_analysis.nodal_entities import _157

            return self._parent._cast(
                _157.TorsionalFrictionNodePairSimpleLockedStiffness
            )

        @property
        def two_body_connection_nodal_component(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "_158.TwoBodyConnectionNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _158

            return self._parent._cast(_158.TwoBodyConnectionNodalComponent)

        @property
        def component_nodal_composite(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite",
        ) -> "ComponentNodalComposite":
            return self._parent

        def __getattr__(
            self: "ComponentNodalComposite._Cast_ComponentNodalComposite", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentNodalComposite.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ComponentNodalComposite._Cast_ComponentNodalComposite":
        return self._Cast_ComponentNodalComposite(self)
