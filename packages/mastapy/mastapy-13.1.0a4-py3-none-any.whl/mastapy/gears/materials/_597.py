"""CylindricalGearISOMaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.materials import _599
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ISO_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "CylindricalGearISOMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.materials import _277
    from mastapy.utility.databases import _1843, _1846, _1839


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearISOMaterialDatabase",)


Self = TypeVar("Self", bound="CylindricalGearISOMaterialDatabase")


class CylindricalGearISOMaterialDatabase(
    _599.CylindricalGearMaterialDatabase["_604.ISOCylindricalGearMaterial"]
):
    """CylindricalGearISOMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_ISO_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearISOMaterialDatabase")

    class _Cast_CylindricalGearISOMaterialDatabase:
        """Special nested class for casting CylindricalGearISOMaterialDatabase to subclasses."""

        def __init__(
            self: "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase",
            parent: "CylindricalGearISOMaterialDatabase",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_material_database(
            self: "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase",
        ) -> "_599.CylindricalGearMaterialDatabase":
            return self._parent._cast(_599.CylindricalGearMaterialDatabase)

        @property
        def material_database(
            self: "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase",
        ) -> "_277.MaterialDatabase":
            from mastapy.materials import _277

            return self._parent._cast(_277.MaterialDatabase)

        @property
        def named_database(
            self: "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase",
        ) -> "_1843.NamedDatabase":
            from mastapy.utility.databases import _1843

            return self._parent._cast(_1843.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase",
        ) -> "_1846.SQLDatabase":
            pass

            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.SQLDatabase)

        @property
        def database(
            self: "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase",
        ) -> "_1839.Database":
            pass

            from mastapy.utility.databases import _1839

            return self._parent._cast(_1839.Database)

        @property
        def cylindrical_gear_iso_material_database(
            self: "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase",
        ) -> "CylindricalGearISOMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "CylindricalGearISOMaterialDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase":
        return self._Cast_CylindricalGearISOMaterialDatabase(self)
