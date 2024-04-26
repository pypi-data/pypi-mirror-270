"""CylindricalCutterDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1843
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_CUTTER_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "CylindricalCutterDatabase"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import (
        _720,
        _712,
        _718,
        _723,
        _724,
    )
    from mastapy.gears.manufacturing.cylindrical import _622, _633
    from mastapy.utility.databases import _1846, _1839


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalCutterDatabase",)


Self = TypeVar("Self", bound="CylindricalCutterDatabase")
T = TypeVar("T", bound="_720.CylindricalGearRealCutterDesign")


class CylindricalCutterDatabase(_1843.NamedDatabase[T]):
    """CylindricalCutterDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _CYLINDRICAL_CUTTER_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalCutterDatabase")

    class _Cast_CylindricalCutterDatabase:
        """Special nested class for casting CylindricalCutterDatabase to subclasses."""

        def __init__(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
            parent: "CylindricalCutterDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_1843.NamedDatabase":
            return self._parent._cast(_1843.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_1846.SQLDatabase":
            pass

            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.SQLDatabase)

        @property
        def database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_1839.Database":
            pass

            from mastapy.utility.databases import _1839

            return self._parent._cast(_1839.Database)

        @property
        def cylindrical_hob_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_622.CylindricalHobDatabase":
            from mastapy.gears.manufacturing.cylindrical import _622

            return self._parent._cast(_622.CylindricalHobDatabase)

        @property
        def cylindrical_shaper_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_633.CylindricalShaperDatabase":
            from mastapy.gears.manufacturing.cylindrical import _633

            return self._parent._cast(_633.CylindricalShaperDatabase)

        @property
        def cylindrical_formed_wheel_grinder_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_712.CylindricalFormedWheelGrinderDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _712

            return self._parent._cast(_712.CylindricalFormedWheelGrinderDatabase)

        @property
        def cylindrical_gear_plunge_shaver_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_718.CylindricalGearPlungeShaverDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _718

            return self._parent._cast(_718.CylindricalGearPlungeShaverDatabase)

        @property
        def cylindrical_gear_shaver_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_723.CylindricalGearShaverDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _723

            return self._parent._cast(_723.CylindricalGearShaverDatabase)

        @property
        def cylindrical_worm_grinder_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "_724.CylindricalWormGrinderDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _724

            return self._parent._cast(_724.CylindricalWormGrinderDatabase)

        @property
        def cylindrical_cutter_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "CylindricalCutterDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalCutterDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase":
        return self._Cast_CylindricalCutterDatabase(self)
