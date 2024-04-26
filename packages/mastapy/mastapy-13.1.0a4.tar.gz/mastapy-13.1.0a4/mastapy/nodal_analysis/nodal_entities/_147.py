"""NodalComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _149
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "NodalComponent"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import (
        _126,
        _127,
        _132,
        _133,
        _136,
        _137,
        _138,
        _139,
        _140,
        _142,
        _145,
        _146,
        _151,
        _152,
        _155,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2826


__docformat__ = "restructuredtext en"
__all__ = ("NodalComponent",)


Self = TypeVar("Self", bound="NodalComponent")


class NodalComponent(_149.NodalEntity):
    """NodalComponent

    This is a mastapy class.
    """

    TYPE = _NODAL_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NodalComponent")

    class _Cast_NodalComponent:
        """Special nested class for casting NodalComponent to subclasses."""

        def __init__(
            self: "NodalComponent._Cast_NodalComponent", parent: "NodalComponent"
        ):
            self._parent = parent

        @property
        def nodal_entity(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_149.NodalEntity":
            return self._parent._cast(_149.NodalEntity)

        @property
        def arbitrary_nodal_component(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_126.ArbitraryNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _126

            return self._parent._cast(_126.ArbitraryNodalComponent)

        @property
        def bar(self: "NodalComponent._Cast_NodalComponent") -> "_127.Bar":
            from mastapy.nodal_analysis.nodal_entities import _127

            return self._parent._cast(_127.Bar)

        @property
        def bearing_axial_mounting_clearance(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_132.BearingAxialMountingClearance":
            from mastapy.nodal_analysis.nodal_entities import _132

            return self._parent._cast(_132.BearingAxialMountingClearance)

        @property
        def cms_nodal_component(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_133.CMSNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _133

            return self._parent._cast(_133.CMSNodalComponent)

        @property
        def distributed_rigid_bar_coupling(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_136.DistributedRigidBarCoupling":
            from mastapy.nodal_analysis.nodal_entities import _136

            return self._parent._cast(_136.DistributedRigidBarCoupling)

        @property
        def external_force_entity(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_137.ExternalForceEntity":
            from mastapy.nodal_analysis.nodal_entities import _137

            return self._parent._cast(_137.ExternalForceEntity)

        @property
        def external_force_line_contact_entity(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_138.ExternalForceLineContactEntity":
            from mastapy.nodal_analysis.nodal_entities import _138

            return self._parent._cast(_138.ExternalForceLineContactEntity)

        @property
        def external_force_single_point_entity(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_139.ExternalForceSinglePointEntity":
            from mastapy.nodal_analysis.nodal_entities import _139

            return self._parent._cast(_139.ExternalForceSinglePointEntity)

        @property
        def friction_nodal_component(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_140.FrictionNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _140

            return self._parent._cast(_140.FrictionNodalComponent)

        @property
        def gear_mesh_node_pair(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_142.GearMeshNodePair":
            from mastapy.nodal_analysis.nodal_entities import _142

            return self._parent._cast(_142.GearMeshNodePair)

        @property
        def inertial_force_component(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_145.InertialForceComponent":
            from mastapy.nodal_analysis.nodal_entities import _145

            return self._parent._cast(_145.InertialForceComponent)

        @property
        def line_contact_stiffness_entity(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_146.LineContactStiffnessEntity":
            from mastapy.nodal_analysis.nodal_entities import _146

            return self._parent._cast(_146.LineContactStiffnessEntity)

        @property
        def pid_control_nodal_component(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_151.PIDControlNodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _151

            return self._parent._cast(_151.PIDControlNodalComponent)

        @property
        def rigid_bar(self: "NodalComponent._Cast_NodalComponent") -> "_152.RigidBar":
            from mastapy.nodal_analysis.nodal_entities import _152

            return self._parent._cast(_152.RigidBar)

        @property
        def surface_to_surface_contact_stiffness_entity(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_155.SurfaceToSurfaceContactStiffnessEntity":
            from mastapy.nodal_analysis.nodal_entities import _155

            return self._parent._cast(_155.SurfaceToSurfaceContactStiffnessEntity)

        @property
        def shaft_section_system_deflection(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "_2826.ShaftSectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2826,
            )

            return self._parent._cast(_2826.ShaftSectionSystemDeflection)

        @property
        def nodal_component(
            self: "NodalComponent._Cast_NodalComponent",
        ) -> "NodalComponent":
            return self._parent

        def __getattr__(self: "NodalComponent._Cast_NodalComponent", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NodalComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "NodalComponent._Cast_NodalComponent":
        return self._Cast_NodalComponent(self)
