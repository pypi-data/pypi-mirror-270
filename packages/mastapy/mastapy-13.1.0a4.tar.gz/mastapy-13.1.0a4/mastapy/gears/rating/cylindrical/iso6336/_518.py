"""ISO63361996GearSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.cylindrical.iso6336 import _526
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO63361996_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336", "ISO63361996GearSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.din3990 import _539
    from mastapy.gears.rating.cylindrical.iso6336 import _524
    from mastapy.gears.rating.cylindrical import _472
    from mastapy.gears.rating import _371


__docformat__ = "restructuredtext en"
__all__ = ("ISO63361996GearSingleFlankRating",)


Self = TypeVar("Self", bound="ISO63361996GearSingleFlankRating")


class ISO63361996GearSingleFlankRating(_526.ISO6336AbstractMetalGearSingleFlankRating):
    """ISO63361996GearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO63361996_GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO63361996GearSingleFlankRating")

    class _Cast_ISO63361996GearSingleFlankRating:
        """Special nested class for casting ISO63361996GearSingleFlankRating to subclasses."""

        def __init__(
            self: "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating",
            parent: "ISO63361996GearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def iso6336_abstract_metal_gear_single_flank_rating(
            self: "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating",
        ) -> "_526.ISO6336AbstractMetalGearSingleFlankRating":
            return self._parent._cast(_526.ISO6336AbstractMetalGearSingleFlankRating)

        @property
        def iso6336_abstract_gear_single_flank_rating(
            self: "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating",
        ) -> "_524.ISO6336AbstractGearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _524

            return self._parent._cast(_524.ISO6336AbstractGearSingleFlankRating)

        @property
        def cylindrical_gear_single_flank_rating(
            self: "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating",
        ) -> "_472.CylindricalGearSingleFlankRating":
            from mastapy.gears.rating.cylindrical import _472

            return self._parent._cast(_472.CylindricalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating",
        ) -> "_371.GearSingleFlankRating":
            from mastapy.gears.rating import _371

            return self._parent._cast(_371.GearSingleFlankRating)

        @property
        def din3990_gear_single_flank_rating(
            self: "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating",
        ) -> "_539.DIN3990GearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.din3990 import _539

            return self._parent._cast(_539.DIN3990GearSingleFlankRating)

        @property
        def iso63361996_gear_single_flank_rating(
            self: "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating",
        ) -> "ISO63361996GearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO63361996GearSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def nominal_tooth_root_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalToothRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ISO63361996GearSingleFlankRating._Cast_ISO63361996GearSingleFlankRating":
        return self._Cast_ISO63361996GearSingleFlankRating(self)
