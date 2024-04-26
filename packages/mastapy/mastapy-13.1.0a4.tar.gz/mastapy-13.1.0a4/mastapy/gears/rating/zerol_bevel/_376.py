"""ZerolBevelGearMeshRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.bevel import _561
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.ZerolBevel", "ZerolBevelGearMeshRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.zerol_bevel import _961
    from mastapy.gears.rating.zerol_bevel import _377
    from mastapy.gears.rating.agma_gleason_conical import _572
    from mastapy.gears.rating.conical import _546
    from mastapy.gears.rating import _367, _360
    from mastapy.gears.analysis import _1226


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshRating",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshRating")


class ZerolBevelGearMeshRating(_561.BevelGearMeshRating):
    """ZerolBevelGearMeshRating

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearMeshRating")

    class _Cast_ZerolBevelGearMeshRating:
        """Special nested class for casting ZerolBevelGearMeshRating to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating",
            parent: "ZerolBevelGearMeshRating",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_rating(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating",
        ) -> "_561.BevelGearMeshRating":
            return self._parent._cast(_561.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating",
        ) -> "_572.AGMAGleasonConicalGearMeshRating":
            from mastapy.gears.rating.agma_gleason_conical import _572

            return self._parent._cast(_572.AGMAGleasonConicalGearMeshRating)

        @property
        def conical_gear_mesh_rating(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating",
        ) -> "_546.ConicalGearMeshRating":
            from mastapy.gears.rating.conical import _546

            return self._parent._cast(_546.ConicalGearMeshRating)

        @property
        def gear_mesh_rating(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating",
        ) -> "_367.GearMeshRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating",
        ) -> "_360.AbstractGearMeshRating":
            from mastapy.gears.rating import _360

            return self._parent._cast(_360.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating",
        ) -> "_1226.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1226

            return self._parent._cast(_1226.AbstractGearMeshAnalysis)

        @property
        def zerol_bevel_gear_mesh_rating(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating",
        ) -> "ZerolBevelGearMeshRating":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def zerol_bevel_gear_mesh(self: Self) -> "_961.ZerolBevelGearMeshDesign":
        """mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def zerol_bevel_gear_ratings(self: Self) -> "List[_377.ZerolBevelGearRating]":
        """List[mastapy.gears.rating.zerol_bevel.ZerolBevelGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating":
        return self._Cast_ZerolBevelGearMeshRating(self)
