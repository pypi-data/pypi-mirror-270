"""BevelGearMeshRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.implicit import overridable
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.agma_gleason_conical import _572
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Bevel", "BevelGearMeshRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.bevel.standards import _565, _567
    from mastapy.gears.rating.iso_10300 import _432, _430
    from mastapy.gears.rating.conical import _552, _546
    from mastapy.gears.rating.zerol_bevel import _376
    from mastapy.gears.rating.straight_bevel import _402
    from mastapy.gears.rating.spiral_bevel import _409
    from mastapy.gears.rating import _367, _360
    from mastapy.gears.analysis import _1226


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshRating",)


Self = TypeVar("Self", bound="BevelGearMeshRating")


class BevelGearMeshRating(_572.AGMAGleasonConicalGearMeshRating):
    """BevelGearMeshRating

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshRating")

    class _Cast_BevelGearMeshRating:
        """Special nested class for casting BevelGearMeshRating to subclasses."""

        def __init__(
            self: "BevelGearMeshRating._Cast_BevelGearMeshRating",
            parent: "BevelGearMeshRating",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_rating(
            self: "BevelGearMeshRating._Cast_BevelGearMeshRating",
        ) -> "_572.AGMAGleasonConicalGearMeshRating":
            return self._parent._cast(_572.AGMAGleasonConicalGearMeshRating)

        @property
        def conical_gear_mesh_rating(
            self: "BevelGearMeshRating._Cast_BevelGearMeshRating",
        ) -> "_546.ConicalGearMeshRating":
            from mastapy.gears.rating.conical import _546

            return self._parent._cast(_546.ConicalGearMeshRating)

        @property
        def gear_mesh_rating(
            self: "BevelGearMeshRating._Cast_BevelGearMeshRating",
        ) -> "_367.GearMeshRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "BevelGearMeshRating._Cast_BevelGearMeshRating",
        ) -> "_360.AbstractGearMeshRating":
            from mastapy.gears.rating import _360

            return self._parent._cast(_360.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "BevelGearMeshRating._Cast_BevelGearMeshRating",
        ) -> "_1226.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1226

            return self._parent._cast(_1226.AbstractGearMeshAnalysis)

        @property
        def zerol_bevel_gear_mesh_rating(
            self: "BevelGearMeshRating._Cast_BevelGearMeshRating",
        ) -> "_376.ZerolBevelGearMeshRating":
            from mastapy.gears.rating.zerol_bevel import _376

            return self._parent._cast(_376.ZerolBevelGearMeshRating)

        @property
        def straight_bevel_gear_mesh_rating(
            self: "BevelGearMeshRating._Cast_BevelGearMeshRating",
        ) -> "_402.StraightBevelGearMeshRating":
            from mastapy.gears.rating.straight_bevel import _402

            return self._parent._cast(_402.StraightBevelGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(
            self: "BevelGearMeshRating._Cast_BevelGearMeshRating",
        ) -> "_409.SpiralBevelGearMeshRating":
            from mastapy.gears.rating.spiral_bevel import _409

            return self._parent._cast(_409.SpiralBevelGearMeshRating)

        @property
        def bevel_gear_mesh_rating(
            self: "BevelGearMeshRating._Cast_BevelGearMeshRating",
        ) -> "BevelGearMeshRating":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshRating._Cast_BevelGearMeshRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def size_factor_bending(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def size_factor_contact(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def agma_bevel_mesh_single_flank_rating(
        self: Self,
    ) -> "_565.AGMASpiralBevelMeshSingleFlankRating":
        """mastapy.gears.rating.bevel.standards.AGMASpiralBevelMeshSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMABevelMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gleason_bevel_mesh_single_flank_rating(
        self: Self,
    ) -> "_567.GleasonSpiralBevelMeshSingleFlankRating":
        """mastapy.gears.rating.bevel.standards.GleasonSpiralBevelMeshSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GleasonBevelMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def iso10300_bevel_mesh_single_flank_rating_method_b1(
        self: Self,
    ) -> "_432.ISO10300MeshSingleFlankRatingMethodB1":
        """mastapy.gears.rating.isoISO10300MeshSingleFlankRatingMethodB1

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO10300BevelMeshSingleFlankRatingMethodB1

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def iso10300_bevel_mesh_single_flank_rating_method_b2(
        self: Self,
    ) -> "_430.ISO10300MeshSingleFlankRatingBevelMethodB2":
        """mastapy.gears.rating.isoISO10300MeshSingleFlankRatingBevelMethodB2

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO10300BevelMeshSingleFlankRatingMethodB2

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def meshed_gears(self: Self) -> "List[_552.ConicalMeshedGearRating]":
        """List[mastapy.gears.rating.conical.ConicalMeshedGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gears_in_mesh(self: Self) -> "List[_552.ConicalMeshedGearRating]":
        """List[mastapy.gears.rating.conical.ConicalMeshedGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsInMesh

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "BevelGearMeshRating._Cast_BevelGearMeshRating":
        return self._Cast_BevelGearMeshRating(self)
