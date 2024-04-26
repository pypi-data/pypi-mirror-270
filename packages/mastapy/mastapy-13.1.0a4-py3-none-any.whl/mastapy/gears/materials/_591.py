"""BevelGearAbstractMaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.materials import _277
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_ABSTRACT_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "BevelGearAbstractMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.gears.materials import _594, _593
    from mastapy.utility.databases import _1843, _1846, _1839


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearAbstractMaterialDatabase",)


Self = TypeVar("Self", bound="BevelGearAbstractMaterialDatabase")
T = TypeVar("T", bound="_594.BevelGearMaterial")


class BevelGearAbstractMaterialDatabase(_277.MaterialDatabase[T]):
    """BevelGearAbstractMaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _BEVEL_GEAR_ABSTRACT_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearAbstractMaterialDatabase")

    class _Cast_BevelGearAbstractMaterialDatabase:
        """Special nested class for casting BevelGearAbstractMaterialDatabase to subclasses."""

        def __init__(
            self: "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase",
            parent: "BevelGearAbstractMaterialDatabase",
        ):
            self._parent = parent

        @property
        def material_database(
            self: "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase",
        ) -> "_277.MaterialDatabase":
            return self._parent._cast(_277.MaterialDatabase)

        @property
        def named_database(
            self: "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase",
        ) -> "_1843.NamedDatabase":
            from mastapy.utility.databases import _1843

            return self._parent._cast(_1843.NamedDatabase)

        @property
        def sql_database(
            self: "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase",
        ) -> "_1846.SQLDatabase":
            pass

            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.SQLDatabase)

        @property
        def database(
            self: "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase",
        ) -> "_1839.Database":
            pass

            from mastapy.utility.databases import _1839

            return self._parent._cast(_1839.Database)

        @property
        def bevel_gear_iso_material_database(
            self: "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase",
        ) -> "_593.BevelGearISOMaterialDatabase":
            from mastapy.gears.materials import _593

            return self._parent._cast(_593.BevelGearISOMaterialDatabase)

        @property
        def bevel_gear_abstract_material_database(
            self: "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase",
        ) -> "BevelGearAbstractMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase",
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
        self: Self, instance_to_wrap: "BevelGearAbstractMaterialDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearAbstractMaterialDatabase._Cast_BevelGearAbstractMaterialDatabase":
        return self._Cast_BevelGearAbstractMaterialDatabase(self)
