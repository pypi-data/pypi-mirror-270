"""ISO63361996MeshSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.cylindrical.iso6336 import _527
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO63361996_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336", "ISO63361996MeshSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.din3990 import _540
    from mastapy.gears.rating.cylindrical.iso6336 import _525
    from mastapy.gears.rating.cylindrical import _474
    from mastapy.gears.rating import _373


__docformat__ = "restructuredtext en"
__all__ = ("ISO63361996MeshSingleFlankRating",)


Self = TypeVar("Self", bound="ISO63361996MeshSingleFlankRating")


class ISO63361996MeshSingleFlankRating(_527.ISO6336AbstractMetalMeshSingleFlankRating):
    """ISO63361996MeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO63361996_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO63361996MeshSingleFlankRating")

    class _Cast_ISO63361996MeshSingleFlankRating:
        """Special nested class for casting ISO63361996MeshSingleFlankRating to subclasses."""

        def __init__(
            self: "ISO63361996MeshSingleFlankRating._Cast_ISO63361996MeshSingleFlankRating",
            parent: "ISO63361996MeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def iso6336_abstract_metal_mesh_single_flank_rating(
            self: "ISO63361996MeshSingleFlankRating._Cast_ISO63361996MeshSingleFlankRating",
        ) -> "_527.ISO6336AbstractMetalMeshSingleFlankRating":
            return self._parent._cast(_527.ISO6336AbstractMetalMeshSingleFlankRating)

        @property
        def iso6336_abstract_mesh_single_flank_rating(
            self: "ISO63361996MeshSingleFlankRating._Cast_ISO63361996MeshSingleFlankRating",
        ) -> "_525.ISO6336AbstractMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _525

            return self._parent._cast(_525.ISO6336AbstractMeshSingleFlankRating)

        @property
        def cylindrical_mesh_single_flank_rating(
            self: "ISO63361996MeshSingleFlankRating._Cast_ISO63361996MeshSingleFlankRating",
        ) -> "_474.CylindricalMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical import _474

            return self._parent._cast(_474.CylindricalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "ISO63361996MeshSingleFlankRating._Cast_ISO63361996MeshSingleFlankRating",
        ) -> "_373.MeshSingleFlankRating":
            from mastapy.gears.rating import _373

            return self._parent._cast(_373.MeshSingleFlankRating)

        @property
        def din3990_mesh_single_flank_rating(
            self: "ISO63361996MeshSingleFlankRating._Cast_ISO63361996MeshSingleFlankRating",
        ) -> "_540.DIN3990MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.din3990 import _540

            return self._parent._cast(_540.DIN3990MeshSingleFlankRating)

        @property
        def iso63361996_mesh_single_flank_rating(
            self: "ISO63361996MeshSingleFlankRating._Cast_ISO63361996MeshSingleFlankRating",
        ) -> "ISO63361996MeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "ISO63361996MeshSingleFlankRating._Cast_ISO63361996MeshSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO63361996MeshSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def helix_angle_factor_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixAngleFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def rating_standard_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingStandardName

        if temp is None:
            return ""

        return temp

    @property
    def transverse_load_factor_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseLoadFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ISO63361996MeshSingleFlankRating._Cast_ISO63361996MeshSingleFlankRating":
        return self._Cast_ISO63361996MeshSingleFlankRating(self)
