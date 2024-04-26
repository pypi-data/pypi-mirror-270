"""GearMaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1843
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "GearMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.gears.materials import _601, _595, _607
    from mastapy.utility.databases import _1846, _1839


__docformat__ = "restructuredtext en"
__all__ = ("GearMaterialDatabase",)


Self = TypeVar("Self", bound="GearMaterialDatabase")
T = TypeVar("T", bound="_601.GearMaterial")


class GearMaterialDatabase(_1843.NamedDatabase[T]):
    """GearMaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _GEAR_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMaterialDatabase")

    class _Cast_GearMaterialDatabase:
        """Special nested class for casting GearMaterialDatabase to subclasses."""

        def __init__(
            self: "GearMaterialDatabase._Cast_GearMaterialDatabase",
            parent: "GearMaterialDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "GearMaterialDatabase._Cast_GearMaterialDatabase",
        ) -> "_1843.NamedDatabase":
            return self._parent._cast(_1843.NamedDatabase)

        @property
        def sql_database(
            self: "GearMaterialDatabase._Cast_GearMaterialDatabase",
        ) -> "_1846.SQLDatabase":
            pass

            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.SQLDatabase)

        @property
        def database(
            self: "GearMaterialDatabase._Cast_GearMaterialDatabase",
        ) -> "_1839.Database":
            pass

            from mastapy.utility.databases import _1839

            return self._parent._cast(_1839.Database)

        @property
        def bevel_gear_material_database(
            self: "GearMaterialDatabase._Cast_GearMaterialDatabase",
        ) -> "_595.BevelGearMaterialDatabase":
            from mastapy.gears.materials import _595

            return self._parent._cast(_595.BevelGearMaterialDatabase)

        @property
        def klingelnberg_conical_gear_material_database(
            self: "GearMaterialDatabase._Cast_GearMaterialDatabase",
        ) -> "_607.KlingelnbergConicalGearMaterialDatabase":
            from mastapy.gears.materials import _607

            return self._parent._cast(_607.KlingelnbergConicalGearMaterialDatabase)

        @property
        def gear_material_database(
            self: "GearMaterialDatabase._Cast_GearMaterialDatabase",
        ) -> "GearMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "GearMaterialDatabase._Cast_GearMaterialDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearMaterialDatabase._Cast_GearMaterialDatabase":
        return self._Cast_GearMaterialDatabase(self)
