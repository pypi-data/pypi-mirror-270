"""NodalComposite"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _149
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_COMPOSITE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "NodalComposite"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import (
        _128,
        _129,
        _130,
        _134,
        _135,
        _141,
        _143,
        _144,
        _153,
        _154,
        _156,
        _157,
        _158,
    )


__docformat__ = "restructuredtext en"
__all__ = ("NodalComposite",)


Self = TypeVar("Self", bound="NodalComposite")


class NodalComposite(_149.NodalEntity):
    """NodalComposite

    This is a mastapy class.
    """

    TYPE = _NODAL_COMPOSITE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NodalComposite")

    class _Cast_NodalComposite:
        """Special nested class for casting NodalComposite to subclasses."""

        def __init__(
            self: "NodalComposite._Cast_NodalComposite", parent: "NodalComposite"
        ):
            self._parent = parent

        @property
        def nodal_entity(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_149.NodalEntity":
            return self._parent._cast(_149.NodalEntity)

        @property
        def bar_elastic_mbd(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_128.BarElasticMBD":
            from mastapy.nodal_analysis.nodal_entities import _128

            return self._parent._cast(_128.BarElasticMBD)

        @property
        def bar_mbd(self: "NodalComposite._Cast_NodalComposite") -> "_129.BarMBD":
            from mastapy.nodal_analysis.nodal_entities import _129

            return self._parent._cast(_129.BarMBD)

        @property
        def bar_rigid_mbd(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_130.BarRigidMBD":
            from mastapy.nodal_analysis.nodal_entities import _130

            return self._parent._cast(_130.BarRigidMBD)

        @property
        def component_nodal_composite(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_134.ComponentNodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _134

            return self._parent._cast(_134.ComponentNodalComposite)

        @property
        def concentric_connection_nodal_component(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_135.ConcentricConnectionNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _135

            return self._parent._cast(_135.ConcentricConnectionNodalComponent)

        @property
        def gear_mesh_nodal_component(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_141.GearMeshNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _141

            return self._parent._cast(_141.GearMeshNodalComponent)

        @property
        def gear_mesh_point_on_flank_contact(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_143.GearMeshPointOnFlankContact":
            from mastapy.nodal_analysis.nodal_entities import _143

            return self._parent._cast(_143.GearMeshPointOnFlankContact)

        @property
        def gear_mesh_single_flank_contact(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_144.GearMeshSingleFlankContact":
            from mastapy.nodal_analysis.nodal_entities import _144

            return self._parent._cast(_144.GearMeshSingleFlankContact)

        @property
        def simple_bar(self: "NodalComposite._Cast_NodalComposite") -> "_153.SimpleBar":
            from mastapy.nodal_analysis.nodal_entities import _153

            return self._parent._cast(_153.SimpleBar)

        @property
        def spline_contact_nodal_component(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_154.SplineContactNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _154

            return self._parent._cast(_154.SplineContactNodalComponent)

        @property
        def torsional_friction_node_pair(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_156.TorsionalFrictionNodePair":
            from mastapy.nodal_analysis.nodal_entities import _156

            return self._parent._cast(_156.TorsionalFrictionNodePair)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_157.TorsionalFrictionNodePairSimpleLockedStiffness":
            from mastapy.nodal_analysis.nodal_entities import _157

            return self._parent._cast(
                _157.TorsionalFrictionNodePairSimpleLockedStiffness
            )

        @property
        def two_body_connection_nodal_component(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "_158.TwoBodyConnectionNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _158

            return self._parent._cast(_158.TwoBodyConnectionNodalComponent)

        @property
        def nodal_composite(
            self: "NodalComposite._Cast_NodalComposite",
        ) -> "NodalComposite":
            return self._parent

        def __getattr__(self: "NodalComposite._Cast_NodalComposite", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NodalComposite.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "NodalComposite._Cast_NodalComposite":
        return self._Cast_NodalComposite(self)
