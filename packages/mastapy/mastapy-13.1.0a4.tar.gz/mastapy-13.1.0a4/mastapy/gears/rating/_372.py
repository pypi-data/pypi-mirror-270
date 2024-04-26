"""MeshDutyCycleRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.gears.rating import _360
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESH_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "MeshDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _365
    from mastapy.gears.rating.worm import _384
    from mastapy.gears.rating.face import _453
    from mastapy.gears.rating.cylindrical import _473
    from mastapy.gears.rating.conical import _551
    from mastapy.gears.rating.concept import _556
    from mastapy.gears.analysis import _1226


__docformat__ = "restructuredtext en"
__all__ = ("MeshDutyCycleRating",)


Self = TypeVar("Self", bound="MeshDutyCycleRating")


class MeshDutyCycleRating(_360.AbstractGearMeshRating):
    """MeshDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _MESH_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeshDutyCycleRating")

    class _Cast_MeshDutyCycleRating:
        """Special nested class for casting MeshDutyCycleRating to subclasses."""

        def __init__(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
            parent: "MeshDutyCycleRating",
        ):
            self._parent = parent

        @property
        def abstract_gear_mesh_rating(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
        ) -> "_360.AbstractGearMeshRating":
            return self._parent._cast(_360.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
        ) -> "_1226.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1226

            return self._parent._cast(_1226.AbstractGearMeshAnalysis)

        @property
        def worm_mesh_duty_cycle_rating(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
        ) -> "_384.WormMeshDutyCycleRating":
            from mastapy.gears.rating.worm import _384

            return self._parent._cast(_384.WormMeshDutyCycleRating)

        @property
        def face_gear_mesh_duty_cycle_rating(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
        ) -> "_453.FaceGearMeshDutyCycleRating":
            from mastapy.gears.rating.face import _453

            return self._parent._cast(_453.FaceGearMeshDutyCycleRating)

        @property
        def cylindrical_mesh_duty_cycle_rating(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
        ) -> "_473.CylindricalMeshDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _473

            return self._parent._cast(_473.CylindricalMeshDutyCycleRating)

        @property
        def conical_mesh_duty_cycle_rating(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
        ) -> "_551.ConicalMeshDutyCycleRating":
            from mastapy.gears.rating.conical import _551

            return self._parent._cast(_551.ConicalMeshDutyCycleRating)

        @property
        def concept_gear_mesh_duty_cycle_rating(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
        ) -> "_556.ConceptGearMeshDutyCycleRating":
            from mastapy.gears.rating.concept import _556

            return self._parent._cast(_556.ConceptGearMeshDutyCycleRating)

        @property
        def mesh_duty_cycle_rating(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
        ) -> "MeshDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MeshDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def energy_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EnergyLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_efficiency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshEfficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def total_energy(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalEnergy

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_duty_cycle_ratings(self: Self) -> "List[_365.GearDutyCycleRating]":
        """List[mastapy.gears.rating.GearDutyCycleRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "MeshDutyCycleRating._Cast_MeshDutyCycleRating":
        return self._Cast_MeshDutyCycleRating(self)
