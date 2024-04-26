"""WindingMaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.materials import _277
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WINDING_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "WindingMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1843, _1846, _1839


__docformat__ = "restructuredtext en"
__all__ = ("WindingMaterialDatabase",)


Self = TypeVar("Self", bound="WindingMaterialDatabase")


class WindingMaterialDatabase(_277.MaterialDatabase["_1326.WindingMaterial"]):
    """WindingMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _WINDING_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WindingMaterialDatabase")

    class _Cast_WindingMaterialDatabase:
        """Special nested class for casting WindingMaterialDatabase to subclasses."""

        def __init__(
            self: "WindingMaterialDatabase._Cast_WindingMaterialDatabase",
            parent: "WindingMaterialDatabase",
        ):
            self._parent = parent

        @property
        def material_database(
            self: "WindingMaterialDatabase._Cast_WindingMaterialDatabase",
        ) -> "_277.MaterialDatabase":
            return self._parent._cast(_277.MaterialDatabase)

        @property
        def named_database(
            self: "WindingMaterialDatabase._Cast_WindingMaterialDatabase",
        ) -> "_1843.NamedDatabase":
            from mastapy.utility.databases import _1843

            return self._parent._cast(_1843.NamedDatabase)

        @property
        def sql_database(
            self: "WindingMaterialDatabase._Cast_WindingMaterialDatabase",
        ) -> "_1846.SQLDatabase":
            pass

            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.SQLDatabase)

        @property
        def database(
            self: "WindingMaterialDatabase._Cast_WindingMaterialDatabase",
        ) -> "_1839.Database":
            pass

            from mastapy.utility.databases import _1839

            return self._parent._cast(_1839.Database)

        @property
        def winding_material_database(
            self: "WindingMaterialDatabase._Cast_WindingMaterialDatabase",
        ) -> "WindingMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "WindingMaterialDatabase._Cast_WindingMaterialDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WindingMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "WindingMaterialDatabase._Cast_WindingMaterialDatabase":
        return self._Cast_WindingMaterialDatabase(self)
