"""ExternalForceLineContactEntity"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _137
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_FORCE_LINE_CONTACT_ENTITY = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "ExternalForceLineContactEntity"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _147, _149


__docformat__ = "restructuredtext en"
__all__ = ("ExternalForceLineContactEntity",)


Self = TypeVar("Self", bound="ExternalForceLineContactEntity")


class ExternalForceLineContactEntity(_137.ExternalForceEntity):
    """ExternalForceLineContactEntity

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_FORCE_LINE_CONTACT_ENTITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ExternalForceLineContactEntity")

    class _Cast_ExternalForceLineContactEntity:
        """Special nested class for casting ExternalForceLineContactEntity to subclasses."""

        def __init__(
            self: "ExternalForceLineContactEntity._Cast_ExternalForceLineContactEntity",
            parent: "ExternalForceLineContactEntity",
        ):
            self._parent = parent

        @property
        def external_force_entity(
            self: "ExternalForceLineContactEntity._Cast_ExternalForceLineContactEntity",
        ) -> "_137.ExternalForceEntity":
            return self._parent._cast(_137.ExternalForceEntity)

        @property
        def nodal_component(
            self: "ExternalForceLineContactEntity._Cast_ExternalForceLineContactEntity",
        ) -> "_147.NodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalComponent)

        @property
        def nodal_entity(
            self: "ExternalForceLineContactEntity._Cast_ExternalForceLineContactEntity",
        ) -> "_149.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _149

            return self._parent._cast(_149.NodalEntity)

        @property
        def external_force_line_contact_entity(
            self: "ExternalForceLineContactEntity._Cast_ExternalForceLineContactEntity",
        ) -> "ExternalForceLineContactEntity":
            return self._parent

        def __getattr__(
            self: "ExternalForceLineContactEntity._Cast_ExternalForceLineContactEntity",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ExternalForceLineContactEntity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def interference_normal_maximum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InterferenceNormalMaximum

        if temp is None:
            return 0.0

        return temp

    @property
    def interference_normal_mean(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InterferenceNormalMean

        if temp is None:
            return 0.0

        return temp

    @property
    def misalignment_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalForce

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_normal(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessNormal

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_tilt(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessTilt

        if temp is None:
            return 0.0

        return temp

    @property
    def velocity_normal_mean(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VelocityNormalMean

        if temp is None:
            return 0.0

        return temp

    @property
    def velocity_normal_at_maximum_interference(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VelocityNormalAtMaximumInterference

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ExternalForceLineContactEntity._Cast_ExternalForceLineContactEntity":
        return self._Cast_ExternalForceLineContactEntity(self)
