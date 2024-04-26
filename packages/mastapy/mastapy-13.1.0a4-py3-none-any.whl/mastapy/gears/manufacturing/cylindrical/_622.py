"""CylindricalHobDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical import _617
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_HOB_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "CylindricalHobDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1843, _1846, _1839


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalHobDatabase",)


Self = TypeVar("Self", bound="CylindricalHobDatabase")


class CylindricalHobDatabase(
    _617.CylindricalCutterDatabase["_716.CylindricalGearHobDesign"]
):
    """CylindricalHobDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_HOB_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalHobDatabase")

    class _Cast_CylindricalHobDatabase:
        """Special nested class for casting CylindricalHobDatabase to subclasses."""

        def __init__(
            self: "CylindricalHobDatabase._Cast_CylindricalHobDatabase",
            parent: "CylindricalHobDatabase",
        ):
            self._parent = parent

        @property
        def cylindrical_cutter_database(
            self: "CylindricalHobDatabase._Cast_CylindricalHobDatabase",
        ) -> "_617.CylindricalCutterDatabase":
            return self._parent._cast(_617.CylindricalCutterDatabase)

        @property
        def named_database(
            self: "CylindricalHobDatabase._Cast_CylindricalHobDatabase",
        ) -> "_1843.NamedDatabase":
            from mastapy.utility.databases import _1843

            return self._parent._cast(_1843.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalHobDatabase._Cast_CylindricalHobDatabase",
        ) -> "_1846.SQLDatabase":
            pass

            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.SQLDatabase)

        @property
        def database(
            self: "CylindricalHobDatabase._Cast_CylindricalHobDatabase",
        ) -> "_1839.Database":
            pass

            from mastapy.utility.databases import _1839

            return self._parent._cast(_1839.Database)

        @property
        def cylindrical_hob_database(
            self: "CylindricalHobDatabase._Cast_CylindricalHobDatabase",
        ) -> "CylindricalHobDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalHobDatabase._Cast_CylindricalHobDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalHobDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CylindricalHobDatabase._Cast_CylindricalHobDatabase":
        return self._Cast_CylindricalHobDatabase(self)
