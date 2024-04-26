"""CylindricalWormGrinderDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical import _617
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_WORM_GRINDER_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters",
    "CylindricalWormGrinderDatabase",
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1843, _1846, _1839


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalWormGrinderDatabase",)


Self = TypeVar("Self", bound="CylindricalWormGrinderDatabase")


class CylindricalWormGrinderDatabase(
    _617.CylindricalCutterDatabase["_715.CylindricalGearGrindingWorm"]
):
    """CylindricalWormGrinderDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_WORM_GRINDER_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalWormGrinderDatabase")

    class _Cast_CylindricalWormGrinderDatabase:
        """Special nested class for casting CylindricalWormGrinderDatabase to subclasses."""

        def __init__(
            self: "CylindricalWormGrinderDatabase._Cast_CylindricalWormGrinderDatabase",
            parent: "CylindricalWormGrinderDatabase",
        ):
            self._parent = parent

        @property
        def cylindrical_cutter_database(
            self: "CylindricalWormGrinderDatabase._Cast_CylindricalWormGrinderDatabase",
        ) -> "_617.CylindricalCutterDatabase":
            return self._parent._cast(_617.CylindricalCutterDatabase)

        @property
        def named_database(
            self: "CylindricalWormGrinderDatabase._Cast_CylindricalWormGrinderDatabase",
        ) -> "_1843.NamedDatabase":
            from mastapy.utility.databases import _1843

            return self._parent._cast(_1843.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalWormGrinderDatabase._Cast_CylindricalWormGrinderDatabase",
        ) -> "_1846.SQLDatabase":
            pass

            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.SQLDatabase)

        @property
        def database(
            self: "CylindricalWormGrinderDatabase._Cast_CylindricalWormGrinderDatabase",
        ) -> "_1839.Database":
            pass

            from mastapy.utility.databases import _1839

            return self._parent._cast(_1839.Database)

        @property
        def cylindrical_worm_grinder_database(
            self: "CylindricalWormGrinderDatabase._Cast_CylindricalWormGrinderDatabase",
        ) -> "CylindricalWormGrinderDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalWormGrinderDatabase._Cast_CylindricalWormGrinderDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalWormGrinderDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalWormGrinderDatabase._Cast_CylindricalWormGrinderDatabase":
        return self._Cast_CylindricalWormGrinderDatabase(self)
