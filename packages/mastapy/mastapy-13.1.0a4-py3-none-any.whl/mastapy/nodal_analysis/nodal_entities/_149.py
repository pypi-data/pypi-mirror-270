"""NodalEntity"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_ENTITY = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "NodalEntity"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import (
        _126,
        _127,
        _128,
        _129,
        _130,
        _132,
        _133,
        _134,
        _135,
        _136,
        _137,
        _138,
        _139,
        _140,
        _141,
        _142,
        _143,
        _144,
        _145,
        _146,
        _147,
        _148,
        _150,
        _151,
        _152,
        _153,
        _154,
        _155,
        _156,
        _157,
        _158,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2826


__docformat__ = "restructuredtext en"
__all__ = ("NodalEntity",)


Self = TypeVar("Self", bound="NodalEntity")


class NodalEntity(_0.APIBase):
    """NodalEntity

    This is a mastapy class.
    """

    TYPE = _NODAL_ENTITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NodalEntity")

    class _Cast_NodalEntity:
        """Special nested class for casting NodalEntity to subclasses."""

        def __init__(self: "NodalEntity._Cast_NodalEntity", parent: "NodalEntity"):
            self._parent = parent

        @property
        def arbitrary_nodal_component(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_126.ArbitraryNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _126

            return self._parent._cast(_126.ArbitraryNodalComponent)

        @property
        def bar(self: "NodalEntity._Cast_NodalEntity") -> "_127.Bar":
            from mastapy.nodal_analysis.nodal_entities import _127

            return self._parent._cast(_127.Bar)

        @property
        def bar_elastic_mbd(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_128.BarElasticMBD":
            from mastapy.nodal_analysis.nodal_entities import _128

            return self._parent._cast(_128.BarElasticMBD)

        @property
        def bar_mbd(self: "NodalEntity._Cast_NodalEntity") -> "_129.BarMBD":
            from mastapy.nodal_analysis.nodal_entities import _129

            return self._parent._cast(_129.BarMBD)

        @property
        def bar_rigid_mbd(self: "NodalEntity._Cast_NodalEntity") -> "_130.BarRigidMBD":
            from mastapy.nodal_analysis.nodal_entities import _130

            return self._parent._cast(_130.BarRigidMBD)

        @property
        def bearing_axial_mounting_clearance(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_132.BearingAxialMountingClearance":
            from mastapy.nodal_analysis.nodal_entities import _132

            return self._parent._cast(_132.BearingAxialMountingClearance)

        @property
        def cms_nodal_component(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_133.CMSNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _133

            return self._parent._cast(_133.CMSNodalComponent)

        @property
        def component_nodal_composite(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_134.ComponentNodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _134

            return self._parent._cast(_134.ComponentNodalComposite)

        @property
        def concentric_connection_nodal_component(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_135.ConcentricConnectionNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _135

            return self._parent._cast(_135.ConcentricConnectionNodalComponent)

        @property
        def distributed_rigid_bar_coupling(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_136.DistributedRigidBarCoupling":
            from mastapy.nodal_analysis.nodal_entities import _136

            return self._parent._cast(_136.DistributedRigidBarCoupling)

        @property
        def external_force_entity(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_137.ExternalForceEntity":
            from mastapy.nodal_analysis.nodal_entities import _137

            return self._parent._cast(_137.ExternalForceEntity)

        @property
        def external_force_line_contact_entity(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_138.ExternalForceLineContactEntity":
            from mastapy.nodal_analysis.nodal_entities import _138

            return self._parent._cast(_138.ExternalForceLineContactEntity)

        @property
        def external_force_single_point_entity(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_139.ExternalForceSinglePointEntity":
            from mastapy.nodal_analysis.nodal_entities import _139

            return self._parent._cast(_139.ExternalForceSinglePointEntity)

        @property
        def friction_nodal_component(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_140.FrictionNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _140

            return self._parent._cast(_140.FrictionNodalComponent)

        @property
        def gear_mesh_nodal_component(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_141.GearMeshNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _141

            return self._parent._cast(_141.GearMeshNodalComponent)

        @property
        def gear_mesh_node_pair(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_142.GearMeshNodePair":
            from mastapy.nodal_analysis.nodal_entities import _142

            return self._parent._cast(_142.GearMeshNodePair)

        @property
        def gear_mesh_point_on_flank_contact(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_143.GearMeshPointOnFlankContact":
            from mastapy.nodal_analysis.nodal_entities import _143

            return self._parent._cast(_143.GearMeshPointOnFlankContact)

        @property
        def gear_mesh_single_flank_contact(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_144.GearMeshSingleFlankContact":
            from mastapy.nodal_analysis.nodal_entities import _144

            return self._parent._cast(_144.GearMeshSingleFlankContact)

        @property
        def inertial_force_component(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_145.InertialForceComponent":
            from mastapy.nodal_analysis.nodal_entities import _145

            return self._parent._cast(_145.InertialForceComponent)

        @property
        def line_contact_stiffness_entity(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_146.LineContactStiffnessEntity":
            from mastapy.nodal_analysis.nodal_entities import _146

            return self._parent._cast(_146.LineContactStiffnessEntity)

        @property
        def nodal_component(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_147.NodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalComponent)

        @property
        def nodal_composite(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_148.NodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _148

            return self._parent._cast(_148.NodalComposite)

        @property
        def null_nodal_entity(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_150.NullNodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _150

            return self._parent._cast(_150.NullNodalEntity)

        @property
        def pid_control_nodal_component(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_151.PIDControlNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _151

            return self._parent._cast(_151.PIDControlNodalComponent)

        @property
        def rigid_bar(self: "NodalEntity._Cast_NodalEntity") -> "_152.RigidBar":
            from mastapy.nodal_analysis.nodal_entities import _152

            return self._parent._cast(_152.RigidBar)

        @property
        def simple_bar(self: "NodalEntity._Cast_NodalEntity") -> "_153.SimpleBar":
            from mastapy.nodal_analysis.nodal_entities import _153

            return self._parent._cast(_153.SimpleBar)

        @property
        def spline_contact_nodal_component(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_154.SplineContactNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _154

            return self._parent._cast(_154.SplineContactNodalComponent)

        @property
        def surface_to_surface_contact_stiffness_entity(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_155.SurfaceToSurfaceContactStiffnessEntity":
            from mastapy.nodal_analysis.nodal_entities import _155

            return self._parent._cast(_155.SurfaceToSurfaceContactStiffnessEntity)

        @property
        def torsional_friction_node_pair(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_156.TorsionalFrictionNodePair":
            from mastapy.nodal_analysis.nodal_entities import _156

            return self._parent._cast(_156.TorsionalFrictionNodePair)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_157.TorsionalFrictionNodePairSimpleLockedStiffness":
            from mastapy.nodal_analysis.nodal_entities import _157

            return self._parent._cast(
                _157.TorsionalFrictionNodePairSimpleLockedStiffness
            )

        @property
        def two_body_connection_nodal_component(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_158.TwoBodyConnectionNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _158

            return self._parent._cast(_158.TwoBodyConnectionNodalComponent)

        @property
        def shaft_section_system_deflection(
            self: "NodalEntity._Cast_NodalEntity",
        ) -> "_2826.ShaftSectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2826,
            )

            return self._parent._cast(_2826.ShaftSectionSystemDeflection)

        @property
        def nodal_entity(self: "NodalEntity._Cast_NodalEntity") -> "NodalEntity":
            return self._parent

        def __getattr__(self: "NodalEntity._Cast_NodalEntity", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NodalEntity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: Self) -> "NodalEntity._Cast_NodalEntity":
        return self._Cast_NodalEntity(self)
